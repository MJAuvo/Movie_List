#!/usr/bin/env python3

import os
import pandas as pd
import csv
import json

source_dir = "D:\\[ MOVIE LIST ]"
source_file = "_movies.csv"
target_file = "_movies.json"

# Switch to source directory
print ("\nSwitching to source directory:\t", source_dir)
os.chdir(source_dir)

# Read source data
print("Reading source CSV:\t\t", source_file)
csv_data =  pd.read_csv(source_file, sep=';', encoding='utf-16')

# write target data
print("Writing target JSON:\t\t", target_file)
csv_data.to_json(target_file, orient="records")

print("FINISHED!!\n")