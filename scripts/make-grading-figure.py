#!/usr/bin/env python3
"""Render the syllabus grading scheme as PNG, SVG, and a one-page PDF.

Run with the project's research-methods Python environment:
    python scripts/make-grading-figure.py

Weights and pass thresholds are read from syllabus.md so the figure can be
checked against its source. Style defaults adapt the generate-python-figures
skill's matplotlib helper; no files outside this repository are required.
"""

from __future__ import annotations

import argparse
import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".cache" / "matplotlib"))

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


INK = "#202B33"
MUTED = "#57636D"
RULE = "#DDE2E5"
COLORS = {
    "submission": "#A75019",
    "independent": "#225A84",
    "writing": "#737373",
}

COMPONENTS = (
    "Exercise 1 submission",
    "Exercise 1 individual test",
    "Exercise 2 submission",
    "Exercise 2 individual test",
    "Day 3 individual practical",
    "Writing component",
)


def read_scheme(path: Path) -> tuple[list[int], float, float]:
    source = path.read_text(encoding="utf-8")
    section = source.split("## Assessment and grading", 1)[1]
    rows = dict(
        (name.strip(), int(weight))
        for name, weight in re.findall(
            r"^\| ([^|]+) \| (\d+)% \|", section, re.MULTILINE
        )
    )
    weights = [rows[name] for name in COMPONENTS]
    overall = re.search(r"\*\*Pass requirements:\*\* at least (\d+(?:\.\d+)?)% overall", section)
    independent = re.search(
        r"at least \*\*(\d+(?:\.\d+)?) out of (\d+) points in aggregate\*\*", section
    )
    if overall is None or independent is None:
        raise ValueError("Could not find the syllabus pass thresholds.")
    independent_total = weights[1] + weights[3] + weights[4]
    minimum = float(independent.group(1))
    if sum(weights) != 100 or any(weight <= 0 for weight in weights):
        raise ValueError("Component weights must be positive and sum to 100%.")
    if int(independent.group(2)) != independent_total:
        raise ValueError("Independent-assessment denominator disagrees with the weights.")
    if not 0 < minimum <= independent_total:
        raise ValueError("Independent pass threshold is outside the available points.")
    return weights, float(overall.group(1)), minimum


def quiet_axes(fig, bounds, xlim, ylim):
    ax = fig.add_axes(bounds)
    ax.set(xlim=xlim, ylim=ylim)
    ax.set_axis_off()
    return ax


def block(ax, left, bottom, width, height, color, label, size=15):
    ax.add_patch(
        Rectangle((left, bottom), width, height, facecolor=color, edgecolor="white", linewidth=1.1)
    )
    ax.text(
        left + width / 2,
        bottom + height / 2,
        label,
        ha="center",
        va="center",
        color="white",
        fontsize=size,
        linespacing=1.2,
    )


