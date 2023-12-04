import os

class Config:
    SECRET_KEY = '5791628bb0b13ce0c676dfde280ba245'
    #SECRET_KEY = os.getenv(SECRET_KEY)
    basedir = os.path.abspath(os.path.dirname(__file__)) 
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.lolipop.jp'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME ='helloworld@yukinando.com'
    #MAIL_PASSWORD = os.getenv(MAIL_USERNAME)
    MAIL_PASSWORD ='0422_DecoYamasan'
    #MAIL_PASSWORD = os.getenv(MAIL_PASSWORD)