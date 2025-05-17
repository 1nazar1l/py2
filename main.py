from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from environs import env
import smtplib

env.read_env()

password = env("PASSWORD")
mail = env("MAIL")

msg = MIMEMultipart()
msg["From"] = mail
msg["To"] = mail
msg["Subject"] = "Test"

module_in_process = ["Основы python", "GitHub", "API"]
completed_module = ["Командная строка", "Введение в python", "Введение в js", "WEB-разработка"]
time = "3 месяца"
text = ""
if len(completed_module) == 0:
    text = f"Привет Мама(Папа), я занимаюсь в школе третье место уже {time}. Сейчас я работаю над модулями {module_in_process}. Пока что я улучшаю свои навыки и узнаю много нового!"
else:
    text = f"Привет Мама(Папа), я занимаюсь в школе третье место уже {time}. В процессе я выполнил модули: {completed_module}! Сейчас я работаю над модулями {module_in_process}. Обучение мне нравится, я получил море знаний!"
msg.attach(MIMEText(text, "plain"))
msg.as_string()

server = smtplib.SMTP_SSL("smtp.yandex.com", 465)

server.login(mail, password=password)
server.sendmail(msg["From"], msg["To"], msg.as_string())
server.quit()