FROM jupyter/datascience-notebook

RUN pip install nbdime

CMD jupyter notebook "$@" --allow-root
