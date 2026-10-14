# Exercise 1

As part of the leak, an internal staff communication has been released. The email contains a mix of both staff and customer email addresses. MilesSmiles™ is highly concerned about the exposure of staff emails and wants you to identify every address in the document that belongs to an employee.
Luckily, the company uses a strict corporate standard for employee email addresses, making it possible for you to design a Regular Expression (regex) pattern to detect them. All staff emails must conform to the following rules:

- Format: `local@domain`.
- TLD (Top-Level Domain): Must end exactly with `.co.uk`.
- Casing: Lowercase letters only throughout both the `local` and `domain` parts.
- Local: Must contain exactly one underscore `_`. Must contain exactly one of the following digits: `1`, `2`, `3`, `4`.
- Domain: Must contain only lowercase letters, no digits or special characters.

## Examples
- `j_ohn1doe@example.co.uk`  -----> Valid
- `john1doe@example.co.uk` -----> Invalid (No Underscore)
- `j_ohn1_doe@example.co.uk` -----> Invalid (Two Underscores)
- `j_ohn5doe@example.co.uk` -----> Invalid (Contains Forbidden Digit 5)
- `J_ohn1doe@example.co.uk` -----> Invalid (Uppercase Letter)
- `j_ohn1doe@example.com` -----> Invalid (wrong TLD)

## Task:

Find all valid staff emails in the provided document. To verify your answer, calculate a validation checksum using these three steps:

1. Count the total number of valid staff emails.
2. Calculate the total combined length of all valid email strings (including the local part, `@` symbol, domain, and `.co.uk`).
3. Sum all the single digits contained within those valid emails.

Finally, multiply these three numbers together to get your final checksum
