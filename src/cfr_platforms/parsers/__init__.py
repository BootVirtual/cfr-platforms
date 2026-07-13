from . import BucurestiNord
from . import ClujNapoca

PARSERS = {
    "BucurestiNord": BucurestiNord,
    "ClujNapoca": ClujNapoca
}

def get_parser(station):
    return PARSERS[station]