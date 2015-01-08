#! /usr/bin/python

import os
import sys
import requests
import argparse
from thredds_crawler.crawl import Crawl

import logging
import logging.handlers

formatter = logging.Formatter('%(asctime)s - [%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger.addHandler(ch)
logger.setLevel(logging.DEBUG)

class ThreddsIsoHarvester:
    def __init__(self, catalog_url, out_dir, log_file=None, select=None, skip=None):
        if log_file is not None:
           self.__add_file_logger(log_file)
        if skip is None:
            skip = Crawl.SKIPS
        else:
            skip.extend(Crawl.SKIPS)
        found_isos = []
        catalog = Crawl(catalog_url, select=select, skip=skip, debug=True)
        isos = [(d.id, s.get("url")) for d in catalog.datasets for s in d.services if s.get("service").lower() == "iso"]
        for iso in isos:
            try:
                filename = iso[0].replace("/", "_") + ".iso.xml"
                found_isos.append(filename)
                filepath = os.path.join(out_dir, filename)
                logger.info("Downloading/Saving %s" % filepath)

                r = requests.get(iso[1], stream=True)
                if r.ok:
                    with open(filepath, 'wb') as f:
                        for chunk in r.iter_content():
                            if chunk:
                                f.write(chunk)
                else:
                    logger.info("Got a non-200 status code (%s) from %s" % (r.status_code, iso[1]))
            except KeyboardInterrupt:
                logger.info("Caught interrupt, exiting")
                sys.exit(0)
            except BaseException:
                logger.exception("Error!")
        self.__clean_not_found_files(out_dir, found_isos)

    def __add_file_logger(self, log_file):
        fh = logging.handlers.RotatingFileHandler(log_file, maxBytes=1024*1024*10, backupCount=5)
        fh.setLevel(logging.INFO)
        fh.setFormatter(formatter)
        logger.addHandler(fh)

    def __clean_not_found_files(self, check_dir, found_files):
        for f in os.listdir(check_dir):
            if (f not in found_files):
                logger.info("%s not found in catalog, deleting...", f)
                os.remove(os.path.join(check_dir, f))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Harvest ISO records from an ncISO enabled THREDDS server.')
    parser.add_argument('--output-dir', '-o', dest='out_dir', required=True, help='ISO output directory')
    parser.add_argument('--select', '-s', dest='select', action='append', help='Data set select pattern (accepts multiple)')
    parser.add_argument('--skip', '-x', dest='skip', action='append', help='Data set skip pattern (accepts multiple)')
    parser.add_argument('--log', '-l', dest='log_file', help='Log file')
    parser.add_argument('catalog_url', help='THREDDS catalog URL to parse')
    parser.set_defaults(defaultSkips=True)
    args = parser.parse_args()
    ThreddsIsoHarvester(catalog_url=args.catalog_url, out_dir=args.out_dir, log_file=args.log_file, select=args.select, skip=args.skip)
