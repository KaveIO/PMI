echo "Getting requirements from root dir..."
cp -vf ../requirements.txt .
docker build -t kave/exercise-solutions .
