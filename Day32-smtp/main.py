import smtplib

my_email = "varunthapa615@gmail.com"
password = "sgjegmecwdseyjds"
connection = smtplib.SMTP("smtp.gmail.com")

connection.starttls()
connection.login(user=my_email, password=password)

connection.sendmail(from_addr=my_email, to_addrs="varunthapa1920@gmail.com", msg="Subject:Hemlo!\n\nThis is Varunthapa")
connection.close()