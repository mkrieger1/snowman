from strings import string_is_rectangular, string_join_horizontal
from random import choice

SNOWMAN = '\n'.join(
  (' HHHHH ',
   ' HHHHH ',
   'X(LNR)Y',
   'X(TTT)Y',
   ' (BBB) ')
)

HAT = [
  (r'     '
   r'_===_'),
  (r' ___ '
   r'.....'),
  (r'  _  '
   r' /_\ '),
  (r' ___ '
   r'(_*_)')
]
NOSE = ',._ '
EYE_LEFT = EYE_RIGHT = '.oO-'
ARM_LEFT = [' <', r'\ ', ' /', '  ']
ARM_RIGHT = [' >', '/ ', ' \\', '  ']
TORSO = [' : ', '] [', '> <', '   ']
BASE = [' : ', '" "', '___', '   ']

SECTIONS = [
  ('H', HAT),
  ('N', NOSE),
  ('L', EYE_LEFT),
  ('R', EYE_RIGHT),
  ('X', ARM_LEFT),
  ('Y', ARM_RIGHT),
  ('T', TORSO),
  ('B', BASE)
]

assert all(len(variants) == 4 for _, variants in SECTIONS)
assert string_is_rectangular(SNOWMAN)

def snowman(code):
    """Return the ASCII art snowman specified by the 8-character input
    code. Each character (from '1234') selects one of the four
    possible variants for the snowman's hat, nose, left eye, right eye,
    left arm, right arm, torso, and base.
    """
    if not (len(code) == 8 and all(c in '1234' for c in code)):
        raise ValueError("The input code must consist of 8 characters "
                         "from '1234'.")
    sections = {letter: iter(variants[int(i)-1])
                for (letter, variants), i in zip(SECTIONS, code)}
    return ''.join(next(sections[c]) if c in sections else c
                   for c in SNOWMAN)

def random_code():
    """Return a random code suitable for creating a snowman."""
    return ''.join(choice('1234') for _ in range(8))

def random_snowman_grid(rows, columns):
    """Return rows * columns snowmen arranged in a grid."""
    def snowman_row():
        codes = (random_code() for _ in range(columns))
        return string_join_horizontal(map(snowman, codes), ' ')
    return '\n\n'.join(snowman_row() for _ in range(rows))

if __name__=='__main__':
    print random_snowman_grid(5, 15)
