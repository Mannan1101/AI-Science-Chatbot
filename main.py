from dotenv import load_dotenv
from agents import set_tracing_disabled
import chainlit as cl
from handlers import start_chat, handle_message

set_tracing_disabled(True)
load_dotenv(override=True)

# Register Chainlit event handlers
cl.on_chat_start(start_chat)
cl.on_message(handle_message)
