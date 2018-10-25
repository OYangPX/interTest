import yaml
import os
import xlrd

from interTest.comment.log import logger


class YamlReader:

    def __init__(self,config):

        if os.path.exists(config):
            self.config = config
        else:
            raise FileNotFoundError('配置文件不存在')
            
        self._data = None

    '''
        读取结果保存为list
    '''
    @property
    def data(self):
        if not self._data:
            with open(self.config,'rb') as f:
                self._data = list(yaml.safe_load_all(f))

        return self._data


class execlReader:

    def __init__(self,config,sheetName='sheet1'):
        if os.path.exists(config):
            self.config = config

            self.data = xlrd.open_workbook(config)
            self.table = self.data.sheet_by_name(sheetName)
            #获取第一行的key值
            self.keys = self.table.row_values(0)

            self.rowNum = self.table.nrows

            self.colNum = self.table.ncols

        else:
            raise FileNotFoundError('配置文件不存在')


    '''
        读取xls文件
    
    '''
    @property
    def readXls(self):
        if self.rowNum<=1:
            logger.info('总行数小于1')
        else:
            result = []
            j=1

            for i in list(range(self.rowNum-1)):
                val={}
                #从第二行开始取值
                val['rowNum']=i+2
                values = self.table.row_values(j)

                for x in self.table.row_values(j):
                    val[self.keys[x]] = values[x]
                result.append(val)
                j+=1

        return result

if __name__ =="__main__":
    path = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
    case_path = os.path.join(path,'config','case.xls')
    data = YamlReader(case_path).data
    print(type(data))
    print(data)

