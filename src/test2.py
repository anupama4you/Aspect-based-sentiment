import spacy
from textblob import TextBlob
nlp = spacy.load("en_core_web_sm")

def sentiment(sentence):
  aspects = []
  doc = nlp(sentence)
  descriptive_term = ''
  target = ''
  for token in doc:
    if token.dep_ == 'nsubj' and token.pos_ == 'NOUN':
      target = token.text
    if token.pos_ == 'ADJ':
      prepend = ''
      for child in token.children:
        if child.pos_ != 'ADV':
          continue
        prepend += child.text + ' '
      descriptive_term = prepend + token.text
      print(prepend)
  aspects.append({'aspect': target,'description': descriptive_term})
  for aspect in aspects:
    aspect['sentiment'] = TextBlob(aspect['description']).sentiment
  print(aspects)