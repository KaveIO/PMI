This is the repository for the PMI proposal task Mentor-Mentee Recommendations.

The `python` subdirectory has a subdirectory `pmi`. We can treat this as a package and install it using:

```bash
pip install -e /path/to/recommendations/python/pmi
```

Then the contents of that directory will be available to any notebooks, scripts, etc. that you are writing. 


# Installation

You can run the notebooks in this repository either by running a docker image, or by creating a local environment with conda. We have tested this analysis on a machine with 8 cores and 32GB of RAM.


## Docker

This repository has an associated docker image for out-of-the-box environment compatibility. To install and run it, please see the instructions at `docker/README.md`.

## Local environment

To build a local environment, please ensure that you have Anaconda (`conda>=4.4.10`) with Python 2.7 installed. To ensure your `conda` installation can access all requirements, please add the `conda-forge` channel to your `conda` configuration using the command

```bash
conda config --append channels conda-forge
```

Then create a new environment for the project, installing the requirements, using

```bash
conda env create -n kpmg -f requirements.txt anaconda
```

Finally, activate your environment using

```bash
conda activate kpmg
```

All required packages should now be available. 


# Required datasets

To download all relevant datasets needed for the exercise solution, please follow the instructions at `data/README.md`.


# Analysis notebooks

The analysis notebooks are described in more detail in `notebooks/README.md`.

