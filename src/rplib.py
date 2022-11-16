# Functions for the reposet project

import configparser as CP
import logging as LOG

def read_config(config_file: str) -> str:
    ''' Read config file, and return diretory to read. '''

    try:
        config = CP.ConfigParser()
        config._interpolation = CP.ExtendedInterpolation()
        config.read(config_file)
        files_dir = config['REPO']['IN_DIR']
    except CP.Error as ee:
        LOG.critical(f"Error reading config file '{config_file}'")
        files_dir = ""
    
    return files_dir