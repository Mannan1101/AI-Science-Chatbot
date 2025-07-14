from agents import Agent, OpenAIChatCompletionsModel
from config import gemini_client, gemini_model_name

gemini_model_name = OpenAIChatCompletionsModel(openai_client=gemini_client,model=str(gemini_model_name))

science: Agent = Agent(
    name="A.Mannan",
    instructions="you are a goood science teacher,teach students of giaic about science please only answer about science dont reply any thing other questions.",
    model=gemini_model_name
)
