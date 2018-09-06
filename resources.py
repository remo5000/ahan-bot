import re

# Hardcoding triggers and responses.
# Tech related
tech_buzzwords = re.compile(r"\bar\b|\bvr\b|\bblock[\s]*chain[sz]*\b|\bcrypto\b|\bmachine[\s]*learning\b|\bcloud\b|\bHD\b",
                            flags=re.IGNORECASE | re.MULTILINE)
tech_buzzwords_reply = ["AR VR BLOCKCHAIN CRYTO CLOUD MACHINE LEARNING HHHHHHHHHD PORRRRNNNNNN!!!!!"]

# Generic Ahan
triggers = re.compile(r"\bstfu\b.*\bahan\b|\bfuck\b.*\bahan\b",
                      flags=re.IGNORECASE | re.MULTILINE)
trigger_replies = ["dohohohoooont be a fucker lah OUI", "LULZ", "fk youuuu LULZ jk luv <3", "thx bb xoxo", "BODOH LA U",
                   "YEEHEEEEEE", "thenkz hon <3", "Thenkz man <3"]

# Food / Ameens
food_words = re.compile(r"\bsupper\b|\ba+m+e+n+[sz]*\b|\bmacs+\b|\bchee+se[\s]*fries+\b|\border(ing)?\b|\bma+la+\b", flags=re.IGNORECASE | re.MULTILINE)
food_replies = ["so ameens???", "you noe what time it is right", "save some cheese fries for me plez <333",
                "CHEEEESE FRIES", "now we HAVE to order", "fuck that, anyone wnna eat some MALA???"]

greetings = re.compile(r'''\b h+[e]*[l]*[o]*[\s] ahan \b
                         | \b ahan bot \b
                         | \b h[e]*[y]* [\s]* ahan \b
                         | \b wass+up [\s]* ahan \b''', 
                         flags=re.IGNORECASE | re.MULTILINE | re.VERBOSE)
greetings_replies = ["masai bruv, masai", "yess bb? <<3", "WWAAPP", "masai gents"]
