# Synthetic inputs
One row is one invented household, hypothetical survey year 2026. All observations
have equal weight. These data describe no real people or regional population.
Income and consumption are EUR per month; size is persons. IDs are strings.
region_code maps N/S/E/W to North/South/East/West in the four-row regions.csv.
Generation: scripts/generate-day-2-data.py, Python random seed 20261111.
There are 201 source rows: 200 households and one exact duplicate. Two income
entries and three consumption entries are unusable. Two complete households
have observed zero income. The declared worked policy retains 195 households
and 193 defined saving shares. Complete-record exclusion is a classroom policy
to discuss, not a universal missing-data recommendation. Preserve raw files.
