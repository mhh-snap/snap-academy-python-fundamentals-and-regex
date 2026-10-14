import re


def calc_digit_sum(staff_emails: list[str]) -> int:
    """
    :param staff_emails: List of valid staff emails.
    :type staff_emails: list[str]
    :return: Returns sum of all digits in all valid emails.
    :rtype: int
    """
    # METHOD 1 - unpacked for clarity
    email_concat = "".join(staff_emails)
    digit_list = [int(num_char) for num_char in re.findall(pattern=r"\d", string=email_concat)]
    return sum(digit_list)


def is_valid_local(email: str) -> bool:
    """
    :param email: Potential email with an unchecked local.
    :type email: str
    :return: Bool indicating if the email has a valid local.
    :rtype: bool
    """
    if re.search(pattern=r"[1234]{1}", string=email) is None: # TODO this doesn't enforce only once , this enforces atleast once
        return False

    if re.search(pattern=r"_{1}", string=email) is None: # TODO this doesn't enforce only once , this enforces atleast once
        return False

    return True


def find_emails(leak: str) -> list[str]:
    """
    Finds all emails in leaked internal communication which satisfy staff email conditions.
    
    :param leak: String containing full leak.
    :type leak: str
    :return: List of all staff emails contained in leaked communication.
    :rtype: list[str]
    """

    """
    List of rules for dev
    - local@domain.co.uk
    - all lowercase letters throughout
    - local must contain exactly one underscore and one {1, 2, 3, 4}
    - domain must precisely be lowercase, no special characters, no digits.
    """
    # TODO remove this list of rules.

    pattern = r"[a-z1234_]+@[a-z]+\.co\.uk" # NOTE could possibly make the local tighter before checking
    potential_emails = re.findall(pattern=pattern, string=leak)

    return [email for email in potential_emails if is_valid_local(email=email)]


def main(leaked_email: str) -> None:
    """"""
    staff_emails = find_emails(leak=leaked_email)

    total_valid_emails = len(staff_emails)
    combined_email_length = sum([len(email) for email in staff_emails])
    digit_sum = calc_digit_sum(staff_emails=staff_emails)
    checksum = total_valid_emails * combined_email_length * digit_sum

    print(
        f"""
        Total valid emails: {total_valid_emails},\n
        Combined email length: {combined_email_length},\n
        Sum of digits: {digit_sum},\n
        Checksum: {checksum}
        """
    )


if __name__ == "__main__":
    input_path = r"C:\Users\MilesHoar-Hewitt\Documents\python\python-fundamentals\regex\exercise-1\input.txt"
    with open(input_path, "r") as file:
        raw_input = file.read()
    
    main(leaked_email=raw_input)