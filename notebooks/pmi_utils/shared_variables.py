import nltk

nltk.download('stopwords')

from nltk.corpus import stopwords
import numpy as np

np.random.seed(seed=0)

iteration_page_rank = 10

path = "../data/pmi_data/"

f_json_dblp = path + 'dblp.json'
f_sample_dblp = path + 'dblp_sample.json'
f_dblp_for_clustering = path + 'dblp_for_clustering.json'
f_paper_clusters = path + 'paper_clusters.csv'
f_json_by_author = path + 'dblp_for_each_author.csv'
f_author_role = path + 'author_role.csv'
f_author_ranks = path + 'author_ranks.csv'
f_cluster_id_name = path + 'cluster_id_name.csv'
f_dblp_by_author = path + 'paper_by_author.pickle'
f_dblp_ref = 'dblp-ref/dblp-ref-%d.json'
f_paper_ranks = path + 'paper_ranks.csv'
f_mentor_ranks = path + 'mentor_ranks.csv'
f_mentee_prefs_dblp_data = path + 'mentee_prefs_dblp_data.csv'
f_mentee_topic_prefs_dblp_data = path + 'mentee_topic_prefs_dblp_data.csv'
f_mentee_prefs_excel = path + 'mentee_prefs_excel.xlsx'

mentee_prefs_page = 'General Preferences'
mentee_topic_prefs_page = 'Topic Preferences'

lbl_paper_id = 'paper_id'
lbl_papertype = 'papertype'
lbl_title = 'title'
lbl_authors = 'authors'
lbl_journal = 'journal'
lbl_booktitle = 'booktitle'
lbl_year = 'year'
lbl_ee = 'ee'
lbl_url = 'url'
columns = [
    lbl_paper_id,
    lbl_papertype,
    lbl_title,
    lbl_authors,
    lbl_journal,
    lbl_booktitle,
    lbl_year,
    lbl_ee,
    lbl_url
]

lbl_author = 'author'
lbl_cluster = 'cluster'
lbl_id = 'id'
lbl_references = 'references'
lbl_rank = 'cite_rank'
lbl_role = 'role'
lbl_num_pubs = 'num_pubs'
lbl_pub_rate = 'pub_rate'
lbl_years_exp = 'years_exp'
lbl_rank = 'cite_rank'

lbl_mentor = 'mentor'
lbl_mentee = 'mentee'

# Variables for capturing mentees' preferences
lbl_cluster_pref = 'cluster_pref'
lbl_num_pubs_pref = lbl_num_pubs + '_pref'
lbl_pub_rate_pref = lbl_pub_rate + '_pref'
lbl_years_exp_pref = lbl_years_exp + '_pref'
lbl_rank_pref = lbl_rank + '_pref'

lbl_cluster_mentor_weight = 'cluster_mentor_weight'

lbl_sink = 'sink'

# Directories for saving trained models
dir_word2vec_models = path + 'word2vec_models/'
dir_clustering_models = path + 'clustering_models/'
# kmeans model filename
f_kmeans = dir_clustering_models + 'kmeans.pickle'

# Variables for text processing
english_stop_words = ["a", "about", "above", "above", "across", "after", "afterwards", "again", "against", "all", "almost", "alone", "along", "already", "also","although","always","am","among", "amongst", "amoungst", "amount",  "an", "and", "another", "any","anyhow","anyone","anything","anyway", "anywhere", "are", "around", "as",  "at", "back","be","became", "because","become","becomes", "becoming", "been", "before", "beforehand", "behind", "being", "below", "beside", "besides", "between", "beyond", "bill", "both", "bottom","but", "by", "call", "can", "cannot", "cant", "co", "con", "could", "couldnt", "cry", "de", "describe", "detail", "do", "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven","else", "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fifteen", "fify", "fill", "find", "fire", "first", "five", "for", "former", "formerly", "forty", "found", "four", "from", "front", "full", "further", "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", "however", "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own","part", "per", "perhaps", "please", "put", "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should", "show", "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", "system", "take", "ten", "than", "that", "the", "their", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they", "thickv", "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us", "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "with", "within", "without", "would", "yet", "you", "your", "yours", "yourself", "yourselves", "the",'like', 'think', 'know', 'want', 'sure', 'thing', 'send', 'sent', 'speech', 'print', 'time','want', 'said', 'maybe', 'today', 'tomorrow', 'thank', 'thanks']
stopw = stopwords.words("english")+english_stop_words

# Used for visualization purposes
f_img_elbow_plot = path + 'img/elbow_plot.PNG'
