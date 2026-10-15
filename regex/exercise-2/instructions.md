# Exercise 2

Oh no! Another massive leak has occurred. This time, a raw text file containing un-hashed credit card numbers has been released online. Among the leaked data are several corporate credit carts belonging to MilesSmiles™. The company needs you to identify these cards immediately as the leak has already resulted in company losses of well over €20.
Once again, you're in luck. MilesSmiles™ corporate cards follow a strict issuing pattern making this a perfect situation for you to utilise your regex skills. Every valid company card must abide by the following rules:

- Length: Must be exactly 9-digits long.
- Prefix: Must begin with `1357`.
- Suffix: Must end with a 5-digit palindrome i.e `12321`, `88888`, or `41014`.


## Examples

- `135778087` -----> Valid
- `135711111` -----> Valid
- `135746884` -----> Invalid (The last five digits, `46884`, do not form a palindrome)
- `635712321` -----> Invalid (Does not begin with `1357`)

## Task:

Find all valid company cards in the comma separated input file below. To verify your answer, calculate a final validation checksum using these two steps:

1. For each valid card number, multiply its full numerical value by its 0-indexed position in the comma separated list.
2. Sum all these products to compute final checksum
