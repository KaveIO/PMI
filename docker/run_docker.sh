WORKDIR="$(cd ..; pwd)"
docker run -p 8888:8888 -h "KPMG-solutions" -it -v $WORKDIR:/opt/recommendations kave/exercise-solutions
