# Verifying user's email address

import re
# Pattern is always written in string form i.e. " ".
# You can concatenate chunks of patterns using + sign.
# To search dot use back-slash dot.
# Use pipe(|) to search one among options. 
pattern = "[a-zA-Z0-9]+@[a-zA-Z]+\.+(com|in|org|net)"  
# pattern = "harshal" 
 
user_input = input()
out = re.search(pattern, user_input)    # out will be of NoneType if no valid pattern found

print('result: ', out.span())   # Gives the index of [start, end) of the string

print(type(out))        # <class '_sre.SRE_Match'>

if re.search(pattern, user_input):
    print('Valid email address')

else:
    print('Invalid email address')