from django.core.mail import EmailMultiAlternatives


def sendmail(subject, recipient_list):
    text_content = 'This is an important message.'
    html_content = '<p>This is an <strong>important</strong> message.</p>'
    msg = EmailMultiAlternatives(subject, text_content, 'info@azine.me', recipient_list)    
    msg.attach_alternative(html_content, "text/html")
    msg.send()
