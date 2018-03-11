#!/bin/bash

echo "Now downloading required datasets for DBLP exercise solution."
echo "This may take several minutes ..."

echo ""
echo "Now downloading the original DBLP datasets."
echo ""

wget -c https://dblp.uni-trier.de/xml/dblp.xml.gz
wget -c https://dblp.uni-trier.de/xml/dblp.dtd

echo ""
echo "Now downloading the processed DBLP datasets and external datasets."
echo ""

wget -c https://s3-eu-west-1.amazonaws.com/kct.bigdata/projects/exercise-solutions/dblp/pmi_data.zip
unzip pmi_data.zip
