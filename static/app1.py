from flask import Flask
from flask_mail import Mail, Message

app1 = Flask(__name__)
mail = Mail(app1)
app1.config['MAIL_SERVER'] = 'smtp.qq.com'
app1.config['MAIL_PORT'] = 465
app1.config['MAIL_USERNAME'] = '1481294865@qq.com'
app1.config['MAIL_PASSWORD'] = 'vbojkpummcwxgfgj'
app1.config['MAIL_USE_TLS'] = False
app1.config['MAIL_USE_SSL'] = True
mail = Mail(app1)


@app1.route("/")
def index():
    msg = Message('Hello', sender='1481294865@qq.com', recipients=['1481294865@qq.com'])
    msg.body = "Hello Flask message sent from Flask-Mail"
    mail.send(msg)
    return "Sent"


if __name__ == '__main__':
    app1.run(debug=True)