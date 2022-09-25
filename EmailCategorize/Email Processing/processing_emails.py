import numpy as np
import glob

import pandas as pd
import os, sys, email
import numpy as np 
import pandas as pd

import string

email_1 = glob.glob('enron_with_categories/1/*.txt')
email_2 = glob.glob('enron_with_categories/2/*.txt')
email_3 = glob.glob('enron_with_categories/3/*.txt')
email_4 = glob.glob('enron_with_categories/4/*.txt')
email_5 = glob.glob('enron_with_categories/5/*.txt')
email_6 = glob.glob('enron_with_categories/6/*.txt')


email_all=email_1+email_2+email_3+email_4+email_5+email_6

category_len = [] #this list will store number of emails belonging to each category
category_len.append(len(email_1))
category_len.append(len(email_2))
category_len.append(len(email_3))
category_len.append(len(email_4))
category_len.append(len(email_5))
category_len.append(len(email_6))

label = []
for i in range(len(category_len)):
  label = label + [i+1] * category_len[i] #since the emails are stored in an arrangement (category1,category2,...,category6),therefore storing the labels accordingly

print(len(label))

def read_email(pathList):
  temp = []
  for path in pathList:
    with open(path) as f:
      lines = f.read()
      temp.append(lines)
  return temp

email_total=[]
email_final=[]
email_total=read_email(email_all)

for a in email_total:
    b = email.message_from_string(a)
    body = ""

    if b.is_multipart():
        for part in b.walk():
            ctype = part.get_content_type()
            cdispo = str(part.get('Content-Disposition'))

            # skip any text/plain (txt) attachments
            if ctype == 'text/plain' and 'attachment' not in cdispo:
                body = part.get_payload(decode=True)  # decode
                break
    else:
        body = b.get_payload(decode=True).decode('utf-8')
    body = ((body).translate(str.maketrans('', '', string.punctuation))).replace("\n", "").replace("\t"," ")
    
    email_final.append(str(body))
print(len(email_final))

emails_df = pd.DataFrame()
emails_df['Content']=email_final
emails_df['label']=label 
emails_df['actual']=emails_df['label']

emails_df = emails_df.replace({'actual': {1: 'Business_and_Strategy', 
                                2: 'Personal',3: 'Personal_Professional',4:'Logistics',5:'Employment_arrngmnts',6:'Documentediting_Checking'}})

print(len(emails_df))

print(emails_df.head(2))

### Shuffle the dataframe for easily splitting the dataframe into train, test and validation

emails_df = emails_df.sample(frac = 1)
print(emails_df.head(20))
