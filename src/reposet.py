# Write a CSV file with metadata of the repository items.
# 

import click as CL
import rplib as RP
import logging as LOG
import csv
@CL.command()
@CL.argument('input', type=CL.File('r'))
def main(input):

    LOG.basicConfig(encoding='utf-8', level=LOG.INFO)

    root_dir = RP.read_config(input.name)
    if not root_dir:
        LOG.critical(f"The path for input files is empty")
        raise Exception("Error getting the directory to read input files from")
    else:
        LOG.info(f"Root directory for data '{root_dir}'")

    json_file_list = RP.get_json(root_dir)

    # For each JSON file, return a row (dictionary) with all the metadata of
    # the repository entity, like thesis, dissertations, etc.
    rows_csv = []
    for jj in json_file_list:
        rows_csv.append(RP.get_metadata(jj))

    with open('metadata.csv', 'w', newline='') as csvfile:
        field_names = rows_csv[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(rows_csv)

if __name__ == "__main__":
    main()