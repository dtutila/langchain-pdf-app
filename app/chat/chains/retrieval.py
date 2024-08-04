from langchain.chains import ConversationalRetrievalChain
from app.chat.chains.streamable import StreamableChain


class StreamingConversationalStreamingChain (
    StreamableChain,
    ConversationalRetrievalChain
):
    pass
