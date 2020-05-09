from logging import getLogger
from inspi_sense.helpers.constants import PROG_NAME

class FileSystem:
    def __init__(self):
        self.log = getLogger(PROG_NAME)
        self.log.info(f'Logger started for {__class__.__name__}')
        info = self.log.info
        self.data_dir = None
        info('Variable for the data directory is None')
        self.tmp_dir = None
        info('Variable for the temp directory is None')

def create_data_dir(data_dir=None):
    # Check if directory exists
    #     if not then create it
    #         Child Directories:
    #             - locale
    #             - .tmp
    #             - logs
    #             - config
    #     if exists raise exception
    # Set data_dir variable
    pass

