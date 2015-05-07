from collections import Counter

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
    """Return the ASCII art snowman corresponding to the 8-character input
    code given as a string. Each character from '1234' selects one of four
    possible variants for each of the snowman's sections.
    """
    if not len(code) == 8 and all(c in '1234' for c in code):
        raise ValueError("The input code must comprise 8 characters "
                         "from '1234'")
    sections = {k: SECTIONS[k][int(i)-1] for k, i in zip('HNLRXYTB', code)}
    def generate_snowman():
        count = Counter()
        for c in SNOWMAN:
            if c in sections:
                yield sections[c][count[c]]
                count[c] += 1
            else:
                yield c
    return ''.join(generate_snowman())
