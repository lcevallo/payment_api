class Config:
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/payment_detail_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False