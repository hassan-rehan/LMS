# Importing necessary libraries
import pandas as pd
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re, os

def _removeNonAscii(s):
    return "".join(i for i in s if  ord(i)<128)

# Function for converting into lower case
def make_lower_case(text):
    return text.lower()

# Function for removing stop words
def remove_stop_words(text):
    text = text.split()
    stops = set(stopwords.words("english"))
    text = [w for w in text if not w in stops]
    text = " ".join(text)
    return text

# Function for removing punctuation
def remove_punctuation(text):
    tokenizer = RegexpTokenizer(r'\w+')
    text = tokenizer.tokenize(text)
    text = " ".join(text)
    return text

# Function for removing the html tags
def remove_html(text):
    html_pattern = re.compile('<.*?>')
    return html_pattern.sub(r'', text)

def clean_description(desc):
    desc = _removeNonAscii(desc)
    desc = make_lower_case(desc)
    desc = remove_stop_words(desc)
    desc = remove_punctuation(desc)
    desc = remove_html(desc)
    return desc

# Function for recommending books based on Book description.
def desc_recommend(bid, category_id):
    current_path = os.path.dirname(__file__)
    store = pd.HDFStore(os.path.join(current_path,'data.h5'))
    dataframe = store.get('model_data')
    # Matching the category_id with the dataset and reset the index
    data = dataframe.loc[dataframe['category_id'] == category_id]  
    data.reset_index(level = 0, inplace = True)
    # Convert the index into series
    indices = pd.Series(data.index, index = data['id'])
    
    #Converting the book description into vectors and used bigram
    tf = TfidfVectorizer(analyzer='word', ngram_range=(2, 2), min_df = 1, stop_words='english')
    tfidf_matrix = tf.fit_transform(data['cleaned_desc'])
    
    # Calculating the similarity measures based on Cosine Similarity
    sg = cosine_similarity(tfidf_matrix, tfidf_matrix)
    # Get the index corresponding to original id  
    idx = indices[bid]
    # Get the pairwsie similarity scores 
    sig = list(enumerate(sg[idx]))
    # Sort the books
    sig = sorted(sig, key=lambda x: x[1], reverse=True)
    
    # Scores of the 1 to 10 most similar books
    if len(data) > 10:
        sig = sig[0:11]
    else:
        sig = sig[0:len(data)]
    
    # Book indicies
    book_indices = [i[0] for i in sig]
   
    # Top books recommendation
    rec = data[['id']].iloc[book_indices]
    
    # It reads the top 1 to 40 recommend book url and print the images
    return rec.id.tolist()

def title_recommend(bid, category_id):
    current_path = os.path.dirname(__file__)
    store = pd.HDFStore(os.path.join(current_path,'data.h5'))
    dataframe = store.get('model_data')
    # Matching the category_id with the dataset and reset the index
    data = dataframe.loc[dataframe['category_id'] == category_id]  
    data.reset_index(level = 0, inplace = True) 
     # Convert the index into series
    indices = pd.Series(data.index, index = data['id'])

    #Converting the book title into vectors and used bigram
    tf = TfidfVectorizer(analyzer='word', ngram_range=(2, 2), min_df = 1, stop_words='english')
    tfidf_matrix = tf.fit_transform(data['title'])

    # Calculating the similarity measures based on Cosine Similarity
    sg = cosine_similarity(tfidf_matrix, tfidf_matrix)
    # Get the index corresponding to original id
    idx = indices[bid]
    # Get the pairwsie similarity scores by giving ID
    sig = list(enumerate(sg[idx]))
    
    # Sort the books
    sig = sorted(sig, key=lambda x: x[1], reverse=True)
    
    # Scores of the 1 to 10 most similar books
    if len(data) > 10:
        sig = sig[0:11]
    else:
        sig = sig[0:len(data)]
    
    # Book indicies
    book_indices = [i[0] for i in sig]

    # Top books recommendation
    rec = data[['id']].iloc[book_indices]
        
    # It reads the top 1 to 40 recommended book urls and print the images
    return rec.id.tolist()

def add_data(id,title,desc,cid):
    current_path = os.path.dirname(__file__)
    store = pd.HDFStore(os.path.join(current_path,'data.h5'))
    dataframe = pd.DataFrame({'id': id,'title': title,'cleaned_desc':clean_description(desc),'category_id': cid}, index=[store.get('model_data').index[-1]+1])
    store.append('model_data', dataframe, format='table',  data_columns=True)

def delete_data(id):
    current_path = os.path.dirname(__file__)
    store = pd.HDFStore(os.path.join(current_path,'data.h5'))
    a = store.get('model_data')
    store.remove('model_data', where="index in %s" % list(a[a['id'] == id].index))