"""
1. Identify all relevant entries in list and correctly extract the mapping id
2. Unmap Vowels
3. Remove Suffix
"""


import re


VOWEL_MAPPING = {
    "a": "e",
    "e": "i",
    "i": "a",
    "o": "u",
    "u": "o",
}


def _undo_vowel_mapping(name: str, exponent: int) -> str:
    """
    Undoes the vowel mapping.

    :param name: Transformed name.
    :type name: str
    :param exponenent: The number of times the vowel mapping has been applied.
    :return: Original name.
    :rtype: str
    """
    """
    The mapping has order 6 <=> m^6 = i <=> m^5 = m^-1 => m^(-i) = m^5i
    """
    clean_name_list = []
    for letter in name:

        if letter in VOWEL_MAPPING.keys():
            for _ in range((exponent * 5) % 6):
                letter = VOWEL_MAPPING[letter] # don't love this

        clean_name_list.append(letter)

    return "".join(clean_name_list)



def is_altered(name: str) -> bool:
    """Returns True if the name has been altered by hackers."""
    return not (re.match(r"i_love_hacking\d", name) is None)


def clean(name: str) -> str:
    """
    Returns a fully cleaned name.

    :param name: Altered name.
    :type name: str
    :return: Name with digits removed and vowel mapping undone.    
    :rtype: str
    """
    mapping_exp = re.match(r"i_love_hacking(\d)", name).group(1)
    name_no_digits = re.match(r"[a-zA-Z ]*").group(1) # need to make this bit nicer
    return _undo_vowel_mapping(name=name_no_digits, exponent=mapping_exp)


def main(name_list: str) -> None:
    """"""
    altered_names = [clean(name) for name in name_list if is_altered(name)]


if __name__ == "__main__":

    file_path = r"regex\exercise-3\input.txt"
    with open(file_path, "r") as file:
        input_txt = file.read()

    leaked_list = input_txt.split(", ")


    main(name_list=leaked_list)
