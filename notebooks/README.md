# Notebooks description

This folder contains four notebooks that explain and implement the mentor-mentee recommendation algorithm on the DBLP dataset.
The notebooks need to be read in the following order in order to analyze the whole analytical flow.
For each notebook you can find below: a brief description, input file requirements and output files.
Objects have been serialized to files so that it is not necessary to process everything, only to run a specific part of the code.

Python scripts used within the notebooks can be found in the folder "pmi_utils/".
This contains a list of variables shared throughout the several notebooks and scripts for unzipping files and extracting information from the DBLP XML file.

## Notebooks used to run the algorithm:
1. Topics Inference by Clustering
	- *Description*: The goal of this notebook is to infer a list of main topics from the dblp.xml.gz dataset. At the end of the notebook we have that every paper is assigned to a topic.
	- *Input*: dblp.xml.gz
	- *Output*: paper_clusters.csv

2. Authors' KPIs
	- *Description*: In this notebook, we calculate the author's level of expertise for each topic. Topics are assigned to authors by matching with the topics of their published papers.
	- *Input*: dblp.json, dblp_sample.json, dblp_for_each_author.csv, paper_clusters.csv, dblp-ref/dblp-ref-(0, 1, 2, 3).json
	- *Output*: author_ranks.csv, paper_by_author.pickle
	
3. Mentor-Mentee data split
	- *Description*: In this notebook we define a rule for splitting the authors between mentors and mentees. In particular, we will categorize mentees by young researchers while mentors as the experienced ones.
	- *Input*: dblp_for_each_author.csv, dblp_v2.json, paper_by_author.csv
	- *Output*: mentor_ranks.csv, mentee_prefs_dblp_data.csv, mentee_topic_prefs_dblp_data.csv

4. Recommender
	- *Description*: This notebook has the objective of finding the mentor that best responds to mentee's preferences. The notebook is capable of capturing mentee's preferences over both topics and mentor's skills. It's possible to run the algorithm in the notebook with your own mentee preference profile by editing the provided Excel file "mentee_prefs_excel.xlsx".
	- *Input*: mentor_ranks.csv, mentee_prefs_dblp_data.csv, mentee_topic_prefs_dblp_data.csv, mentee_prefs_excel.xlsx
	- *Output*: mentees_mentors.csv
	

## Side notebooks:
Side_1 Word2Vec on Abstracts:
This notebook is used to fit a richer word2vec model using the external data source Citation Network (https://aminer.org/citation).
	
Side_2 Measuring Performance:
This notebook is used to measure the performance of the topics inference and the mentor assignment.