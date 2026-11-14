import os
from dotenv import load_dotenv
from urllib.parse import quote_plus

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'you-should-really-change-this-fallback-key')

    # Railway MySQL configuration
    mysql_host = os.getenv('MYSQLHOST')
    mysql_port = os.getenv('MYSQLPORT', '3306')
    mysql_user = os.getenv('MYSQLUSER')
    mysql_password = os.getenv('MYSQLPASSWORD')
    mysql_database = os.getenv('MYSQLDATABASE')

    if mysql_host and mysql_user and mysql_password and mysql_database:
        SQLALCHEMY_DATABASE_URI = (
            f"mysql+pymysql://{quote_plus(mysql_user)}:"
            f"{quote_plus(mysql_password)}@"
            f"{mysql_host}:{mysql_port}/{mysql_database}"
        )
    else:
        SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    RAZORPAY_KEY_ID = os.getenv('RAZORPAY_KEY_ID')
    RAZORPAY_KEY_SECRET = os.getenv('RAZORPAY_KEY_SECRET')

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_USERNAME')

    OTP_EXPIRY_MINUTES = 10

    GOOGLE_OAUTH_CLIENT_ID = os.getenv('GOOGLE_OAUTH_CLIENT_ID')
    GOOGLE_OAUTH_CLIENT_SECRET = os.getenv('GOOGLE_OAUTH_CLIENT_SECRET')
    OAUTHLIB_INSECURE_TRANSPORT = os.getenv('OAUTHLIB_INSECURE_TRANSPORT', '0')

    GITHUB_OAUTH_CLIENT_ID = os.getenv('GITHUB_OAUTH_CLIENT_ID')
    GITHUB_OAUTH_CLIENT_SECRET = os.getenv('GITHUB_OAUTH_CLIENT_SECRET')

    UPLOAD_FOLDER = os.path.join(basedir, 'app', 'static', 'uploads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'webp', 'gif'}

    os.environ["LIBRIVOX_API_URL"] = os.getenv(
        "LIBRIVOX_API_URL",
        "https://librivox.org/api/feed/audiobooks/"
    )