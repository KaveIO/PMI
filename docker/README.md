# Docker

Consistent environments for analysis development and use can be created with docker containers. Containers are created and managed by [Docker](https://www.docker.com/). A container contains a pre-installed environment and runs out-of-the-box.  It is possible to mount your customized code for development inside the container.

The instructions below show how one can use a locally checked-out version of this repository in combination with this Docker image. This combination is a very convenient way of actively working with and/or developing code.

By default, code is executed as `root` user in the container. 

# Required software

Docker installation instructions can be found [here](https://docs.docker.com/install/).

# Getting docker images

All commands below are assumed to be run from this directory (`recommendations/docker`).

## From DockerHub

We have committed the docker image to [DockerHub](https://hub.docker.com/r/kave/exercise-solutions/). To download it, run the command

```bash
$ docker pull kave/exercise-solutions
```

This will download the `kave/exercise-solutions` image locally. Downloading this docker image can take a minute or two.

## Building from scratch
To build the container yourself, you can run the script `build_docker.sh`. This essentially runs the commands

```bash
$ cp -vf ../requirements.txt .
$ docker build -t kave/exercise-solutions .
```

Copying the requirements file ensures that the most recent version of requirements are installed in the container.

# Spinning up a container

For the purposes if this analysis we typically want to run a container with the source code mounted so that it is available from inside the container. To accomplish this, the script `run_docker.sh` has been provided, which should be run from the `docker` directory. It runs the commands

```bash
$ WORKDIR="$(cd ..; pwd)"
$ docker run -p 8888:8888 -h "KPMG-solutions" -it -v $WORKDIR:/opt/recommendations kave/exercise-solutions
```

This ensures that the parent directory (`WORKDIR`) is mounted to `/opt/recommendations` inside the container, and that the port `8888` is forwarded to `8888` on the host machine. This allows for running jupyter notebooks from inside the container. 

# Running jupyter notebooks

The container has been set up with the alias `jupy` for running jupyter notebooks. To start a jupyter notebook server from the analysis directory, run the following commands:

```bash
$ cd /opt/recommendations
$ jupy &
```

To get back into the shell, press enter twice.

Now you can point your browser to [localhost:8888](http://localhost:8888/) to run notebooks. The notebook output will be piped to the file `nohup.out`. If you nonetheless want to see the jupyter output as it appears, you can do so with

```bash
$ tail -f nohup.out
```

In case you get asked for a password, take a look at the tail end of the file ``nohup.out``, where you will see the exact url address (with token) that you need to go to
in your browser.

