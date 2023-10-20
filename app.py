# -*- coding: utf-8 -*-

from flask import Flask,session,g

import config

from exts import db,mail

from models import UserModel

from blueprints.auth import bp as auth_bp

from blueprints.qa import bp as qa_bp

from flask_migrate import Migrate
# --------------------------------------------------------------
# 初始化Flask对象
app = Flask(__name__)

# 导入配置信息
app.config.from_object(config)

# 绑定APP
db.init_app(app)
mail.init_app(app)
app.config['MAIL_SERVER'] = 'smtp.qq.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = '1481294865@qq.com'
app.config['MAIL_PASSWORD'] = 'vbojkpummcwxgfgj'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail.init_app(app)

migrate = Migrate(app,db)

app.register_blueprint(auth_bp)
app.register_blueprint(qa_bp)




# hook(钩子函数)
@app.before_request
def my_fun():
    user_id = session.get("user_id")
    if user_id:
        user = UserModel.query.get(user_id)
        setattr(g,"user",user)
    else:
        setattr(g,"user",None)




@app.context_processor
def my_fun1():
    return {"user":g.user}




# 程序入口
if __name__ == "__main__":
    app.run(debug=True)