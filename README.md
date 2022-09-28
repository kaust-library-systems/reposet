# Repository to Dataset

Creating dataset from the files in the repository.

## Starting GROBID 

Starting the GROBID container

```
a-garcm0b@library-elk:~/Work$ docker run -d -t --rm --name grobid_docker -p 8070:8070 lfoppiano/grobid:0.7.1
f3e49017f985d93bf9a87546434e6a2c0f7d6c6dccac2c866f6355c5c00bb127
a-garcm0b@library-elk:~/Work$
a-garcm0b@library-elk:~/Work$ docker ps
CONTAINER ID   IMAGE                    COMMAND                  CREATED         STATUS         PORTS                                       NAMES
f3e49017f985   lfoppiano/grobid:0.7.1   "/tini -s -- ./grobi[38;5;81m~@"   8 seconds ago   Up 7 seconds   0.0.0.0:8070->8070/tcp, :::8070->8070/tcp   gocker
a-garcm0b@library-elk:~/Work$
```

## Cleaning Input File

Extracting the URL from the file. From 

```
(...)
"PDF_URL": "https://repository.kaust.edu.sa/bitstream/10754/133211/1/FarhanAbdulGhaffarThesis.pdf"
"PDF_URL": "https://repository.kaust.edu.sa/bitstream/10754/133969/1/Gamal%20Amin%20Thesis-final2.pdf"
(...)
```

To just the URL

```
a-garcm0b@library-elk:~/Work$ grep 'PDF_URL' listOfETDs.json | head | cut -d ':' -f 2-
"https://repository.kaust.edu.sa/bitstream/10754/133211/1/FarhanAbdulGhaffarThesis.pdf"
"https://repository.kaust.edu.sa/bitstream/10754/133969/1/Gamal%20Amin%20Thesis-final2.pdf"
(...)
```

Next we remove the double quotes from the URL

```
a-garcm0b@library-elk:~/Work$ sed -i 's/"//g' listOfArticles.txt
a-garcm0b@library-elk:~/Work$ head listOfArticles.txt
https://repository.kaust.edu.sa/bitstream/10754/205812/1/Abdulaziz%20Barastheses.pdf
(...)
```

Finally we download the articles (no thesis or dissertations)

```
a-garcm0b@library-elk:~/Work$ FILES=`cat listOfArticles.txt `

```
a-garcm0b@library-elk:~/repo2text/in$ for ff in $FILES
> do
> wget --quiet $ff
> done
a-garcm0b@library-elk:~/repo2text/in$ ll
total 412M
-rw-r--r-- 1 a-garcm0b g-a-garcm0b 5.8M Sep 14  2021 '2015_12_14_Garret McKerricher_Final.pdf'
-rw-r--r-- 1 a-garcm0b g-a-garcm0b 1.5M Sep 14  2021 'A Regularized Stationary Mean-Field Game.pdf'
(...)
```