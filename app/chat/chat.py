from app.chat.models import ChatArgs
from app.chat.vector_stores.pinecode import build_retriever
from app.chat.llms.chatopenai import build_llm
from app.chat.memories.sql_memory import build_memory
from app.chat.chains.retrieval import StreamingConversationalStreamingChain


def build_chat(chat_args: ChatArgs):
    retriever = build_retriever(chat_args)
    llm = build_llm(chat_args)
    memory = build_memory(chat_args)
    return StreamingConversationalStreamingChain.from_llm(
        retriever=retriever,
        llm=llm,
        memory=memory
    )