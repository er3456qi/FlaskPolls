import os

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True # 启动Flask的Debug模式
BCRYPT_LEVEL = 13 # 配置Flask-Bcrypt拓展
SECRET_KEY = 'somesecretkey' # Flask使用这个密钥来对cookies和别的东西进行签名。

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
SQLALCHEMY_TRACK_MODIFICATIONS = True