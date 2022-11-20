# FIIs Extractor

## Idea

This project is intended to extract and analyze FIIs (*Fundos de Investimento Imobiliário*, in Portuguese) from Bovespa reports. Usually, there are two types of useful reports: monthly report and dividend report. The former is an overview about this investment and it is released once a month, usually. The latter is, as its name suggests, a report about dividend performance and it is released once a month, usually.

### What it does NOT do

If you are looking for information that is not present in any of the above reports, you can improve this project to do so, but currently it supports only two reports.

### What it WILL (maybe) do

These two reports contain more information than collected by this project. It might be useful to get more fields and it is quite simple to do: just inspect the page and look for a pattern.

## Requirements

*  docker-compose 1.29+
*  docker 20.10+

## How to use it

Just run:
```sh
./exec all  # This terminal will be 'locked' because it will be attached to all containers
```

To see all options available, run:
```sh
./exec
```

And then you can execute something like `./exec tests`

## Current flow

First, verify how many documents will be extracted and save this number into `webpage_extractor/script.py` (variable **batch_size**). You can change the failure threshold as well, so this script will check whether previous extraction process had more errors than expected. If so, it will not proceed.

Usually, the first couple attempts to scrap should have small *batch_size* so you can quickly check whether it is working or something went bad, such as connection issues. After testing this step, you can increase *batch_size* to tens or hundreds of thousands documents. Of course, it will take longer, but you will have more data.

Then, you should wait the script to finish this step (it may take a while depending on how many documents you want to save). After that, all valid documents will be saved onto **webpages_dump** folder. Not found documents will be saved onto **webpages_not_found** as well.

After saving all documents you need, you can execute `web_scraper/script.py` and, if everything goes well, a dense file will be created at **reports_data/reports.json**. This file contains all available reports based on all files extracted on the previous step.


The steps below is yet to be implemented.
~~To get stock prices (how much a fund's quote is worth), you should run `stock/script.py`.~~

~~Then, you can execute `analyzer/script.py` to evaluate all reports and generate more data which should be helpful to measure funds' quality. If the final report is still "irrelevant" (it has just a few data), so you should increase the *batch_size* variable in the scraping step and keep extracting data until you have enough information.~~


