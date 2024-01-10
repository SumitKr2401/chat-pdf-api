import os
from fastapi import APIRouter, UploadFile, File
from shared.factory import pdf_parser, vector_store, conversation_chain

router = APIRouter()


@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    # create chunks from pdf
    chunks = pdf_parser.parse(file.file)

    # store chunks in a vector store
    vector_store.save(vector_store.new(chunks))
    conversation_chain.setup(vector_store.load())

    # directly setup the conversation chain in memory
    # conversation_chain.setup(vector_store.new(chunks))

    return {"msg": f"successfully uploaded {file.filename}"}
