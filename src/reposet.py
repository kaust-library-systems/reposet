# Write a CSV file with metadata of the repository items.
# 

import click as CL
import rplib as RP
import logging as LOG

@CL.command()
@CL.argument('input', type=CL.File('r'))
def main(input):

    LOG.basicConfig(encoding='utf-8', level=LOG.INFO)

    files_dir = RP.read_config(input.name)
    if not files_dir:
        LOG.critical(f"The path of input files is empty")
        raise Exception("Error getting the directory to read input files")

    LOG.info(f"Input files in '{files_dir}'")

if __name__ == "__main__":
    main()