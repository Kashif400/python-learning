from google.cloud import language_v1

def summarize_text_with_google_nlp(text):
    client = language_v1.LanguageServiceClient()

    document = language_v1.Document(
        content=text,
        type_=language_v1.Document.Type.PLAIN_TEXT
    )

    response = client.annotate_text(
        document=document,
        features={'extract_syntax': False, 'extract_entities': False, 'extract_document_sentiment': False,
                  'extract_entity_sentiment': False, 'classify_text': False, 'summarize_text': True}
    )

    summary = response.document_sentiment

    return f"Text Summary: {summary.text.content}"

# Example usage
input_text = """
Text summarization is an essential task in Natural Language Processing (NLP) that allows us to distill lengthy articles or documents into concise, easy-to-understand summaries. In this tutorial, we’ll explore how to harness the power of GoogleBard, a cutting-edge language model developed by Google, to perform text summarization effortlessly.
"""

result = summarize_text_with_google_nlp(input_text)
print(result)
