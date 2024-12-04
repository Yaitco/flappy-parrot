import math, random
from game.window import game_window
from game import const

def distance(point_1=(0, 0), point_2=(0, 0)) -> float:
    """Returns the distance between two points"""
    return math.sqrt((point_1[0] - point_2[0]) ** 2 + (point_1[1] - point_2[1]) ** 2)

def is_rect_sect(rect1 = ((0, 0), (0, 0)), rect2 = ((0, 0), (0, 0))):
    return is_seg_sect_seg((rect1[0][0], rect1[1][0]), (rect2[0][0], rect2[1][0])) and \
           is_seg_sect_seg((rect1[0][1], rect1[1][1]), (rect2[0][1], rect2[1][1]))

def is_seg_sect_seg(seg1 = (0, 0), seg2 = (0, 0)):
    return not(seg1[1] <= seg2[0] or seg2[1] <= seg1[0])

def is_dot_in_seg(dot = 0, seg = (0, 0)):
    return seg[0] <= dot <= seg[1]

def center_image(image):
    """Sets an image's anchor point to its center"""
    image.anchor_x = image.width / 2
    image.anchor_y = image.height / 2

def next_pipe_mid(mid):
    LOWER_BOUND = max(game_window.height * const.PIPE_OFFSET, mid - const.PIPE_RANGE * game_window.height)
    UPPER_BOUND = min(game_window.height * (1 - const.PIPE_OFFSET), mid + const.PIPE_RANGE * game_window.height)
    return random.uniform(LOWER_BOUND, UPPER_BOUND)