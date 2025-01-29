from langchain.document_loaders import TextLoader,UnstructuredURLLoader

loader = UnstructuredURLLoader(urls=["https://www.moneycontrol.com/news/business/india-committed-to-buy-economically-priced-energy-oil-minister-hardeep-singh-puri-12919144.html"])

data = loader.load()


print(data)

# Path to your text file
# file_path = "nvda_news_1.txt"

# # Initialize the TextLoader
# loader = TextLoader(file_path)

# # Load the document
# documents = loader.load()

# # Print the documents
# for doc in documents:
#     print(f"Document Content: {doc.page_content}")
#     print(f"Metadata: {doc.metadata}")