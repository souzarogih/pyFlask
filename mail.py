import smtplib


def send_mail_google():
  server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
  server.login("rogih.andrade@gmail.com", "nvvikxyqxdjyemfl")
  server.sendmail(
    "higor.andrade@hotmail.com",
    "rogih.andrade@gmail.com",
    "Higor Deu certo!!!\n Python Here")
  server.quit()


# nvvikxyqxdjyemfl
# https://www.treinaweb.com.br/blog/enviando-email-com-python-e-smtp