import us
from uszipcode import SearchEngine


class Locales:
    from inspi_sense.helpers.constants import PROG_NAME

    import us

    from logging import getLogger

    from uszipcode import SearchEngine

    log = getLogger(PROG_NAME)
    info = log.info

    info(f'Logger started for {__name__}.{PROG_NAME}')

    @staticmethod
    def validate_zipcode(zip_code: int) -> object:
        search = SearchEngine(simple_zipcode=True)
        res = search.by_zipcode(zip_code)
        return res

    @staticmethod
    def get_territories_and_states():
        states = us.STATES_AND_TERRITORIES

        return states

    def write_list(self):
        pass
