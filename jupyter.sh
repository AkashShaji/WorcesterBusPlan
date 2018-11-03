#!/bin/sh

docker run --rm -d --name woobusplan -p 8900:8888 -v `pwd`:/home/jovyan:Z jupyter/datascience-notebook
