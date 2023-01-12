# Functions for the reposet project

import configparser as CP
import logging as LOG
import pathlib as PL
import json as JSON


def clean_json(json_file: str) -> dict:
    """Clean the JSON file by removing the external quotes.
    Returns json data or an empty dict in case unable to clean."""

    LOG.info(f"Trying to clean JSON file '{json_file}'")
    try:
        with open(json_file) as fin:
            in_text = fin.readlines()
        #
        text = str(in_text[0])
        len_text = len(text)
        data = JSON.loads(text[1 : len_text - 1])
    except ValueError as ee:
        LOG.warning(f"Unable to clean JSON file '{json_file}'")
        data = {}
    finally:
        return data


def read_json_file(json_file: str) -> dict:
    """Read the JSON file.
    Returns the JSON data or an empty dict in case of error."""

    # Try to read the json
    LOG.info(f"Reading JSON file '{json_file}'")
    try:
        with open(json_file, "r", encoding="utf-8") as fin:
            data = JSON.load(fin)
    except ValueError as ee:
        LOG.error(f"Error {ee} while reading JSON file '{json_file}'.")
        data = clean_json(json_file)
    finally:
        return data


def get_metadata(json_file: str) -> dict:
    """Return a dictionary with article metadata from the json file"""
    """Return a dictionary with article metadata from the json file"""

    data = read_json_file(json_file)

    if not data:
        return {}
    else:
        entity_metadata = data["metadata"]
        row_csv = dict(
            (ee["key"].split(".")[-1], ee["value"]) for ee in entity_metadata
        )
        entity_metadata = data["metadata"]
        row_csv = dict(
            (ee["key"].split(".")[-1], ee["value"]) for ee in entity_metadata
        )
        return row_csv


def get_json(root_dir: str) -> list:
    """Return  a list with the path to the JSON files"""
    """Return  a list with the path to the JSON files"""

    files_path = PL.Path(root_dir)
    json_list = []

    for ff in files_path.iterdir():
        json_file = f"{ff.stem}.json"
        json_path = ff.joinpath(json_file)
        if json_path.exists():
            json_list.append(json_path)
        else:
            LOG.warn(f"JSON file '{json_path}' not found.")
            # Adding a 'next' in case we add more statements below, and
            # forget that we should go to the next directory in the list.
            next

    return json_list


def read_config(config_file: str) -> str:
    """Read config file, and return diretory to read."""
    """Read config file, and return diretory to read."""

    try:
        config = CP.ConfigParser(interpolation=CP.ExtendedInterpolation())
        # config._interpolation = CP.ExtendedInterpolation()
        config.read(config_file)
        files_dir = config["REPO"]["IN_DIR"]
        files_dir = config["REPO"]["IN_DIR"]
    except CP.Error as ee:
        LOG.critical(f"Error reading config file '{config_file}'")
        files_dir = ""

    return files_dir
