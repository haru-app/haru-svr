import sys
import json


class Config:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Config, cls).__new__(cls)

            filePath = None

            if len(sys.argv) <= 1 or ('dev' == sys.argv[1]) or ('development' == sys.argv[1]):
                filePath = './config/development.json'
            else:
                filePath = './config/%s.json' % sys.argv[1]

            with open(filePath, "r") as jsonFile:
                cls.config = json.load(jsonFile);

            print(cls.config)

        return cls.instance

    def __init__(self):
        super().__init__()

    @classmethod
    def getConfig(cls):
        return cls.config
