from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_groq import ChatGroq
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.prompts import PromptTemplate

from settings import config_data, working_dir
from prompts import DEFAULT_SYSTEM_PROMPT, DEFAULT_NEGATIVE_PROMPT


def setup_vectorstore():
    """Initialize and return the Chroma vectorstore from the persisted directory."""
    persist_directory = f"{working_dir}/vector_db_dir"
    embeddings = HuggingFaceEmbeddings()
    vectorstore = Chroma(
        persist_directory=persist_directory,
        embedding_function=embeddings
    )
    return vectorstore


def chat_chain(vectorstore, system_prompt=DEFAULT_SYSTEM_PROMPT, negative_prompt=DEFAULT_NEGATIVE_PROMPT):
    """Build and return a ConversationalRetrievalChain using the given vectorstore and prompts."""
    llm = ChatGroq(
        groq_api_key=config_data["GROQ_API_KEY"],
        model_name="llama-3.1-8b-instant"
    )

    # Create a combined prompt template
    prompt_template = f"""{system_prompt}

{negative_prompt}

Context (from mental health database):
{{context}}

Chat History:
{{chat_history}}

Question: {{question}}

Answer:"""

    prompt = PromptTemplate(
        template=prompt_template,
        input_variables=["context", "chat_history", "question"]
    )

    retriever = vectorstore.as_retriever(
        search_kwargs={"k": 3}  # Retrieve top 3 most relevant documents
    )

    memory = ConversationBufferMemory(
        llm=llm,
        output_key="answer",
        memory_key="chat_history",
        return_messages=True
    )

    chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        memory=memory,
        verbose=True,
        return_source_documents=True,
        combine_docs_chain_kwargs={"prompt": prompt}
    )
    return chain
