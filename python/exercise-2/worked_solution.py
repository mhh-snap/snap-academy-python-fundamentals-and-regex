def caesar_cipher(
    alphabet: str,
    text: str,
    shift: int,
    encode: bool=False       
):
    """
    Performs a Caesar Cipher on a given corpus for a given
    shift. Able to encode or decode depending on user
    preference

    :param text: Corpus to be transformed by cipher.
    :type text: str
    :param shift: Shift amount for Caesar Cipher. When encoding think clockwise shift.
    :type shift: int
    :param encode: indicator representing wether we encode or decode message.
    :type encode: bool
    :return: Transformed Corpus
    :rtype: str
    """
    alphabet_len = len(alphabet)

    if not encode:
        shift *= -1

    shifted_alphabet = "".join(alphabet[(i + shift) % alphabet_len] for i in range(alphabet_len))

    translation_map = str.maketrans(alphabet, shifted_alphabet)

    return text.translate(translation_map)

def main(text: str):
    """
    :param text: Input text.
    :type text: str
    """
    lc_alphabet = "".join(chr(i) for i in range(97, 123))

    sample_text = text[:18]
    
    for j in range(1, len(lc_alphabet) + 1):
        print(f"shift: {j}, sample_text: {caesar_cipher(alphabet=lc_alphabet, text=sample_text, shift=j)} \n")

    # by inspection this tells us that we can decode using a shift of 21

    decoded_message = caesar_cipher(alphabet=lc_alphabet, text=text, shift=21)
    print(decoded_message)

if __name__ == "__main__":
    input_file = r"C:\Users\MilesHoar-Hewitt\Documents\python\python-fundamentals\exercise-2\input.txt"
    with open(input_file, "r") as file:
        raw_file = file.read()

    puzzle_input = raw_file.replace("\n", "").strip().lower()

    main(text=puzzle_input)
