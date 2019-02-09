import string
import logging

logging.basicConfig(level="INFO")


def is_pangram(sentence):
    """
    Determine if a sentence is a pangram. A pangram (Greek: παν γράμμα, pan gramma, "every letter")
    is a sentence using every letter of the alphabet at least once. The best known English pangram
    is: The quick brown fox jumps over the lazy dog.  The alphabet used consists of ASCII letters
    a to z, inclusive, and is case insensitive. Input will not contain non-ASCII symbols.
    :param sentence: String to check
    :return: true or false
    """
    alphabet = string.ascii_lowercase
    if isinstance(sentence, str):
        logging.info("Starting, for string: " + sentence)
        sentence = sorted(set(sentence.lower()))
        prepped_string = ''.join([s for s in sentence if (96 < ord(s) < 144)])
        print(prepped_string)
        if prepped_string == alphabet:
            print('Yes')
            return True
        else:
            print('No')
            return False

    else:
        raise Exception("A type other than String was inputted.")


is_pangram("Five quacking Zephyrs jolt my wax bed.")
