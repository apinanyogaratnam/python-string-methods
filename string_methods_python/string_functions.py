from constants import (ALPHABET_LOWERED, ALPHABET_CAPITALIZED, DIGITS_STRING)
from helper_functions import len_copy


def capitalize(word): # string method DONE
    """ Return a copy of the string with its first character capitalized and
    the rest lowercased.

    >>> capitalize('name')
    'Name'
    >>> capitalize('Hello')
    'Hello'
    >>> capitalize('HELLO WORLD')
    'Hello world'
    >>> capitalize('')
    ''
    """

    # return word.capitalize()
    if word == '':
        return ''
    elif word[0] in ALPHABET_LOWERED:
        return (ALPHABET_CAPITALIZED[index(word[0], ALPHABET_LOWERED)] +
                lower(word[1:]))
    return word[0] + lower(word[1:])


def lower(word): # string method DONE
    """ Return a copy of the string with all the cased characters converted to
    lowercase.

    >>> lower('NAME')
    'name'
    >>> lower('name')
    'name'
    >>> lower('')
    ''
    """

    # return word.lower()
    new_word = ''
    for char in word:
        if char in ALPHABET_CAPITALIZED:
            new_word += swapcase(char)
        else:
            new_word += char
    return new_word


def upper(word): # string method DONE
    """ Return a copy of the string with all the cased characters 4 converted to
    uppercase.

    >>> upper('name')
    'NAME'
    >>> upper('NAME')
    'NAME'
    >>> upper('')
    ''
    >>> upper('123abc')
    '123ABC'
    """

    # return word.upper()
    new_word = ''
    for char in word:
        if char in ALPHABET_LOWERED:
            new_word += ALPHABET_CAPITALIZED[index(char, ALPHABET_LOWERED)]
        else:
            new_word += char
    return new_word


def is_lower(word): # string method
    """ Return True if and only if all the characters in word are lowercase
    characters.

    >>> is_lower('name')
    True
    >>> is_lower('Name')
    False
    >>> is_lower('')
    False
    >>> is_lower('12asd')
    True
    """

    # return word.islower()
    if word == '':
        return False
    for char in word:
        if not char in ALPHABET_LOWERED and char in ALPHABET_CAPITALIZED:
            return False
    return True


def is_upper(word): # string method
    """ Return True if and only if all the characters in word are uppercase
    characters.

    >>> is_upper('name')
    False
    >>> is_upper('NAME')
    True
    >>> is_upper('')
    False
    """

    # return word.isupper()
    if word == '':
        return False
    for char in word:
        if not char in ALPHABET_CAPITALIZED and char in ALPHABET_LOWERED:
            return False
    return True


def is_digit(word): # string method
    """ Return True if and only if all characters in word are digits.

    >>> is_digit('12341234')
    True
    >>> is_digit('qwer')
    False
    >>> is_digit('qwer1234')
    False
    >>> is_digit('')
    False
    """

    # return word.isdigit()
    if word == '':
        return False
    for char in word:
        if not char in DIGITS_STRING:
            return False
    return True


def is_alpha(word): # string method
    """ Return True if and only if all characters in word are alphabetic.

    >>> is_alpha('name')
    True
    >>> is_alpha('1234')
    False
    >>> is_alpha('qwer1234')
    False
    >>> is_alpha('')
    False
    """

    # return word.isalpha()
    if word == '':
        return False
    for char in word:
        if not (char in ALPHABET_LOWERED + ALPHABET_CAPITALIZED):
            return False
    return True


def starts_with(begin_word, word):
    """ Return True if and only if word starts with begin_word.

    >>> starts_with('hello', 'hello world')
    True
    >>> starts_with('world', 'hello world')
    False
    >>> starts_with('', '')
    True
    """

    # return word.startswith(begin_word)
    for i in range(len_copy(begin_word)):
        if begin_word[i] != word[i]: return False
    return True


