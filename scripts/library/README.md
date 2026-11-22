# KEEBOX Library importer

Rebuilds `docs/library/` from the lists in [sindresorhus/awesome](https://github.com/sindresorhus/awesome).

Rules:

- **Public domain** (CC0, Unlicense) → imported into `docs/library/` with a source credit on each page.
- **Requires attribution** (MIT, CC BY, CC BY-SA, Apache, GPL, …) → credited on `docs/credits.md`, not copied.
- **No license / non-commercial / no-derivatives** → not reproduced.

## Run

```bash
cd scripts/library
mkdir -p work && cd work
curl -s https://raw.githubusercontent.com/sindresorhus/awesome/main/readme.md -o awesome.md
# 1. parse the master list into lists.json (see parse step in ../fetch.py header)
python3 ../fetch.py      # downloads READMEs + licenses into raw/ (re-run until 100%)
python3 ../classify.py   # writes classified.json
python3 ../genlib.py     # converts public-domain lists
python3 ../writelib.py   # writes docs/library/*.md
```

Then rebuild the Credits page and run `mkdocs build --strict` before committing.
