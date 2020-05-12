import inspy_logger
from inspi_sense.helpers.constants import PROG_NAME


class InsPiSense:

    def get_config(self, path=None):
        from inspi_sense.helpers.filesystem import FileSystem
        fs = FileSystem()
        if path is None:
            from inspi_sense.models.windows.config_win import ConfigWindow

            conf_window = ConfigWindow()
            return conf_window.values

    def __init__(self, cl_args):

        _logger = inspy_logger.start(PROG_NAME, cl_args.is_verbose)
        self.info = _logger.info

        self.info(f'Received the following from the command-line: {cl_args}')

        self.config = self.get_config()

