# RAG (Retrieval Augmented Generation) Basics

def search_documents(query, documents):
    """Simple document search"""
    results = []
    for doc in documents:
        if query.lower() in doc.lower():
            results.append(doc)
    return results

def generate_response(query, context):
    """Simulate LLM response"""
    return f"Based on context: '{context}', answer for '{query}'"

# Sample documents
docs = [
    "RAG combines retrieval and generation",
    "Vector databases store embeddings",
    "LangChain is a popular RAG framework"
]

query = "What is RAG?"
context = search_documents(query, docs)
response = generate_response(query, context)
print(response)
