from crypto_info import get_data
import smtplib, os 
from dotenv import load_dotenv
from email.mime.text import MIMEText
from termcolor import colored


def export(profile):
    load_dotenv()
    user_email = profile["email"]
    GMAIL_USERNAME = os.getenv('GMAIL_USERNAME')
    GMAIL_APP_PASSWORD = os.getenv('GMAIL_APP_PASSWORD')
    if GMAIL_USERNAME == None or GMAIL_APP_PASSWORD == None:
        print(colored(".env file was not found, email export is not available", "red"))
    elif "test" in user_email.lower():
        print(colored("Your email is used for testing, message won't be sent", "red"))
    else:
        try:
            text = f"""Hello {profile["name"]},\nYour currently have ${profile["money"]}\nYour assets are:\n"""
            for asset in profile["assets"]:
                text.append(f"""{asset["ammount"]} {asset["symbols"]}\n""")
            message = MIMEText(text)
            message["Subject"] = "Data export"
            message["To"] = user_email
            message["From"] = f"{GMAIL_USERNAME}@gmail.com"
            
            smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            smtp_server.login(GMAIL_USERNAME, GMAIL_APP_PASSWORD)
            smtp_server.sendmail(message["From"], [user_email], message.as_string())
            smtp_server.quit()
            print(colored("Message sucessfully sent to your email", "yellow"))
        except:
            print(colored("An error occured while sending email message", "red"))
            
    print(colored("Enter anything to continue: ", "green"), end = "")
    input("")