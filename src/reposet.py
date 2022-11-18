# Write a CSV file with metadata of the repository items.
# 

import click as CL
import rplib as RP
import logging as LOG

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

    for jj in json_file_list:
        RP.get_metadata(jj)

if __name__ == "__main__":
    main()