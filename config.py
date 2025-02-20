import os

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'instance', 'tasks.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
