import smtplib
import optparse
import subprocess
from emailsender_art import logo


def get_options():
    parser = optparse.OptionParser()
    parser.add_option('-e', '--email', dest="email", help="Your email address.")
    parser.add_option('-p', '--password', dest='password', help="Your email address' password.")
    parser.add_option('-d', '--destination', dest='destination', help='Destination mail address.')
    parser.add_option('-h', '--host', dest='host', help='Smpt server of your email.')
    (options, arguments) = parser.parse_args()
    if not options.email or not options.password or not options.destination or not options.host:
        parser.error("[-] Please don't leave any option empty.")
    if options.host == 'gmail':
        options.host = 'smpt.gmail.com'
    elif options.host == 'hotmail':
        options.host = 'smpt.outlook.com'
    elif options.host == 'yahoo':
        options.host = 'smpt.mail.yahoo.com'
    return options


def send_email(email, passwd, destination, host):
    subprocess.call('clear',shell=True)
    print(logo)
    subject = input('[+] Enter Your subject >')
    message = input('[+] Enter your message >')
    with smtplib.SMTP(host, port=587) as connection:
        connection.starttls()
        connection.login(email, passwd)
        connection.sendmail(
            from_addr=email,
            to_addrs=destination,
            msg=f'Subject:{subject}\n\n{message}'
        )


options = get_options()
send_email(email=options.email, passwd=options.password, destination=options.destination, host=options.host)
