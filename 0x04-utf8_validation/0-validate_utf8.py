#!/usr/bin/python3
"""UTF-8 validation module.
"""


def validUTF8(data):
    """Checks if a list of integers are valid UTF-8 codepoints.
    """
    def is_trailing_byte(byte):
        """Checks if a byte is a valid trailing byte (10xxxxxx) in UTF-8 encoding."""
        return (byte & 0b11000000) == 0b10000000

    n = len(data)
    i = 0
    while i < n:
        byte = data[i]
        
        if byte <= 0x7F:
            i += 1
            continue
        
        if (byte & 0b11111000) == 0b11110000:  
            span = 4
        elif (byte & 0b11110000) == 0b11100000: 
            span = 3
        elif (byte & 0b11100000) == 0b11000000:  
            span = 2
        else:
            return False  

        if i + span > n:
            return False
        
        for j in range(1, span):
            if not is_trailing_byte(data[i + j]):
                return False
        
        i += span

    return True