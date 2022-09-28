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


