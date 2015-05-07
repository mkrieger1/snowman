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

if __name__=='__main__':
    from sys import argv
    from random import choice
    if not len(argv) > 1:
        code = ''.join(choice('1234') for _ in range(8))
    else:
        code = argv[1]
    print snowman(code)
