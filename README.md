# Repository to Dataset

Creating dataset from the files in the repository in similar way to [cord19 project](https://github.com/allenai/cord19). As with `cord19`, the starting point is a metadata file with one line per item in the repository. The content of the metadata file is:

* repository id
* advisor
* author
* title
* DOI
* `uri`
* abstract
* language
* type
* department
* grantor

The pseudo code for script is

```
ROOT_DIR: root directory to data, like `/repo`
DIR_IN: directory where repository will dump the file, like `/repo/in`
CSV_FILE: file with the CSV for the items from the repository: `${ROOT_DIR}/metadata.csv`

for each dir in $DIR_IN:
    read file JSON named ${DIR_IN}/${dir_name}/${dir_name}.json
    read fields to csv_line
    append to csv_line to $CSV_FILE

```

