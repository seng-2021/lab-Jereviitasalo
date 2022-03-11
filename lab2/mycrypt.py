import codecs

def encode(s):
    if not isinstance(s,str):
        raise TypeError
    origlen = len(s)
    crypted = ""
    digitmapping = dict(zip('1234567890!"#€%&/()=','!"#€%&/()=1234567890'))
    if len(s) > 1000:
        raise ValueError
    #Added characters to 1001, so if the input is 1000 it still has to go trough
    #as many lines of code than the input that has less than 1000
    #so the time is independent of the input.
    s = s.ljust(1001, 'a')
    #Remove 1 character to get 1000.
    s = s[:-1]
    for c in s:
        #Checks if there is non-ascii characters
        if ord(c) >= 0 and ord(c) <= 127:
            if c.isalpha():
                if c.islower():
                    c=c.upper()
                # Rot13 the character for maximum security
                crypted+=codecs.encode(c,'rot13')
            elif c in digitmapping:
              crypted+=digitmapping[c]
            #Added else statement for possible invalid inputs
            else:
                raise ValueError
        else:
            raise ValueError
    #Changes return value back to original length
    return crypted[:origlen]

def decode(s):
    return encode(s).lower()