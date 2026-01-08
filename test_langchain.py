import os
from langchain_openai import ChatOpenAI

# 1. Set your API key (Replace with your actual key)
os.environ["OPENAI_API_KEY"] = "your api_key"

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




