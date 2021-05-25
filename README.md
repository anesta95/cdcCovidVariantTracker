# cdcCovidVariantTracker

This is a repository that uses Bertrand Martel's [Tableau Scraper](https://pypi.org/project/TableauScraper/) library in order to scrape the COVID-19 case proportion for HHS region from the [CDC Covid Data Tracker](https://covid.cdc.gov/covid-data-tracker/#variant-proportions).

Data is taken from the nationwide HHS region map instead of the state-by-state Tableau table
further down in the website because of the statistical weighting that is incorporated into the map percentages that makes them more reliable.

Per the CDC: The data below show the estimated biweekly proportions of the most common SARS-CoV-2 lineages circulating in the United States, based on greater than 175,000 sequences collected through CDC’s national genomic surveillance since Dec 20, 2020 and grouped in 2-week intervals.

The `cdcVariantData.csv` file is then updated by the script at 12:30pm every Tuesday and Thursday to update the [Datawrapper](https://app.datawrapper.de) COVID-19 Variant viz at [VeryWell health](https://www.verywellhealth.com/)