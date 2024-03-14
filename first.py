from textblob import TextBlob

def simplify_sentence(sentence):
    blob = TextBlob(sentence)
    simplified_sentence = " ".join([word.lemmatize() for word in blob.words])
    return simplified_sentence

def simplify_text(text):
    blob = TextBlob(text)
    simplified_text = " ".join([simplify_sentence(str(sentence)) for sentence in blob.sentences])
    return simplified_text

text = '''
The titular threat of The Blob has always struck me as the ultimate movie
monster: an insatiably hungry, amoeba-like mass able to penetrate
virtually any safeguard, capable of--as a doomed doctor chillingly
describes it--"assimilating flesh on contact.
Snide comparisons to gelatin be damned, it's a concept with the most
devastating of potential consequences, not unlike the grey goo scenario
proposed by technological theorists fearful of
artificial intelligence run rampant.
'''

# Simplify the text
simplified_text = simplify_text(text)

# Print the original and simplified texts
print(f"Original Text:\n{text}\n")
print(f"Simplified Text:\n{simplified_text}\n")
