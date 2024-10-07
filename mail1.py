

import smtplib #simple mail transfer protocol

s=smtplib.SMTP("smtp.gmail.com",587)

s.starttls()

s.login('rinurinuzz01@gmail.com',"tejg fjmc vdin viqy")

msg="hello how are you"

s.sendmail("rinurinuzz01@gmail.com","shazzshahinsha9@gmail.com",msg)

s.quit()