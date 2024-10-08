import smtplib, ssl

"""
Before running the script, make sure you've set up 2 - Step Authentication from the account settings 
and then copy the app password using password manager in Google, if you're using Google
"""

def send_email(message):
    host = 'smtp.gmail.com'
    port = 465
    #set up your email and app password here:
    username = '*********'
    password = '*********'
    receiver = '*********'
    
    context = ssl.create_default_context()
   
    
    with smtplib.SMTP_SSL(host, port, context= context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
    
if __name__ == '__main__':
    send_email('This is a test message')
    
