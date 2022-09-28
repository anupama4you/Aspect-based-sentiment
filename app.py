import nltk
import stanfordnlp

stanfordnlp.download('en')
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

from src.preprocess import process

process()