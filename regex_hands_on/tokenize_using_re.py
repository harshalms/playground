import re
pattern = "[\S]"
string = "Hi my name is Harshal! I'm working in Bengluru."
# mat = re.match(pattern, string)
# print(mat.group())

tokens = string.split()
print(tokens)