def render(syllabus: Path, output: Path) -> None:
    weights, overall_minimum, independent_minimum = read_scheme(syllabus)
    s1, t1, s2, t2, practical, writing = weights
    submissions = s1 + s2
    independent = t1 + t2 + practical
    programming = submissions + independent

    plt.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "font.size": 14,
            "text.color": INK,
            "figure.facecolor": "white",
            "savefig.facecolor": "white",
            "axes.grid": False,
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
            "svg.fonttype": "none",
            "svg.hashsalt": "research-methods-grading",
        }
    )
    fig = plt.figure(figsize=(7.2, 11.8))
    left, width = 0.08, 0.84

    def text(y, label, size=14, color=INK, weight="normal", **kwargs):
        return fig.text(left, y, label, fontsize=size, color=color, weight=weight, **kwargs)

    text(0.895, "Every percentage is a share of the whole course.", 12.5, MUTED)

    # An honest 100% bar: the first two segments form the programming part.
    whole = quiet_axes(fig, [left, 0.765, width, 0.115], (0, 100), (0, 2.2))
    block(whole, 0, 0.10, submissions, 1.0, COLORS["submission"], f"Take-home\n{submissions}%", 13)
    block(whole, submissions, 0.10, independent, 1.0, COLORS["independent"], f"Independent\n{independent}%", 15)
    block(whole, programming, 0.10, writing, 1.0, COLORS["writing"], f"Writing\n{writing}%", 15)
    whole.plot([0, 0, programming, programming], [1.25, 1.42, 1.42, 1.25], color=MUTED, lw=0.8)
    whole.text(programming / 2, 1.65, f"Programming & research · {programming}%", ha="center", fontsize=13, weight="bold")
    text(0.740, "Take-home: AI allowed. Independent: no AI.", 12, MUTED)

    text(0.697, "Where the marks come from", 19, weight="bold")
    detail_max = max(s1 + t1, s2 + t2, practical, writing) + 2
    detail = quiet_axes(fig, [left, 0.337, width, 0.328], (0, detail_max), (0, 4.9))
    rows = [
        ("Exercise 1", s1 + t1, [(s1, "submission", f"Submission\n{s1}%"), (t1, "independent", f"MCQ test\n{t1}%")]),
        ("Exercise 2", s2 + t2, [(s2, "submission", f"Submission\n{s2}%"), (t2, "independent", f"MCQ test\n{t2}%")]),
        ("Day 3 practical", practical, [(practical, "independent", f"Individual practical · {practical}%")]),
        ("Writing", writing, [(writing, "writing", f"Other lecturer · {writing}%")]),
    ]
    for index, (label, total, segments) in enumerate(rows):
        heading_y = 4.65 - index * 1.2
        detail.text(0, heading_y, label, fontsize=15, weight="bold", va="center")
        detail.text(detail_max, heading_y, f"{total}%", fontsize=15, weight="bold", ha="right", va="center")
        offset = 0
        for value, category, segment_label in segments:
            block(detail, offset, heading_y - 0.86, value, 0.67, COLORS[category], segment_label, 14)
            offset += value
    # A shared zero baseline and shared scale make row lengths comparable.
    detail.plot([0, detail_max], [0.03, 0.03], color=RULE, lw=0.7)
    for value in range(0, detail_max + 1, 10):
        detail.plot([value, value], [0.03, -0.035], color=RULE, lw=0.7, clip_on=False)
        detail.text(value, -0.17, f"{value}%", fontsize=10, color=MUTED, ha="center", clip_on=False)

    text(0.284, "To pass, meet both requirements", 18, weight="bold")
    text(0.247, f"At least {overall_minimum:g} / 100 overall", 20, weight="bold")
    text(0.219, "AND", 10.5, MUTED, "bold")
    text(0.187, f"At least {independent_minimum:g} / {independent} independent points", 17.5, COLORS["independent"], "bold")
    text(0.161, f"Tests ({t1} + {t2}) and practical ({practical}), combined.", 12, MUTED)
    text(0.138, f"At least {100 * independent_minimum / independent:g}% across these three assessments together.", 11.5, MUTED)

    fig.add_artist(plt.Line2D([left, left + width], [0.116, 0.116], transform=fig.transFigure, color=RULE, lw=0.8))
    text(0.091, "Example: full submission marks + 40% on the test", 11.5, MUTED)
    text(0.063, f"{s1} + {0.4 * t1:g} = {s1 + 0.4 * t1:g} / {s1 + t1} for that exercise", 18, weight="bold")
    text(0.028, "Pass requirements subject to institutional confirmation.", 10, MUTED)

    output.mkdir(parents=True, exist_ok=True)
    stem = output / "grading-overview"
    for extension in ("png", "svg", "pdf"):
        metadata = {"Creator": "Research Methods 2026"}
        if extension == "svg":
            metadata["Date"] = None
            metadata["Title"] = "How your Research Methods grade works"
            metadata["Description"] = (
                f"Programming {programming}% and writing {writing}%. "
                f"Exercise 1: {s1}% submission plus {t1}% individual test. "
                f"Exercise 2: {s2}% submission plus {t2}% individual test. "
                f"Final practical: {practical}%. Pass requires at least "
                f"{overall_minimum:g}/100 overall and {independent_minimum:g}/{independent} "
                "across the individual tests and practical combined."
            )
        elif extension == "pdf":
            metadata["CreationDate"] = None
            metadata["ModDate"] = None
        path = stem.with_suffix(f".{extension}")
        fig.savefig(path, dpi=200, bbox_inches="tight", pad_inches=0.15, metadata=metadata)
        if extension == "svg":
            # Matplotlib leaves trailing spaces in multiline path attributes.
            lines = path.read_text(encoding="utf-8").splitlines()
            path.write_text("\n".join(line.rstrip() for line in lines) + "\n", encoding="utf-8")
        print(path.relative_to(ROOT) if path.is_relative_to(ROOT) else path)
    plt.close(fig)
    print(f"Verified: {programming}% programming + {writing}% writing = 100%; independent pool = {independent} points.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--syllabus", type=Path, default=ROOT / "syllabus.md")
    parser.add_argument("--output-dir", type=Path, default=ROOT / "docs" / "figures")
    args = parser.parse_args()
    render(args.syllabus, args.output_dir)
