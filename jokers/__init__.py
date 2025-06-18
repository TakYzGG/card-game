# Init para los jokers

__all__ = ["WhySoSerious"]

from jokers.joker import Joker
from jokers.why_so_serious import WhySoSerious
from jokers.low_quality_joker import LowQualityJoker
from jokers.musico_misterioso import MusicoMisterioso
from jokers.rereremix import ReReRemix
from jokers.sigma_joker import SigmaJoker
from jokers.why_so_serious_perfecto import WhySoSeriousPerfecto

def get_jokers():
    return (WhySoSerious(), LowQualityJoker(),
            MusicoMisterioso(), ReReRemix(),
            SigmaJoker(), WhySoSeriousPerfecto())
