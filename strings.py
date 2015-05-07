def all_equal(sequence):
    """Test if all items in the sequence are equal or if the sequence is
    empty.

    >>> all_equal('aaaa')
    True
    >>> all_equal([])
    True
    >>> all_equal(range(5))
    False
    """
    # solution from http://stackoverflow.com/a/3844832/4621513
    return len(set(sequence)) <= 1

def string_is_rectangular(s):
    """Test if a string occupies a rectangular area when printed, i.e.,
    all lines have the same length.

    >>> string_is_rectangular('')
    True
    >>> string_is_rectangular('asdf')
    True
    >>> string_is_rectangular('asdf\\nqwer')
    True
    >>> string_is_rectangular('asdf\\nqwert')
    False
    """
    return all_equal(map(len, s.splitlines()))

def string_join_horizontal(strings, between=''):
    """Join a sequence of rectangular strings horizontally, preserving the
    layout of each string. All strings must have the same number of lines.
    Between two strings a column of `between` is inserted.
    """
    splitlines = str.splitlines
    return '\n'.join(between.join(lines)
                     for lines in zip(*map(splitlines, strings)))
