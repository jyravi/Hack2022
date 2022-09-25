import pandas as pd
import os
import openai

###Loading data 
df=pd.read_csv('test_email.csv')
content=df['Content'].tolist()


###Define your own categories
categories=["Logistics","Personal","Confirmation","Follow Up"]

###OpenAi api on Azure credentials
openai.api_type = "azure"
###paste your resource name
openai.api_base = "https://[resourcename].openai.azure.com/"
openai.api_version = "2022-06-01-preview"
### Paste your key
openai.api_key = "##############"

###Construct the prompt

def createPrompt(categories,query_text):  
    description=f"Classifiy the email into any one of the following categories :{categories}"
    prompt = (f"{description}\n {query_text}\n")
    return prompt
#print(get_prompt(categories, query_text))

### Make the openai api call

query_text=content[5]
response = openai.Completion.create(
  engine="text-davinci-002",
  prompt=createPrompt(categories,query_text),
  temperature=0,
  max_tokens=64,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0,
  stop=None
)
print(response['choices'])

print(response['choices'][0]['text'])

