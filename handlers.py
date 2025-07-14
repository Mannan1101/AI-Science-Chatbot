import chainlit as cl
from agents import Runner
from agent_setup import science

@cl.on_chat_start
async def start_chat():
    await cl.Message("🧪 Welcome to ScienceBot!").send()

@cl.on_message
async def handle_message(message: cl.Message):
    content = message.content.strip()

    history = cl.user_session.get("history", [])

    if content.lower() == "history":
        all_history = "\n".join(history) if history else "📭 No history yet."
        await cl.Message(content=all_history).send()
        return

    history.append(f"🧑 User: {content}")
    cl.user_session.set("history", history)

    result = await Runner.run(science , content)

    history.append(f"🤖 Agent: {result.final_output}")
    cl.user_session.set("history", history)

    await cl.Message(content=result.final_output).send()
