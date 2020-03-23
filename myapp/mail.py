import smtplib

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("authixx@gmail.com", "SHEERO12")
message = "Message_you_need_to_send"
s.sendmail("authixx@gmail.com", "vijay@student.tce.edu", message)
s.quit()
