import os

class Config:
    def __init__(self):
        self.host = os.getenv('HOST', 'localhost')
        self.port = os.getenv('PORT', '8080')

config = Config()
