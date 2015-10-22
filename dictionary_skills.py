# To work on the advanced problems, set to True
ADVANCED = False


def count_unique(input_string):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys, and the number of times
    that word appears in the string as values.


    For example:

        >>> print_dict(count_unique("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time:

        >>> print_dict(count_unique("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different:

        >>> print_dict(count_unique("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}

    """
    #  take a single string and return dictionary
    #  distinct words are keys
    #  number of times words appears in the string is the value

    # create emmpty dictionary
    unique_words_dictionary = {}
    # taking the string and spliting the string by space
    input_string = input_string.split()

    for word in input_string:
        if word not in unique_words_dictionary:
            unique_words_dictionary[word] = 1

        else:
            unique_words_dictionary[word] += 1

    return unique_words_dictionary


def find_common_items(list1, list2):
    """Produce the set of common items in two lists.

    Given two lists, return a list of the common items shared between
    the lists.

    IMPORTANT: you may not not 'if ___ in ___' or the method 'index'.


    For example:

        >>> sorted(find_common_items([1, 2, 3, 4], [1, 2]))
        [1, 2]

    If an item appears more than once in at least one list and is present
    in both lists, return it each time:

        >>> sorted(find_common_items([1, 2, 3, 4], [1, 1, 2, 2]))
        [1, 1, 2, 2]

    (And the order of which has the multiples shouldn't matter, either):

        >>> sorted(find_common_items([1, 1, 2, 2], [1, 2, 3, 4]))
        [1, 1, 2, 2]

    """

    # iterate over both list to find common items
    # return list of common items

    # create an emapty list
    common_items_list = []
    # using for loop to iterate over items in list1
    for item1 in list1:
        # iterating items in list2
        for item2 in list2:
            # if item is same as item in list two append to new list
            if item1 == item2:
                # items are are same append item to new list
                common_items_list.append(item1)
    return common_items_list  # return list of commomn items


def find_unique_common_items(list1, list2):
    """Produce the set of *unique* common items in two lists.

    Given two lists, return a list of the *unique* common items shared between
    the lists.

    IMPORTANT: you may not not 'if ___ in ___' or the method 'index'.


    Just like `find_common_items`, this should find [1, 2]:

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [1, 2]))
        [1, 2]

    However, now we only want unique items, so for these lists, don't show
    more than 1 or 2 once:

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [1, 1, 2, 2]))
        [1, 2]

    """

#FIRST TRY
    # unique_items_list = []  # created empty list for unique items found in both list
    # for item1 in list1:  # for items in list1
    #     for item2 in list2:
    #         if item1 != item2:
    #             unique_items_list.append(item1)

    # return unique_items_list

# SECOND TRY
    # create an emapty list
    common_items_list = []
    # using for loop to iterate over items in list1
    for item1 in list1:
        # iterating items in list2
        for item2 in list2:
            # if item is same as item in list two append to new list
            if item1 == item2:
                # items are are same append item to new list
                common_items_list.append(item1)
    unique_list = set(common_items_list)  # used set function to list unique items and remove duplciates
     #print "unqiue is ", unique
    return list(unique_list)  # created list from the set of unique items


def get_sum_zero_pairs(input_list):
    """Given list of numbers, return list of pair summing to 0.

    Given a list of numbers, add up each individual pair of numbers.
    Return a list of each pair of numbers that adds up to 0.


    For example:

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1]) )
        [[-2, 2], [-1, 1]]

        >>> sort_pairs( get_sum_zero_pairs([3, -3, 2, 1, -2, -1]) )
        [[-3, 3], [-2, 2], [-1, 1]]

    This should always be a unique list, even if there are
    duplicates in the input list:

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1]) )
        [[-2, 2], [-1, 1]]

    Of course, if there are one or more zeros to pair together,
    that's fine, too (even a single zero can pair with itself):

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1, 0]) )
        [[-2, 2], [-1, 1], [0, 0]]

    """
    # # UMA MADE IT WORK WITH LISTS AND SETS!!!!
    # sum_zero_pairs_list = list(set(input_list))
    # output = []

  # for number in input_list:
    #     if number >= 0:
    #         if -number in sum_zero_pairs_list:
    #             if [-number, number] not in output:
    #                 output.append([-number, number])

    # return output
    #####################

    # NOW DO IT WITH DICTIONARIES
    #I THINK I FINALLY DID IT! my output was clear when I ran it

    # if there number in the input_list and the number is -negative in that list and if that
    #-negative number is greater than or qual to 0 add it to dictionary as its key.
    #second iteration if number has the opposite value of key add it add it as value to the dict
    #return dict in list of sum of value pairs
    dict1 = {}
    for number in input_list:
            if (-number) in input_list:
                if -number >= 0:
                    dict1[-(number)] = number
    return dict1.items()

def remove_duplicates(words):
    """Given a list of words, return the list with duplicates removed.

    Do this without using a Python set.

    For example:

        >>> sorted(remove_duplicates(
        ...     ["rose", "is", "a", "rose", "is", "a", "rose"]))
        ['a', 'is', 'rose']

    You should treat differently-capitalized words as different:

        >>> sorted(remove_duplicates(
        ...     ["Rose", "is", "a", "rose", "is", "a", "rose"]))
        ['Rose', 'a', 'is', 'rose']

    """

    # duplciate_words = set(words) set method is unique itmes in list
    duplicates_words = set(words)
    # returns dupliate_words into a list
    return list(duplicates_words)


def encode(phrase):
    """Given a phrase, return the encoded string.

    Replace all "e" characters with "p",
    replace "a" characters with "d", replace "t" characters with "o",
    and "i" characters with "u".

    For example:

        >>> encode("You are a beautiful, talented, brilliant, powerful musk ox.")
        'You drp d bpduouful, odlpnopd, brulludno, powprful musk ox.'
    """
    # first split string by charachter
    # take index of each char in list and replace it with letters
    # joing char back together
    # return phrase

    # list_phrase = pharase.split ()
    # for char in list_phrase: # iterate though word_list for word
    #     if char in

    phrase1 = phrase.replace("e", "p").replace("a", "d").replace("t", "o").replace("i", "u")
    return phrase1


def sort_by_word_length(words):
    """Given list of words, return list of ascending [(len, [words])].

    Given a list of words, return a list of tuples, ordered by word-length.
    Each tuple should have two items--the length of the words for that
    word-length, and the list of words of that word length.

    For example:

        >>> sort_by_word_length(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['ok', 'an']), (3, ['day']), (5, ['apple'])]

    """
    # created empty list
    word_length_dictionary = {}
    word_length_list = []
    for word in words:
        if len(word) not in word_length_dictionary.keys():
            word_length_dictionary[len(word)] = [word]
        else:
            word_length_dictionary[len(word)].append(word)

    for key, value in word_length_dictionary.iteritems():
        word_length_list.append((key, value))

    return word_length_list





def get_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak equivalent.
    Words that cannot be translated into Pirate-speak should pass through
    unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    boy         matey
    madam       proud beauty
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    lawyer      foul blaggart
    the         th'
    restroom    head
    my          me
    hello       avast
    is          be
    man         matey

    For example:

        >>> get_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words:

        >>> get_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'

    """

    pirate_dictionary = {
        "sir": "matey",
        "hotel": "fleabag inn",
        "student": "swabbie",
        "boy": "matey",
        "madam": "proud beauty",
        "professor": "foul blaggart",
        "restaurant": "galley",
        "your": "yer",
        "excuse": "arr",
        "students": "swabbies",
        "are": "be",
        "lawyer": "foul blaggart",
        "the": "th'",
        "restroom": "head",
        "my": "me",
        "hello": "avast",
        "is": "be",
        "man": "matey"
    }

    pirate_translation = []
    word_list = phrase.split()
    for word in word_list:
        if word in pirate_dictionary.keys():
            pirate_translation.append(pirate_dictionary[word])
        else:
            pirate_translation.append(word)

    pirate_translation = " ".join(pirate_translation)
    return pirate_translation



