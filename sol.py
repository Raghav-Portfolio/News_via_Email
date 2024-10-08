import requests
from email_writing import send_email

api = "8457b05cd33e42d1a2027f52d96a4823 "
url = 'https://newsapi.org/v2/everything?q=tesla&from='\
      '2024-09-08&sortBy=publishedAt&apiKey'\
      '=8457b05cd33e42d1a2027f52d96a4823'

#make a request
request = requests.get(url)

#Get a dictionary of the data instead of a plain string
content = request.json()

text = []

#Access article title and description
for article in content['articles']:
    text.append(article['title'] + '\n')
    text.append(article['description'] + '\n\n\n')

message = ''.join(text)
#Encode the message as UTF-8 instead of ASCII as it can't encode characters like é 
message = message.encode('utf-8')

#Finally, send the email
send_email(message)