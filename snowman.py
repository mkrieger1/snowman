SNOWMAN = '\n'.join(
  (' HHHHH ',
   ' HHHHH ',
   'X(LNR)Y',
   'X(TTT)Y',
   ' (BBB) ')
)

HAT = [
  (r'     ',
   r'_===_'),
  (r' ___ ',
   r'.....'),
  (r'  _  ',
   r' /_\ '),
  (r' ___ ',
   r'(_*_)')
]
NOSE = ',._ '
EYE_LEFT = '.oO-'
EYE_RIGHT = EYE_LEFT
ARM_LEFT = [' <', r'\ ', ' /', '  ']
ARM_RIGHT = [' >', '/ ', r' \', '  ']
TORSO = [' : ', '] [', '> <', '   ']
BASE = [' : ', '" "', '___', '   ']

SECTIONS = {
  'H': HAT,
  'N': NOSE,
  'L': EYE_LEFT,
  'R': EYE_RIGHT,
  'X': ARM_LEFT,
  'Y': ARM_RIGHT,
  'T': TORSO,
  'B': BASE
}

def snowman(code):
    """Return the ASCII art snowman corresponding to the 8-digit input
    code given as a string. Each of the digits selects one of four
    possible variants for each of the snowman's sections.
    """
    pass
