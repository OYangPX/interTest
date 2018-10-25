import os

from interTest.comment.ReadYaml import YamlReader

BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
LOG_PATH=os.path.join(BASE_PATH,'log')
CONFIG_FILE = os.path.join(BASE_PATH,'config','config.yaml')
REPORT_PATH =os.path.join(BASE_PATH,'report')


class Config:

    def __init__(self,config=CONFIG_FILE):

        self.config = YamlReader(config).data

    def get(self,element,index =0):
        return self.config[index].get(element)



if __name__ == "__main__":
    c = Config()
    print(c.get('log'))
    