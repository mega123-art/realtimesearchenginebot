from googlesearch import search
from groq import Groq
from json import load, dump
import datetime
from dotenv import dotenv_values



env_vars=dotenv_values(".env")

#retreive envio vars

username=env_vars["USERNAME"]
assistant_name=env_vars["ASSISTANT_NAME"]
Groqapi_key=env_vars["GROQ_API_KEY"]


client=Groq(api_key=Groqapi_key)

System=f"""Hello, I am {username}, You are a very accurate and advanced AI chatbot named {assistant_name} which has real-time up-to-date information from the internet.
*** Provide Answers In a Professional Way, make sure to add full stops, commas, question marks, and use proper grammar.***
*** Just answer the question from the provided data in a professional way. ***"""
try:
    with open(r"chatbot.json","r") as f:
        messages=load(f)
except:
    with open(r"chatbot.json","w") as f:
        dump([],f)
        
#function for google search
def GoogleSearch(query):
    results=list(search(query,advanced=True, num_results=10))
    Answer=f"The search results for '{query}' are: \n[start]\n"

    for i in results:
        Answer += f"Title: {i.title}\nDescription: {i.description}\n\n"
    Answer+="[end]"
    return Answer


#function for cleaning answers by removing emptylines
def Answermodifier(Answer):
    lines=Answer.split("\n")
    non_emptylines=[line for line in lines if line.strip()]
    modifiedAnswer="\n".join(non_emptylines)
    return modifiedAnswer
#predifined chatbot conversation system message and an initial user lines
SystemChatbot=[
    {"role":"system","content":System},
    {"role":"user","content":f"Hello {assistant_name}"},
    {"role":"assistant","content":"Hello {username}"}
]
def Information():
    data=""
    current_data_time=datetime.datetime.now()
    day=current_data_time.strftime("%A")
    date=current_data_time.strftime("%d")
    month=current_data_time.strftime("%B")
    year=current_data_time.strftime("%Y")
    time=current_data_time.strftime("%I:%M %p")
    data+=f"use this real-time information if needed\n"
    data+=f"day: {day}\n"
    data+=f"date: {date}\n"
    data+=f"month: {month}\n"
    data+=f"year: {year}\n"
    data+=f"time: {time}\n"
    
    return data

def realtimesearchengine(query):
    global SystemChatbot, messages

    with open(r"Data\chatbot.json","r") as f:
        messages=load(f)
    messages.append({"role":"user","content":f"{query}"})

    SystemChatbot.append({"role":"user","content":GoogleSearch(query)})

    completion=client.chat.completions.create(
        model="llama3-70b-8192",
        messages=SystemChatbot+[{"role":"user","content":Information()}]+messages,
        temperature=0.7,
        max_tokens=2048,
        top_p=1,
        stream=True,
        stop=None
    )
    Answer=""
    for chunk in completion:
        if chunk.choices[0].delta.content:
            Answer+=chunk.choices[0].delta.content
    #CLEANING RESPONSE
    Answer=Answer.strip().replace("</s>", "")
    messages.append({"role":"assistant","content":Answer})
    with open(r"chatbot.json","w") as f:
        dump(messages,f,indent=4)

    #remove the most recent user message from the SystemChatbot list

    SystemChatbot.pop()
    return Answermodifier(Answer)

if __name__=="__main__":
    while True:
        query=input("Enter your query: ")
        print(realtimesearchengine(query))
