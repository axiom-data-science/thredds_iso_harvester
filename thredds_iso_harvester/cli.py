#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import argparse
from thredds_iso_harvester.harvest import ThreddsIsoHarvester

def main():
    parser = argparse.ArgumentParser(description='Harvest ISO records from an ncISO enabled THREDDS server.')
    parser.add_argument('--output-dir', '-o', dest='out_dir', required=True, help='ISO output directory')
    parser.add_argument('--select', '-s', dest='select', action='append', help='Data set select pattern (accepts multiple)')
    parser.add_argument('--skip', '-x', dest='skip', action='append', help='Data set skip pattern (accepts multiple)')
    parser.add_argument('--log', '-l', dest='log_file', help='Log file')
    parser.add_argument('--clean', '-c', action='store_true', help='Remove extra files that are not found in catalog')
    parser.add_argument('catalog_url', help='THREDDS catalog URL to parse')
    parser.set_defaults(defaultSkips=True)
    args = parser.parse_args()
    ThreddsIsoHarvester(catalog_url=args.catalog_url, out_dir=args.out_dir, log_file=args.log_file, select=args.select, skip=args.skip, clean=args.clean)
