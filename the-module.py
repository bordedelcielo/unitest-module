def match(pattern, string):
    """
    Pattern Matching

    Take an input `pattern` and an input `string` and determine if they match. Pattern may use
    the following special characters:

      + = match against 0 or more arbitrary characters
      . = match a single arbitrary character

    """
    i = 0 # string pointer
    j = 0 # pattern pointer
    match = -1 # position of char to find for * search
    start = -1  # position to start searching in * search          
    # Loop over string
    while (i < len(string)):
        # both . and char matching should move forward in the pattern and the string
        if (j < len(pattern) and (pattern[j] == '.' or string[i] == pattern[j])):
            i+=1
            j+=1
        # If * matching then set match/start vars and move forward in the pattern
        elif (j < len(pattern) and pattern[j] == '+'):
            match = i
            start = j
            j+=1
        # if in a * search look at the next letter in the pattern, start looking for the letter in the string
        elif (start != -1):
            j = start + 1
            match+=1
            i = match
        else:
            # Not searching, not a match
            return False
    # if the pattern ended on a * and we are at the end of the string keep reading the pattern
    while (j < len(pattern) and pattern[j] == '+'):
        j+=1
    # if the pattern has been completely read then match success
    return j == len(pattern)