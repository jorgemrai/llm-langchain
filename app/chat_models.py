from config import set_env_variable
from langchain_openai import OpenAI
from langchain_google_genai import GoogleGenerativeAI
from langchain_anthropic import ChatAnthropic
from langchain_core.messages import SystemMessage,HumanMessage

set_env_variable()


# Initialize the ChatGPT model
openai_llm = OpenAI()
response = openai_llm.invoke("Hello, how are you?")
print(response)


# Initialize the Gemini model
gemini_pro = GoogleGenerativeAI(model="gemini-2.0-flash")
response = gemini_pro.invoke("Hello, how are you?")
print(response)


#Initialize the Anthropic model
anthropic_model = ChatAnthropic(model="claude-3-openai-20240229")
messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="What is the capital of France?")
]
response = anthropic_model.invoke(messages)
print(response) 