import codecs

def encode(s):
    if not isinstance(s,str):
        raise TypeError
    origlen = len(s)
    crypted = ""
    digitmapping = dict(zip('1234567890!"#€%&/()=','!"#€%&/()=1234567890'))
    if len(s) > 1000:
        raise ValueError
    #Lisätään merkkejä kunnes 1001 täyttyy.
    #Valittiin 1001, jotta saataisiin ohjelman käymään yhtä monta koodiriviä
    #inputista välittämättä, jolloin aika pysyisi melkein samana.
    s = s.ljust(1001, "a")
    #Poistetaan yksi merkki pois, jotta saataisiin 1000.
    s = s[:-1]
    for c in s:
        if ord(c) >= 0 and ord(c) <= 127: #Tarkistaa ettei tule ääkkösiä
            if c.isalpha():
                if c.islower():
                    c=c.upper()
                # Rot13 the character for maximum security
                crypted+=codecs.encode(c,'rot13')
            elif c in digitmapping:
              crypted+=digitmapping[c]
            #Lisäsin else lauseen, mahdollisten virheellisten syöttöjen takia
            else:
                raise ValueError
        else:
            raise ValueError
    return crypted[:origlen]

def decode(s):
    return encode(s).lower()