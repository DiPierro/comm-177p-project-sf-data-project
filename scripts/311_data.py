# Shaves down the 311 data to noise reports only

import csv
import os

data_dir = os.environ['DATA_DIR']   # path to data/
rawdata_dir = data_dir + '/raw/'
processeddata_dir = data_dir + '/processed/'

infile_with_path = os.path.join(rawdata_dir, '311_Cases.csv')
outfile_with_path = os.path.join(rawdata_dir, '311_Cases_filtered.csv')

with open(infile_with_path, 'r') as infile, open(outfile_with_path, 'w') as outfile:
  writer = csv.writer(outfile)
  for row in csv.reader(infile):
    if row[0].strip().lower() == 'caseid': # Captures header
      writer.writerow(row)
    if row[7].strip().lower() == 'noise report': # Filters to noise reports only
      req_type = row[8].strip().lower() 
      # Within noise reports, selects only noise & entertainment
      if req_type.find('entertainment') != -1  or  req_type.find('noise') != -1:
        writer.writerow(row)