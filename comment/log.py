import logging
import os
import time
from logging.handlers import TimedRotatingFileHandler

from interTest.comment import Config,LOG_PATH


class TestLogger:

    def __init__(self):
        self.logger = logging.getLogger()
        logging.root.setLevel(logging.NOTSET)

        c = Config().get('log')
        now = time.strftime('%Y-%m-%d',time.localtime())

        self.log_name = c.get('file_name') if c and c.get('file_name') else '%s.log' % now

        self.backup_count = c.get('backup') if c and c.get('backup') else 5

        self.console_level = c.get('console_level') if c and c.get('console_level') else 'INFO'

        self.file_level = c.get('file_level') if c and c.get('file_level') else 'DEBUG'

        pattern = c.get('pattern')  if c and c.get('pattern') else '%(asctime)s - %(name)s -%(levelname)s -%(message)s'
        self.formatter = logging.Formatter(pattern)



    @property
    def  get_log(self):

        #避免重复日志
        if not self.logger.handlers:

            console_handler = logging.StreamHandler()


            console_handler.setFormatter(self.formatter)

            console_handler.setLevel(self.console_level)

            self.logger.addHandler(console_handler)

            file_handler = TimedRotatingFileHandler(filename=os.path.join(LOG_PATH,self.log_name),
                                                    when='D',
                                                    interval=1,
                                                    backupCount=self.backup_count,
                                                    delay=True,
                                                    encoding='UTF-8')

            file_handler.setFormatter(self.formatter)
            file_handler.setLevel(self.file_level)
            self.logger.addHandler(file_handler)
        return self.logger

logger = TestLogger().get_log

if __name__ == '__main__':
    logger.info('log config ')