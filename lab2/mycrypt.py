import codecs

def encode(s):
    if not isinstance(s,str):
        raise TypeError
    origlen = len(s)
    crypted = ""
    digitmapping = dict(zip('1234567890!"#€%&/()=','!"#€%&/()=1234567890'))
    invalid_char = ["+", "ä", "ö", "å"]
    if len(s) > 1000:
        raise ValueError
    else:
        s = s.ljust(1000, "x")
        

    for c in s:
        for i in invalid_char:      #check in valid_char [+, ä, ö, å]  
            if c == i:
                raise ValueError

        if c.isalpha():
            if c.islower():
                c=c.upper()
            # Rot13 the character for maximum security
            crypted+=codecs.encode(c,'rot13')
        
        elif c in digitmapping:
          crypted+=digitmapping[c]
        
        else:
            raise ValueError
    return crypted[0:origlen]
    
def decode(s):
    decoded_value = ""
    digitmapping = dict(zip('1234567890!"#€%&/()=','!"#€%&/()=1234567890'))
    for c in s:
        if c.isalpha():
            if c.isupper():
                decoded_value+=codecs.decode(c,'rot13').lower()
        elif c in digitmapping:
            decoded_value+=digitmapping[c]
    return decoded_value
