from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

from rag import setup_vectorstore, chat_chain
from utils import contains_sensitive_topics

# FastAPI app instance
app = FastAPI()


class MessageRequest(BaseModel):
    message: str


@app.post("/chat")
async def chatbot(request: MessageRequest):
    """FastAPI endpoint: accepts a message and returns the chatbot's response."""
    message = request.message

    # Setup vectorstore and conversational chain
    vectorstore = setup_vectorstore()
    conversational_chain = chat_chain(vectorstore)

    # Check for sensitive topics
    if contains_sensitive_topics(message):
        response = "It seems you may be asking questions outside my context, please ask questions related to College Name only."
    else:
        response = conversational_chain({"question": message})["answer"]

    return {"response": response}


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
