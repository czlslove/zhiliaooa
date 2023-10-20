SECRET_KEY = "aafsfasdfadgafdgag"

# 数据库配置信息
HOSTNAME = '127.0.0.1'
PORT     = '3306'
DATABASE = 'zhiliaooa'
USERNAME = 'root'
PASSWORD = 'root'
DB_URI   = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI

# 邮件验证信息
# MAIL_SERVER = "smtp.qq.com"
# MAIL_USE_SSL = True
# MAIL_USE_TLS = False
# MAIL_PORT = 465
# MAIL_USERNAEM = "1481294865@qq.com"
# MAIL_PASSWORD = "vbojkpummcwxgfgj"
