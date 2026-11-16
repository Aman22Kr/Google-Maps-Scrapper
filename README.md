# Google-Maps-Scrapper
This Python script utilises the Playwright library to perform web scraping and data extraction from Google Maps. It is particularly designed for obtaining information about businesses, including their name, address, website, phone number, reviews, and more.

## Read Prerequisites
The latest Python was not used and is not recommended

## Prerequisites
- Python 3.8 or 3.9 (Python 3.10+ may not be compatible with some dependencies)
- Chromium browser installed (for Playwright)

## Multiple Branches
The repo currently has 3 branches
- Main
- Latest Libraries (The one that works with the latest libraries; can cause issues. Prefer Main)
- Linux ( Linux Support if the main branch does not work correctly)


## Key Features
- Data Scraping: The script scrapes data from Google Maps listings, extracting valuable information about businesses, such as their name, address, website, and contact details.

- Review Analysis: It extracts review counts and average ratings, providing insights into businesses' online reputation.

- Business Type Detection: The script identifies whether a business offers in-store shopping, in-store pickup, or delivery services.

- Operating Hours: It extracts information about the business's operating hours.

- Introduction Extraction: The script also scrapes introductory information about the businesses when available.

- Data Cleansing: It cleanses and organizes the scraped data, removing redundant or unnecessary columns.

- CSV Export: The cleaned data is exported to a CSV file for further analysis or integration with other tools.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Aman22Kr/Google-Maps-Scrapper.git
   cd Google-Maps-Scrapper
   ```
2. Install Python dependencies:
   ```
   pip install -r requirements.txt
   ```
3. restart your system

4. Install Playwright browsers:
   ```bash
   playwright install
   ```

## Usage

Run the script with your desired search term and number of results:

```bash
python main.py -s "Turkish Restaurants in Toronto Canada" -t 20
```

- `-s` or `--search`: Search query for Google Maps (default: "turkish stores in toronto Canada")
- `-t` or `--total`: Number of results to scrape (default: 1)
- `-o` or `--output`: Output CSV file path (default: result.csv)
- `--append`: Append results to the output file instead of overwriting (default: off)

## Example

1. Append new results to an existing CSV file:
```
python main.py -s "Diagnostic Centre in Kharar Punjab" -t 20 -o DiagnosticCentreinKhararPunjab.csv --append
```

The script will launch a browser, perform the search, and start scraping information. The script displays progress in the terminal and saves results to the specified CSV file. If `--append` is used, new results will be added to the end of the file without removing previous data.

2. For many scrapes in a short period, put the prompt in queries.txt and run `runer.py`.
   ```
   cd data
   python3 aamerge.csv.py
   ```
   OR
   ```
   cd data
   python aamerge.csv.py
   ```


## Notes
- The script opens a visible browser window (not headless) for scraping.
- Google Maps DOM may change, which can break the script. If you encounter issues, update the XPaths in `main.py`.

