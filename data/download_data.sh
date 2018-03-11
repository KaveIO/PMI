#!/bin/bash

echo "Now downloading required datasets for DBLP exercise solution, 10 files in total."
echo "This may take several minutes ..."

echo ""
echo "Now downloading the original DBLP datasets."
echo ""

wget -c https://dblp.uni-trier.de/xml/dblp.xml.gz
wget -c https://dblp.uni-trier.de/xml/dblp.dtd

echo ""
echo "Now downloading the processed DBLP datasets and external datasets."
echo ""

# --- all derived datasets
wget -c https://s3-eu-west-1.amazonaws.com/kct.bigdata/projects/exercise-solutions/dblp/Data.7z
7zr x Data.7z 

# --- page rank and citations
wget -c https://s3-eu-west-1.amazonaws.com/kct.bigdata/projects/exercise-solutions/dblp/dblp.v10.zip
unzip dblp.v10.zip

# --- word2vec models
mkdir word2vec_models
wget -c https://s3-eu-west-1.amazonaws.com/kct.bigdata/projects/exercise-solutions/dblp/word2vec_models/model_1520420116 -P word2vec_models/
wget -c https://s3-eu-west-1.amazonaws.com/kct.bigdata/projects/exercise-solutions/dblp/word2vec_models/model_1520420191 -P word2vec_models/
wget -c https://s3-eu-west-1.amazonaws.com/kct.bigdata/projects/exercise-solutions/dblp/word2vec_models/model_abstract_1520532394 -P word2vec_models/

# --- custom mentor-mentee preferences files for demonstration
wget -c https://s3-eu-west-1.amazonaws.com/kct.bigdata/projects/exercise-solutions/dblp/custom_mentees_preferencies.xlsx
wget -c https://s3-eu-west-1.amazonaws.com/kct.bigdata/projects/exercise-solutions/dblp/custom_mentees_topic_preferencies.xlsx
wget -c https://s3-eu-west-1.amazonaws.com/kct.bigdata/projects/exercise-solutions/dblp/mentee_mentors_match.csv

