import smtplib, os, json
from email.message import EmailMessage

def notification(message):
  try:
    message = json.loads(message)
    mp3_fid = message["mp3_fid"]
    sender_addres = os.environ.get("GMAIL_ADDRESS")
    sender_password = os.environ.get("GMAIL_PASSWORD")
    receiver_address = message["username"]

    msg = EmailMessage()
    msg.set_content(f"mp3 file_id: {mp3_fid} is now ready!")
    msg["Subject"] = "MP3 Download"
    msg["From"] = sender_addres
    msg["To"] = receiver_address

    session = smtplib.SMTP("smtp.gmail.com", 587)
    session.starttls()
    session.login(sender_addres, sender_password)
    session.send_message(msg, sender_addres, receiver_address)
    session.quit()
    print("Mail sent")
  except Exception as err:
    print(err)
    return err