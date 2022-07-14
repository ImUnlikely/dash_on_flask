import os
class BaseConfig:
    SECRET_KEY = os.environ['SECRET_KEY']
