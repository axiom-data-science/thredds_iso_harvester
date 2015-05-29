# thredds_iso_harvester

Python class/script to harvest ISO metadata records from an [__ncISO enabled__](https://www.unidata.ucar.edu/software/thredds/v4.3/tds/tds4.2/reference/ncISO.html) [THREDDS](http://www.unidata.ucar.edu/software/thredds/current/tds/TDS.html) server.

See https://www.unidata.ucar.edu/software/thredds/v4.3/tds/tds4.2/reference/ncISO.html for instructions on enabling ncISO in [THREDDS](http://www.unidata.ucar.edu/software/thredds/current/tds/TDS.html).

## Install

First install [lxml's dependencies](http://lxml.de/installation.html#requirements):

```
sudo apt-get install libxml2-dev libxslt-dev python-dev
```

Then install using pip:

```
pip install git+git://github.com/axiom-data-science/thredds_iso_harvester
```

## Upgrade

```
pip install --upgrade --no-deps git+git://github.com/axiom-data-science/thredds_iso_harvester
pip install git+git://github.com/axiom-data-science/thredds_iso_harvester
```

Note: depending on your pip installation, you may need to run the above command using sudo.

## Usage

thredds-iso-harvester can be run from the command line or as a Python class.

### Command line

Run

```
./thredds_iso_harvester.py -h
```

to view options.

Example run:

```
./thredds_iso_harvester.py --output-dir=/srv/http/iso-waf --log=/var/log/iso-harvest.log \
  http://yourserver.org/thredds/catalog.html
```

Example for downloading a subset of data sets:
```
./thredds_iso_harvester.py --output-dir=/srv/http/iso-waf --log=/var/log/iso-harvest.log \
  --select=DATASET1 --select=ANOTHER_DATASET_ID \ 
  http://yourserver.org/thredds/catalog.html
```

### Python class

```
from thredds_iso_harvester.harvest import ThreddsIsoHarvester

ThreddsIsoHarvester(catalog_url="http://yourserver.org/thredds/catalog.html", out_dir="/srv/http/iso-waf")
```