# End of skills. See below for advanced problems.
# To work on them, set ADVANCED=True at the top of this file.
############################################################################


def adv_get_top_letter(input_string):
    """Given an input string, return a list of letter(s) which appear(s) the most the input string.

    If there is a tie, the order of the letters in the returned
    list should be alphabetical.

    For example:
        >>> adv_get_top_letter("The rain in spain stays mainly in the plain.")
        ['i', 'n']

    If there is not a tie, simply return a list with one item.

    For example:
        >>> adv_get_top_letter("Shake it off, shake it off. Shake it off, Shake it off.")
        ['f']

    Spaces do not count as letters.

    """

    pass


def adv_alpha_sort_by_word_length(words):
    """Given a list of words, return a list of tuples, ordered by word-length.

    Each tuple should have two items--a number that is a word-length,
    and the list of words of that word length. In addition to ordering
    the list by word length, order each sub-list of words alphabetically.
    Now try doing it with only one call to .sort() or sorted(). What does the
    optional "key" argument for .sort() and sorted() do?

    For example:

        >>> adv_alpha_sort_by_word_length(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]

    """

    pass

##############################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is just used to print dictionaries in key-alphabetical
    # order, and is only used for our documentation tests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join("%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is used only
    # for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)

if __name__ == "__main__":
    print
    import doctest
    for k, v in globals().items():
        if k[0].isalpha():
            if k.startswith('adv_') and not ADVANCED:
                continue
            a = doctest.run_docstring_examples(v, globals(), name=k)
    print "** END OF TEST OUTPUT"
    print
