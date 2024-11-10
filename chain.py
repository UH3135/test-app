from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_upstage import ChatUpstage
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful, smart, kind, and efficient AI assistant. You always fulfill the user's requests to the best of your ability. You always answer succinctly. You must answer in Korean."),
    ("user", "{user_input}"),
    MessagesPlaceholder(variable_name="messages")
])

llm = ChatUpstage()

chain = prompt | llm | StrOutputParser()
