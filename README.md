# **Python - Financial Reporter**
> Created by Matthew Farmer

## About
Financial Reporter, written in Python, is a command line program designed to gather the values of your current assets and liabilities. Each asset/liability is entered separately and is given its own value by the user. Once the user has indicated that all sources/values have been provided, a summary of one's net worth is printed to the console and a printer-friendly report file is generated inside the current folder.

## Run Program
`python finrep.py`

### Assets

The application will prompt users for the name an asset source, then its value, and then whether or not the user would like to add another asset source.
![ Assets ](/demoMedia/assets.png)

### Liabilities

Once the user has indicated that all desired asset sources have been entered, it will then prompt the user for any liability sources. Similarly to the assets section, users will be prompted for liability source names and values until it has been indicated that there are no more to enter.
![ Liabilities ](/demoMedia/liabilities.png)

### Net Worth

Upon conclusion of entering liability sources, users will see printed to the console a summary of total assets, total liabilities, and current net worth.
![ Net Worth ](/demoMedia/netWorth.png)

### Generated Report

In addition to viewing the final results as printed to the console, a printer-friendly report will be generated in the current folder that reflects all information entered.
![ Generated Report ](/demoMedia/generatedReport.png)
