import os


class Config(object):
    SECRET_KEY = os.getenv('SECRET_KEY', 'you-will-never-guess')
    UPLOAD_FOLDER = './uploaded_files'
