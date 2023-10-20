from flask import Blueprint,render_template,jsonify,redirect,url_for,session
from exts import mail,db
from flask_mail import Message
from flask import request
import random
from models import EmailCaptchaModel,UserModel
from .forms import RegisterForm,LoginForm
from werkzeug.security import generate_password_hash,check_password_hash

bp = Blueprint("auth",__name__,url_prefix="/auth")

@bp.route("login",methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        form = LoginForm(request.form)
        if form.validate():
            email =form.email.data
            password = form.password.data
            user = UserModel.query.filter_by(email=email).first()
            if not user:
                return redirect(url_for("auth.login"))
            if check_password_hash(user.password,password):
                # cookie:存储少量证据（身份证明（登录授权））
                # session(一种解决方案)
                # flask中的session，是经过加密后存储在cookie中
                session['user_id'] = user.id
                return redirect("/")
            else:
                print("密码错误")
                return redirect(url_for("auth.login"))
        else:
            print(form.errors)
            return redirect(url_for("auth.login"))


@bp.route("register",methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template("regist.html")
    else:
        form = RegisterForm(request.form)
        if form.validate():
            email = form.email.data
            username = form.username.data
            password = form.password.data
            user = UserModel(email=email,username=username,password=generate_password_hash(password))
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("auth.login"))
        else:
            print(form.errors)
            return redirect(url_for("auth.register"))


@bp.route("/logout")
def logout():
    session.clear()
    return redirect("/")



@bp.route("/captcha/email")
def get_email_captcha():
    email = request.args.get("email",default="yt1481294865@163.com",type=str)
    captcha = random.randint(100000,999999)
    print(f"{email}       {captcha}")
    msg = Message('Hello', sender='1481294865@qq.com', recipients=[email])
    msg.body = f"验证码是：{captcha}"
    mail.send(msg)
	
    email_captcha = EmailCaptchaModel(email=email,captcha=captcha)
    db.session.add(email_captcha)
    db.session.commit()
    return jsonify({"code":200,"message":"","data":None})

@bp.route("/mail/test")
def mail_test():
    msg = Message('Hello', sender='1481294865@qq.com', recipients=['1481294865@qq.com'])
    msg.body = "邮件已发送！"
    mail.send(msg)
    return "邮件已发送！"
