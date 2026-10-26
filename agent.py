from dotenv import load_dotenv
import os
load_dotenv()

from langchain_openrouter import ChatOpenRouter
from langchain.agents import create_agent
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langgraph.checkpoint.memory import InMemorySaver
from tool import send_email_tool

api_key = os.getenv("OPENROUTER_API_KEY")
MODEL = os.getenv("MODEL")

SYSTEM_PROMPT = """You are an email assistant. You can do one thing: send an email.

You need two things before you can send:
1. the recipient's email address
2. the reason for the email — what it is actually about

Rules:
- If either one is missing, ASK for it in one short sentence. Ask for one thing at a time.
- Never invent an email address and never invent a reason. Asking is always better
  than guessing.
- Before Sending the email, first show the draft email to user, and ask the feedback, 
    and if user request to update and again take approval, 
    and once user approve to send the email, then only call the 'send_email' tool 
    and send the mail
- Remember what the user already told you earlier in this conversation. If they gave
  you the address three messages ago, you already have it — do not ask again.
- Once you have both, write the email yourself: a clear one-line subject and a short
  plain-text body of 3 to 6 sentences. No placeholders like [Your Name].
- Then call send_email straight away. Do not ask for permission first.
- After it is sent, reply with one line saying who it went to and the subject.
"""

llm = ChatOpenRouter(
    model=MODEL,
    api_key=api_key,
    temperature=0.7,
    max_tokens=500,
)

def get_agent():
    "Get Agent that send email to any email address"
    return create_agent(
        model=llm,
        tools=[send_email_tool],
        checkpointer=InMemorySaver(),
        system_prompt=SYSTEM_PROMPT
    )