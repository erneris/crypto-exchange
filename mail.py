import sys, requests, json, credentials, smtplib
from email.mime.text import MIMEText

def main():
    try:
        mail, api = sys.argv[1], sys.argv[2]
        if "." not in mail or "@" not in mail or mail.split("@")[0] == "" or mail.split("@")[1] == "":
            raise IndexError
        if api == "cat":
            text = cat_fact()
            send_email(text, mail)
        elif api == "crypto":
            while True:
                symbol = input("Enter cryptocurrency symbol (e.g. BTC): ")
                if not crypto_check(symbol):
                    print("This cryptocurrency doesn't exist\n")
                    pass
                else:
                    send_email(crypto_check(symbol), mail)
                    break
            
        else:
            raise IndexError

    except IndexError:
        print("Invalid usage.")
        sys.exit(1)

def cat_fact(): #gets a random cat fact and formats it to human-readible text
    data = requests.get("https://meowfacts.herokuapp.com").json()["data"][0]
    text = f"""Hello,\nThis is your random cat fact:\n{data}\nHave a nice day!"""
    return text

def crypto_check(symbol): #return cryptocurrency data on specified symbol, if symbol doesn't exist, return false
    symbol = symbol.replace(" ", "").upper()
    request = requests.get("https://api.coincap.io/v2/assets").json()["data"]

    if not any(currency["symbol"] == symbol for currency in request):
        return False
    
    data = {}
    for currency in request:
        if currency["symbol"] == symbol:
            data = currency
            break
    
    text = f"""Hello,\nCurrently price of {data["name"]} ({data["symbol"]}) is ${float(data["priceUsd"]):.2f}.
In last 24 hours price of the cryptocurrency has changed by {float(data["changePercent24Hr"]):.2f}%
Have a nice day!"""
    return text

def send_email(message, mail): #sends email containing provided message to provided email adress
    try:
        message = MIMEText(message)
        message["Subject"] = "mail.py output"
        message["To"] = mail
        message["From"] = f"{credentials.GMAIL_USERNAME}@gmail.com"
        
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.login(credentials.GMAIL_USERNAME, credentials.GMAIL_APP_PASSWORD)
        smtp_server.sendmail(message["From"], [mail], message.as_string())
        smtp_server.quit()
    except:
        print("Error while sending email. Try again.")
        return False
    else:
        print("Message sent successfully. Check your mailbox.")
    

if __name__ == "__main__":
    main()

#My top5 used shorcuts:
#cmnd(ctrl) + J - opens and closes terminal
#cmnd(ctrl) + shift + [/] - allows to switch quickly between terminals or files
#cmnd(ctrl) + R - runs currently open python file
#cmnd(ctrl) + S - saves currently open file
#cmnd(ctrl) + W - closes currently running file or app
