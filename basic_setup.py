import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# print(f"Current Directory: {os.getcwd()}")
# print(f"Does .env exist here? {os.path.exists('.env')}")

load_dotenv(override=True)

# 1. Set your API key (Replace with your actual key)
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
print(OPENAI_API_KEY)

# 2. Initialize the Model
# Temperature 0.7 allows for some creativity; gpt-4o-mini is cost-effective
llm = ChatOpenAI(
    temperature=0.7, 
    model="gpt-4o-mini"
)

# 3. Invoke the model
response = llm.invoke("Explain Python in one sentence.")

# 4. Print the result
print("--- AI Response ---")
print(response.content)