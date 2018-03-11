# --- base image: anaconda (python2.7)
FROM continuumio/anaconda:5.1.0

# --- link sh to bash
SHELL ["/bin/bash", "-c"]

# --- add conda-forge as lowest priority channel in conda
RUN conda config --append channels conda-forge

# --- install requirements
COPY requirements.txt /tmp/
RUN conda install --yes --file /tmp/requirements.txt && rm /tmp/requirements.txt

# --- unpacking tool: 7za
RUN apt-get install -y --no-install-recommends p7zip

# --- append sourcing of Kave env to bashrc
COPY bashrc_addendum /tmp/
RUN cat /tmp/bashrc_addendum >> "${HOME}"/.bashrc && rm /tmp/bashrc_addendum
