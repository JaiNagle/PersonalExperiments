# Personal Experiments

A scratchpad for small Python experiments I use to learn new libraries and techniques.

## Experiments

### `web_scraping.py`: IMDb top-rated TV shows

Scrapes the IMDb Top Rated TV Shows chart with `requests` and `BeautifulSoup`, collecting each show's title, year and rating into a `pandas` DataFrame and exporting it to `test1.xlsx`.

```bash
pip install requests beautifulsoup4 pandas openpyxl
python web_scraping.py
```

> IMDb has changed its chart markup since this was written, so the CSS selectors (`titleColumn`, `ratingColumn`) may no longer match and the script would need updating. Check a site's terms and `robots.txt` before scraping it.

## More soon

New experiments will be added as separate scripts in this repo.
