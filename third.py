import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.probability import FreqDist
from heapq import nlargest

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

def summarize_article(article_text, num_sentences=1):
    # Tokenize the text into sentences
    sentences = sent_tokenize(article_text)

    # Tokenize and remove stopwords for each sentence
    words = [word for word in word_tokenize(article_text.lower()) if word.isalpha() and word not in stopwords.words('english')]

    # Calculate word frequencies
    word_freq = FreqDist(words)

    # Calculate sentence scores based on word frequencies
    sentence_scores = {}
    for sentence in sentences:
        for word, freq in word_freq.items():
            if word in sentence.lower():
                if sentence in sentence_scores:
                    sentence_scores[sentence] += freq
                else:
                    sentence_scores[sentence] = freq

    # Get the top 'num_sentences' sentences with highest scores
    summary_sentences = nlargest(num_sentences, sentence_scores, key=sentence_scores.get)

    # Join the summary sentences to get the final summary
    summary = ' '.join(summary_sentences)
    return summary

# Example usage
article_text = """
The titular threat of The Blob has always struck me as the ultimate movie
monster: an insatiably hungry, amoeba-like mass able to penetrate
virtually any safeguard, capable of--as a doomed doctor chillingly
describes it--"assimilating flesh on contact.
Snide comparisons to gelatin be damned, it's a concept with the most
devastating of potential consequences, not unlike the grey goo scenario
proposed by technological theorists fearful of
artificial intelligence run rampant
"""

summary = summarize_article(article_text)
print("Original Article:\n", article_text)
print("\nSummary:\n", summary)
