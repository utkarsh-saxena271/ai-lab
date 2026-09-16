from dotenv import load_dotenv

load_dotenv()

from langchain_groq import ChatGroq

model = ChatGroq(
    model='qwen/qwen3.8-27b'
)
 
while(True):
    prompt = input('User: ')
    response = model.invoke(prompt)
    print(response.content)