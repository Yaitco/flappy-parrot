from game import pipe, resources, const
from game.window import game_window

def generate_pipe(mid=game_window.height//2, batch=None):
    pipe_x = game_window.width + resources.upper_pipe_image.width / 2
    half_gap = const.PIPE_GAP / 2 * game_window.height
    upper_pipe = pipe.Pipe(img=resources.upper_pipe_image, x=pipe_x, y=mid + half_gap, batch=batch)
    lower_pipe = pipe.Pipe(img=resources.lower_pipe_image, x=pipe_x, y=mid - half_gap, batch=batch, is_upper=False)
    return [lower_pipe, upper_pipe]

