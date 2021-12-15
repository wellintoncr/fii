# FIIs Extractor

## Idea

This project is intended to extract FIIs (*Fundos de Investimento Imobiliário*, in Portuguese) from Bovespa reports. Usually, there are two types of useful reports: monthly report and dividend report. The former is an overview about this investment and it is released once a month, usually. The latter is, as its name suggests, a report about dividend performance and it is released once a month, usually.

### What it does NOT do

If you are looking for information that is not present in any of the above reports, you can improve this project to do so, but currently it supports only two reports.

### What it WILL (maybe) do

These two reports contain more information than collected by this project. Maybe, it would be useful to get more fields and it is quite simple to do: just inspect the page and look for a pattern.

## How to use

### Environment

First of all, it is advised you use a virtual env for this project. So,
```sh
python3 -m venv .venv
source .venv/bin/activate
```

### Installing dependencies

Just install all dependencies from requirements file
```sh
pip3 install -r requirements.txt
```
After installation, you are ready to use this project

### Creating instances

Currently, it is pretty simple and straightforward to extract data: first, create an instance of a report that you want to get. To do so, pass a parameter called `base_url`. For now, this is *http://fnet.bmfbovespa.com.br*.

Then, you run `get_report_from_document_id` and pass a parameter called `document_id`. This value represents which page you are trying to collect data from. You will need to search for a report and then copy this `document_id`. For instance, if you visited *https://fnet.bmfbovespa.com.br/fnet/publico/exibirDocumento?id=229904*, `document_id` is **229904**.

After running the above method, you will get a dict or an exception.


## Things to know

If you provide a `base_url` as **https** you may have problems with certificates. You can try to solve that or just drop the `s` and make it just **http**.