import os
import uuid
import logging
from .modules.pdf_parser import PDFParser
from .modules.vector_store import VectorStore
from .modules.conversation_chain import ConversationChain

WORKER_ID = str(uuid.uuid4().hex)
logger = logging.getLogger(__name__)

pdf_parser = PDFParser()

vector_store = VectorStore()

conversation_chain = ConversationChain()
