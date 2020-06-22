from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_welcome_email(receiver,password):
    subject = 'Welcome to TechLand'
    sender = 'muneneeekev@gmail.com'

    text_content = render_to_string('email/newsmail.txt',{'name':'name'})


    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.send()
