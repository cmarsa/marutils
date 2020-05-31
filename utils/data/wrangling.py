# wranling.py
# some utilities or helper functions that I use
# when working with data.
import os
import re
import unicodedata


def strip_accents(text:str) -> str:
    """
    Strip accents from input String.
    
    arguments
    ---------
        text: text to be parsed
    
    returns
    -------
        text: parsed text with accents removed
    """
    try:
        text = unicode(text, 'utf-8')
    except (TypeError, NameError): # unicode is a default on python 3 
        pass
    text = unicodedata.normalize('NFD', text)
    text = text.encode('ascii', 'ignore')
    text = text.decode("utf-8")
    return str(text)



def parse_col_names(colnames_list: list) -> dict:
    """
    Parses the column names to a standard format:
    removes parentheses, slashes and $,
    converts every character to lower case, and converts
    blank spaces to `_`.

    arguments
    ---------
        colnames_list: a list-like structure that haves
            the current names of the columns to be parsed.
    
    returns
    -------
        new_col_names: a dictionary containing the old column names
            and their respective parsed names.
    """
    new_col_names = {key: 0 for key in colnames_list}
    for key, value in new_col_names.items():
        text = strip_accents(key.lower())
        text = re.sub(' - ', '_', text)
        text = re.sub('/[ ]+', '_', text)
        text = re.sub('[ ]-+', '_', text)
        text = re.sub('[. ]+', '_', text)
        text = re.sub('[ ]+', '_', text)
        text = re.sub('[-]+', '_', text)
        text = re.sub('[^0-9a-zA-Z_-]', '', text)

        # assign to dict key the new_col_name
        new_col_names[key] = text
        
    # remove the _ left at the start and/or end of the string
    for key, value in new_col_names.items():
        text = re.sub('^_*|_*$', '', value)
        new_col_names[key] = text
        
    return new_col_names


def split_and_keep(s, sep) -> list:
    '''
    Splits the string according to the specified string `sep`
    preserving the `sep` string in the former or first detachment.
    Returns a list of strings.

    arguments
    ---------
        s: the string to be split up.

        sep: the substring to look for in `s` to separate
        it and preserving `sep` in the first partition. 
    returns
    -------
        a list of strings, product of the separation.
    '''
    if not s:
        return [''] # consistent with string.split()

    # Find replacement character that is not used in string
    # i.e. just use the highest available character plus one
    # Note: This fails if ord(max(s)) = 0x10FFFF (ValueError)
    p = chr(ord(max(s)) + 1) 

    return s.replace(sep, sep + p).split(p)