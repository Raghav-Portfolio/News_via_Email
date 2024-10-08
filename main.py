import requests
from email_writing import send_email

topic = 'NVIDIA'
api = "*****"

#make sure you only add the f string at the line that it's required at.
url = 'https://newsapi.org/v2/everything?'\
      f'q={topic}'\
      '&from=2024-09-08&sortBy=publishedAt'\
      '&apiKey=*********'\
      '&language=en'

#make a request
request = requests.get(url)

#Get a dictionary of the data instead of a plain string
content = request.json()

text = []

#Access article title and description
for article in content['articles'][:30]:
    if  article['title'] is not None: #ensure that no blank article gets added
        if article['title'] != '[Removed]':
            text.append("Subject: Today's News" + '\n')
            text.append(article['title'] + '\n')
            text.append(article['url'] + '\n')
            text.append(article['description'] + '\n\n\n')

message = ''.join(text)
#Encode the message as UTF-8 instead of ASCII as it can't encode characters like é 
message = message.encode('utf-8')

#Finally, send the email
send_email(message)
