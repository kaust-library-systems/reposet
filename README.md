# Repository to Dataset

Creating dataset from the files in the repository in similar way to [cord19 project](https://github.com/allenai/cord19). As with `cord19`, the starting point is a metadata file with one line per item in the repository. 


Directory structure of files downloaded from the repository

```
(venv) mgarcia@mordor:~/Work/reposet/data/in$ tree 10754_209405/
10754_209405/
├── 10754_209405.json
├── 10754_209405.xml
├── 218531-377184.json
├── 218531-377185.json
├── 218531-377185.pdf
├── 218531-377186.json
├── 218531-377186.pdf
├── data
│   ├── 218531-377184.metadata
│   └── 218531-377184.pdf
├── manifest-sha256.txt
└── tagmanifest-sha256.txt
```

## Installation

Clone the repository with `clone` command with GitHub desktop. Next install the requirements:

```
(venv) PS C:\Users\garcm0b\Work\reposet> pip install -r .\requirements.txt
```
