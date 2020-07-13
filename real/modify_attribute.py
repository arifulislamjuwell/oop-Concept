class Email:

    def __init__(self):
        self.is_sent= False
    
    def send_mail(self):
        self.is_sent= True

email_1= Email()
email_1.send_mail()
print(email_1.is_sent)