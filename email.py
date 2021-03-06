import environment #this is the module that I have created. It contains my email and password
import smtplib #this is a library which uses gmail api to access and send emails


userName = environment.data.user_name 
passWord = environment.data.password

subject = 'Enquiry' 
content = 'Please let me know the status of the project'
msg = f'Subject: {subject}\n\n{content}'


with smtplib.SMTP('smtp.gmail.com', 587) as mail: #587 is the port number
    mail.ehlo()
    mail.starttls()
    mail.ehlo()

    mail.login(userName,passWord)
    mail.sendmail(userName, Sender, msg)

    mail.close()
