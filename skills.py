"""Skills Assessment: Lists.

To work on an item, uncomment the entire function (including the docstring)
and then run this script. It should output an error that the newly-uncommented
function is now failing its tests.

Edit the function body until you have a solution and the test passes, and then
move on to the next function.

This assessment is DUE TO YOUR ADVISOR BY SUNDAY EVENING.
"""


def all_odd(number_list):
    """Return a list of only the odd numbers in the input list.

        >>> all_odd([1, 2, 7, -5])
        [1, 7, -5]

        >>> all_odd([2, -6, 8])
        []

    """
    odds = []
    for number in number_list:
        if number % 2 == 1:
            odds.append(number)

    return odds
        # I can only get the first one to return [1], and I don't know why. 
        # Advice appreciated!


def all_even(number_list):
    """Return a list of only the even numbers in the input list.

        >>> all_even([2, 6, -1, -2])
        [2, 6, -2]

        >>> all_even([-1, 3, 5])
        []

    """
    evens = []
    for number in number_list:
        if number % 2 == 0:
            evens.append(number)

    return evens

#Similar problem as above. It only adds one number. 

def print_indeces(my_list):
    """Print the index of each list item, followed by the item itself.
    Do this without using a counting variable. I.e. don't do something
    like this:

    count = 0
    for item in list:
        print count
        count = count + 1

    Output should look like this:

    >>> print_indeces(["Toyota", "Jeep", "Volvo"])
    0 Toyota
    1 Jeep
    2 Volvo

    """
    

    for item in my_list:
        print my_list.index(item), item

def long_words(word_list):
    """Return all words in input list that are longer than 4 characters.

        >>> long_words(["hello", "hey", "spam", "spam", "bacon", "bacon"])
        ['hello', 'bacon', 'bacon']

        >>> long_words(["all", "are", "tiny"])
        []

    """
    longer_words = []
    for item in word_list:
        if len(item) > 4:
           longer_words.append(item) 
    
    return longer_words

def smallest_int(number_list):
    """Find the smallest integer in a list of integers and return it.

        >>> smallest_int([-5, 2, -5, 7])
        -5

    If the input list is empty, return None:

        >>> smallest_int([]) is None
        True

    """
    if len(number_list):
        number_list.sort()
        return number_list[0]
    else:
        return None


def largest_int(number_list):
    """Find the largest integer in a list of integers and return it.

        >>> largest_int([-5, 2, -5, 7])
        7

    If the input list is empty, return None:

        >>> largest_int([]) is None
        True

    """
    if len(number_list):
        number_list.sort()
        return number_list[-1]
    else:
        return None


def halvesies(number_list):
    """Return list of numbers from input list, each divided by two.

        >>> halvesies([2, 6, -2])
        [1.0, 3.0, -1.0]

    If any of the numbers are, make sure you don't round off the half:

        >>> halvesies([1, 5])
        [0.5, 2.5]

    """
    halvesies = []
    for item in number_list:
        i = 0
        halved_number = float(item) / 2
        halvesies.append(halved_number)
        i += 1

    return halvesies




def word_lengths(word_list):
    """Return the length of words in the input list.

        >>> word_lengths(["hello", "hey", "hello", "spam"])
        [5, 3, 5, 4]

    """
    word_len = []
    i = 0
    for item in word_list:
        length = len(word_list[i])
        word_len.append(length)
        i += 1
    
    return word_len

def sum_numbers(number_list):
    """Return the sum of all of the numbers in the list.

    Python has a built-in function, `sum()`, which already does this -- but for
    this exercise, you should not use it.

        >>> sum_numbers([1, 2, 3, 10])
        16

    Any empty list should return the sum of zero:

        >>> sum_numbers([])
        0

    """
    for item in number_list:
        if len(number_list) > 0:
            sum = 0
            for item in number_list:
                sum += item
            return sum
        else:
            return 0

# This one works for all tests when I run it in a separate file, but not for the 
# empty list here.

def mult_numbers(number_list):
    """Return product (result of multiplication) of the numbers in the list.

        >>> mult_numbers([1, 2, 3])
        6

    Obviously, if there is a zero in the input, the product will be zero:

        >>> mult_numbers([10, 20, 0, 50])
        0

    As explained at http://en.wikipedia.org/wiki/Empty_product, if the list is
    empty, the product should be 1:

        >>> mult_numbers([])
        1

    """
    for item in number_list:
        if len(number_list) > 0:
            product = 1
            for item in number_list:
                product = product * item
            return product
        else:
            return 1

# This one works for all tests when I run it in a separate file, but not for the 
# empty list here.

def join_strings(word_list):
    """Return a string of all input strings joined together.

    Python has a built-in method on lists, `join` -- but this exercise, you
    should not use it.

        >>> join_strings(["spam", "spam", "bacon", "balloonicorn"])
        'spamspambaconballoonicorn'

    For an empty list, you should return an empty string:

        >>> join_strings([])
        ''

    """
    for word in word_list:
        if len(word_list) >= 1:
            concatenated_words = ""
            for word in word_list:
                concatenated_words = concatenated_words + word
            return concatenated_words
        else:
            return ""

    return ""


def average(number_list):
    """Return the average (mean) of the list of numbers given.

        >>> average([2, 12, 3])
        5.666666666666667

    There is no defined answer if the list given is empty. It's fine if
    this raises an error when given an empty list.
    """
    for item in number_list:
        sum = 0.000000000000000
        for item in number_list:
            sum += item
        return sum / len(number_list)
    return 0


##############################################################################
# END OF SKILLS TEST; YOU CAN STOP HERE OR YOU CAN WORK ON ADVANCED PROBLEMS


def advanced_join_strings(list_of_words):
    """Return a single string with each word from the input list
    separated by a comma.
        >>> advanced_join_strings(["Labrador", "Poodle", "French Bulldog"])
        'Labrador, Poodle, French Bulldog'

     If there's only one thing in the list, it should return just that
     thing, of course:

         >>> advanced_join_strings(["Pretzel"])
         'Pretzel'

     """
    for word in list_of_words:
        concatenation = ", ".join(list_of_words)

    return concatenation


##############################################################################
# You can ignore everything after here

if __name__ == "__main__":
    import doctest
    print
    result = doctest.testmod()
    if not result.failed:
        print "*** %s TESTS PASSED. GOOD WORK!" % result.attempted
    print