def ends_with(end_word, word):
    """ Return True if and only if word ends with end_word.

    >>> ends_with('world', 'hello world')
    True
    >>> ends_with('hello', 'hello world')
    False
    >>> ends_with('', '')
    True
    >>> ends_with('hello there', 'a')
    False
    >>> ends_with('a', 'a')
    True
    """

    # return word.endswith(end_word)
    if len_copy(end_word) > len_copy(word): return False
    return word[len_copy(word) - len_copy(end_word):] == end_word


def is_space(word):
    """ Return True if and only if the string is a whitespace string.

    >>> is_space(' ')
    True
    >>> is_space('         ')
    True
    >>> is_space('        a')
    False
    >>> is_space('')
    False
    """

    # return word.isspace()
    if word == '': return False
    for char in word:
        if not char == ' ': return False
    return True


def index(obj, objects): # string method
    """ Return the index of obj in objects or return -1 if not found.

    >>> index('name', ['phone', 'address', 'name', 'postal code'])
    2
    >>> index('Hello', ['hello', 'world', 'how', 'are' 'you'])
    -1
    """

    # linear search
    # make a function for range
    # return objects.index(obj)
    for i in range(len_copy(objects)):
        if objects[i] == obj: return i
    return -1


def swapcase(word):
    """ Return a copy of the string with uppercase characters converted to
    lowercase and vice versa.

    >>> swapcase('name')
    'NAME'
    >>> swapcase('NaMe')
    'nAmE'
    >>> swapcase('name123')
    'NAME123'
    """

    new_word = ''
    for char in word:
        if char in ALPHABET_CAPITALIZED:
            new_word += ALPHABET_LOWERED[index(char, ALPHABET_CAPITALIZED)]
        elif char in ALPHABET_LOWERED:
            new_word += ALPHABET_CAPITALIZED[index(char, ALPHABET_LOWERED)]
        else: new_word += char
    return new_word


def casefold(word): # string method
    """ Return a lowercase version of word for caseless comparison

    >>> casefold('NAME')
    'name'
    >>> casefold('NaMe')
    'name'
    """
    #return word.casefold()

    return lower(word)


def center(word, length_needed, padding): # string method
    """ Return a string with given padding on the edges with desired length
        if length_needed is odd, padding will be added to the beginning

    >>> center("name", 4, 'a')
    'name'
    >>> center("name", 8, '*')
    '**name**'
    >>> center("name", 9, '*')
    '***name**'
    >>> center("name", 8, '**')
    '**name**'
    """
    #return word.center(length_needed, padding)

    if length_needed <= len_copy(word): return word

    for i in range(int((length_needed-len_copy(word))/len_copy(padding))):
        if i%2 == 0: word = padding + word
        else: word = word + padding
    return word


# method overloading count()
def count(word, substring): # string method OP (optional parameters)
    """Return the number of non-overlapping occurrences of substring sub in the
    range [start, end]. Optional arguments start and end are interpreted as in
    slice notation.

    >>> count("Hello", "l")
    2
    >>> count("Hello", "Hell")
    1
    
    """
    # return word.count(substring)

    counter = 0
    for i in range(len_copy(word)):
        if word[i:len_copy(substring)+i] == substring:
            counter += 1
    return counter


def count(word, substring, start_index): # string method OP (optional parameters)
    """Return the number of non-overlapping occurrences of substring sub in the
    range [start, end]. Optional arguments start and end are interpreted as in
    slice notation.

    >>> count("Hello", "l", 1)
    2
    >>> count("Hello", "Hell", 1)
    0
    
    """
    # return word.count(substring)

    counter = 0
    word = word[start_index:]
    for i in range(len_copy(word)):
        if word[i:len_copy(substring)+i] == substring:
            counter += 1
    return counter


def count(word, substring, start_index, end_index):
    """Return the number of non-overlapping occurrences of substring sub in the
    range [start, end]. Optional arguments start and end are interpreted as in
    slice notation.

    >>> count("Hello", "l", 0, len_copy("Hello"))
    2
    >>> count("Hello", "Hell", 1, 2)
    0
    
    """
    # return word.count()

    word = word[start_index:end_index]
    counter = 0
    for i in range(len_copy(word)):
        if word[i:len_copy(substring)+i] == substring:
            counter += 1
    return counter


if __name__ == '__main__':
    import doctest
    doctest.testmod()
