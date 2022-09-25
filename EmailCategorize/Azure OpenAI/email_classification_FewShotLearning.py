import pandas as pd
import os
import openai

##read the csv file (sample is provided. You may create your own as well.)
df = pd.read_csv('fewshotemail.csv')

text=[]
text=df['Content'].tolist()
label=[]
label=df['actual'].tolist()


###OpenAi api on Azure credentials
openai.api_type = "azure"
###paste your resource name
openai.api_base = "https://[resourcename].openai.azure.com/"
openai.api_version = "2022-06-01-preview"
### Paste your key
openai.api_key = "##############"


key=[]

description="This is an email classifier"
key1="message"
key2="Category"
key=[key1,key2]

####Paste your query text  and construct the openai query####

query_text=" "

def createPrompt(description,key, text, label, query_text):
    prompttext=''
    for i in range(len(text)):
        ptext=''.join(str(key[0])+":"+str(text[i])+" "+str(key[1])+":"+ str(label[i]))
        prompttext+=f"{ptext}\n"
    
    query1=f"{key1}: {query_text} {key2}: "
    prompt = (f"{description}\n {prompttext} {query1}")

    return prompt

response = openai.Completion.create(
  engine="text-davinci-002",
  prompt=createPrompt(description,key, text, label, query_text),
  temperature=0,
  max_tokens=64,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0,
  stop=None
)

print(response['choices'])
