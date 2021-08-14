import smtplib
import subprocess
import getpass
from emailsender_art import logo


def send_email():
    subprocess.call('clear',shell=True)
    print(logo)
    email = input('[+] Enter your email >')
    passwd = getpass.getpass("[+] Enter your email's password >")
    destination = input('[+] Enter destination email >')
    subject = input('[+] Enter your subject >')
    message = input('[+] Enter your message >')
    host = input('[+] Enter your host server >')
    if host == 'gmail':
        host = 'smpt.gmail.com'
    elif host == 'hotmail':
        host = 'smpt.outlook.com'
    elif host == 'yahoo':
        host = 'smpt.mail.yahoo.com'
    with smtplib.SMTP(host, port=587) as connection:
        connection.starttls()
        connection.login(email, passwd)
        connection.sendmail(
            from_addr=email,
            to_addrs=destination,
            msg=f'Subject:{subject}\n\n{message}'
        )


send_email()
