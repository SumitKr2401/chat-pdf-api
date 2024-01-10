import os
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.callbacks import get_openai_callback


class ConversationChain:
    def __init__(self):
        self.llm = ChatOpenAI(
            model_name=os.environ.get("OPENAI_MODEL_NAME", "gpt-3.5-turbo")
        )
        self.memory = None
        self.llm_chain = None

    def setup(self, vectorstore):
        self.memory = ConversationBufferMemory(
            memory_key="chat_history", return_messages=True
        )
        self.vectorstore = vectorstore

        self.llm_chain = ConversationalRetrievalChain.from_llm(
            llm=self.llm, retriever=self.vectorstore.as_retriever(), memory=self.memory
        )

        return self.llm_chain

    def generate_response(self, question):
        const = 0.0

        with get_openai_callback() as cb:
            response = self.llm_chain.run(question)

            if cb is not None:
                cost = round(cb.total_cost, 5)

        return response, cost

    def reset_chat(self):
        if self.memory is not None:
            self.memory = ConversationBufferMemory(
                memory_key="chat_history", return_messages=True
            )

        if self.llm_chain is not None:
            self.llm_chain = ConversationalRetrievalChain.from_llm(
                llm=self.llm,
                retriever=self.vectorstore.as_retriever(),
                memory=self.memory,
            )
