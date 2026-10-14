# Regex Exercise 3

Company pay roll information has been leaked. A list of employee names has been released. You need to identify which employees have had their names leaked.

## Alterations

**Note that:** It's easier to add regex if we mix numbers and letters. This should be proper pattern recognition stuff.

- Append a suffix: `i_love_hacking` + a digit to identify how many times the vowel transformation has been applied
- Vowel transformation: Should this be a vowel transformation mapping. Remember the way that these mappings work in a group theory setting.

Make it so that lots of names have digits in them but not necessarily the `i_love_hacking` string. Also make it so that some names include digits before the `i_love_hacking` string. We want the user to have to find the specific match `r"i_love_hacking(\d)"`.

## Task

1. Identify all relevant entries in list and correctly extract the mapping id
2. Unmap Vowels
3. Remove Suffix
4. Reassemble into a comma separated list of all relevant names in the order which they are found in the leak
5. Hash the answser
6. Extract all integers from hash and concatenate them to make checksum

## Vowel mapping

```
{
    "a": "e",
    "e": "i",
    "i": "a",
    "o": "u",
    "u": "o",
}
```