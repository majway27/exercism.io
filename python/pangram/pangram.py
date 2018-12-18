import logging
import string

logging.basicConfig(level=logging.DEBUG)


def is_pangram(sentence):
    """
    Determine if a sentence is a pangram. A pangram (Greek: παν γράμμα, pan gramma, "every letter")
    is a sentence using every letter of the alphabet at least once. The best known English pangram
    is: The quick brown fox jumps over the lazy dog.  The alphabet used consists of ASCII letters
    a to z, inclusive, and is case insensitive. Input will not contain non-ASCII symbols.
    :param sentence: String to check
    :return: true or false
    """
    alphabet = string.ascii_lowercase[:26]
    if isinstance(sentence,str):
        logging.info("You entered a string Bob")
    else:
        raise Exception("A type other than String was inputted.")
    # create a set to eliminate dupes
    sentence_set = {sentence.split()}
    print(sentence_set)
    # order string
    # compare to reference alphabet range
    # decide