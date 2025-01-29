from langchain.document_loaders import UnstructuredURLLoader


# import nltk
# nltk.download('averaged_perceptron_tagger_eng')
# nltk.download('punkt_tab')


urls = [
    "https://www.moneycontrol.com/news/business/india-committed-to-buy-economically-priced-energy-oil-minister-hardeep-singh-puri-12919144.html"

]


loader = UnstructuredURLLoader(urls=urls)

# Load and fetch the data
documents = loader.load()

# Print the fetched documents
for doc in documents:
    print(f"Content: {doc.page_content}")
    print(f"Metadata: {doc.metadata}")
