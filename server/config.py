import os
from dotenv import load_dotenv

load_dotenv()  



SQLALCHEMY_DATABASE_URI = "postgresql://planet@localhost:5432/late_show_db"
SQLALCHEMY_TRACK_MODIFICATIONS = False
JWT_SECRET_KEY = "a7f3d84c72e34b9ea0bfa2ef84cb96312ad67821e678c5d798a25eec5d4b4e99"
