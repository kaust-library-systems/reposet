# Write a CSV file with metadata of the repository items.
# 

import click as CL
import rplib as RP
import logging as LOG
import pathlib as PL

@CL.command()
@CL.argument('input', type=CL.File('r'))
def main(input):

    LOG.basicConfig(encoding='utf-8', level=LOG.INFO)

    files_dir = RP.read_config(input.name)
    if not files_dir:
        LOG.critical(f"The path for input files is empty")
        raise Exception("Error getting the directory to read input files from")

    LOG.info(f"Input files in '{files_dir}'")
    
    files_path = PL.Path(files_dir)

    for ff in files_path.iterdir():
        json_file = f"{ff.stem}.json"
        json_path = ff.joinpath(json_file)
        if json_path.exists:
            LOG.info(f"Reading JSON file '{json_path}'")
            
        else:
            LOG.warn(f"JSON file '{json_path}' not found.")
            # Adding a 'next' in case we add more statements below, and
            # forget that we should go to the next directory in the list.
            next

if __name__ == "__main__":
    main()