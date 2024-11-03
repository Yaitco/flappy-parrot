import math
import random
from game.window import game_window
from game import const

def distance(point_1=(0, 0), point_2=(0, 0)) -> float:
    """Returns the distance between two points"""
    return math.sqrt((point_1[0] - point_2[0]) ** 2 + (point_1[1] - point_2[1]) ** 2)

def next_pipe_mid(mid):
    LOWER_BOUND = max(game_window.height * const.PIPE_OFFSET, mid - const.PIPE_RANGE * game_window.height)
    UPPER_BOUND = min(game_window.height * (1 - const.PIPE_OFFSET), mid + const.PIPE_RANGE * game_window.height)
    return random.uniform(LOWER_BOUND, UPPER_BOUND)