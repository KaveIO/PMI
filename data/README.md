# Required datasets for DBLP exercise solution

To download and unpack the required datasets for the DBLP exercise solution, from the `data` directory run the command:

```bash
$ download_data.sh
```

This will download the original input files and 1 big zip file datasets from Amazon S3 and unpack it where needed (i.e. within the root of your notebooks). Please note that this download may take several minutes.

After extraction of *pmi_data.zip*, if not done automatically, please place the extracted files into a folder called *pmi_data* at the root of the notebooks.

## Description of the Datasets
- *dblp.xml.gz*: the original dblp dataset in XML format
- *dblp.dtd*: the DTD of the orginal dblp dataset

Inside the *pmi_data.zip* file you can find the following files:
1. Folder *clustering_models*: containing the last trained k-means model serialized with pickle
2. Folder *dblp-rf*: containing the Citation Network dataset, split into three json files
3. Folder *img*: containing any image needed to be imported in the notebooks
4. Folder *word2vec_models*: containing a series of trained models, on both abstracts (files starting with 'abstract_') and on title (files starting with 'model_')
5. *author_ranks.csv*: contains information about the level of expertise for each (author, cluster) pair
6. *author_role.csv*: contains information about whether an author has the role of a mentor or a mentee
7. *cluster_id_name.csv*: contains a mapping between cluster_id and cluster_name
8. *dblp.json*: contains the whole dblp data, preprocessed and converted to json format 
9. *dblp_for_each_author.csv*: contains a many-to-many relation between papers and authors
10. *dblp_sample.json*: contains a sample of 10% of "dblp_v2.json" used for training and testing the models
11. *mentee_mentors_match.csv*: contains the recommendation results based on a simulation over 300 mentees and 10% of dblp dataset
12. *mentee_prefs_dblp_data.csv*: contains general preferences of mentees inferred from dblp data
13. *mentee_prefs_excel.xlsx*: Excel file that can be modified to define new mentees and used as input for the recommendation algorithm
14. *mentee_topic_prefs_dblp_data.csv*: contains preferences over topics by mentees inferred from dblp data
15. *mentor_ranks.csv*: contains 4 kpi scores for each mentor inferred from dblp publications data
16. *paper_by_author.pickle*: used for convenience, contains the join between *dblp.json* and *dblp_for_each_author.csv*
17. *paper_clusters.csv*: contains the result of clustering papers into topics
18. *paper_ranks.csv*: contains citation ranks for each paper
