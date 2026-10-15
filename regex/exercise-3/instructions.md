# Exercise 3

The situation has escalated. It appears that hackers have gained access to MilesSmiles™ internal systems and maliciously corrupted a comma separated list of all active employee names. Payday is rapidly approaching, and dissent is spreading among the ranks of MilesSmiles™ employees.
Fortunately, a crack team of MilesSmiles™ code breakers have reverse engineered exactly how the hackers' script altered the data. Crucially, the hackers script only successfully modified some of the names in the list. Where it did execute it applied two specific modifications:

- Appended Suffix: The literal string `_i_love_hacking` has been added to the very end of every name.
- Vowel Cipher: All vowels (`a`, `e`, `i`, `o`, `u`) have been swapped according to the following cipher mapping
    - `a` ----> `i`
    - `e` ----> `o`
    - `i` ----> `a`
    - `o` ----> `u`
    - `u` ----> `e`

## Example:

- `liam rhiordan` -----> `laim raurdin_i_love_hacking`
- `natthaya watthanamassakul` -----> `nitthiyi witthinimissikel_i_love_hacking`

## Task:

1. Identify: Use a regex pattern to scan the payroll document and identify names which have been altered by the hackers.
2. Restore: Reverse the changes by removing the suffix and decoding the vowels back to their original state.
3. Verify: Finally convert the list of names into a single string, hash it using ... and compare your result against the solutions answer.
