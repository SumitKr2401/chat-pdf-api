import os
from fastapi import APIRouter, UploadFile, File, HTTPException
from shared.factory import pdf_parser, vector_store, conversation_chain

router = APIRouter()


@router.post("/generate")
async def generate_response(question: str):
    if conversation_chain.llm_chain is None:
        # Try to load default vectorstore
        vectorstore = vector_store.load()

        if vectorstore is None:
            # No vectorstore found, raise error
            raise HTTPException(status_code=400, detail="Please upload a PDF first")

        # Setup conversation chain
        conversation_chain.setup(vectorstore)

    question = question.strip()
    response, cost = conversation_chain.generate_response(question)

    return {"response": response, "cost": cost}


@router.post("/reset")
def reset_chat():
    conversation_chain.reset_chat()
    return {"msg": "Chat has been reset"}
