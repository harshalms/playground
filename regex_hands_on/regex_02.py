# Removing hyphens (-) using re given phone numbers.
# You can such methods to replace somthing in large database

import re

pattern = "(\d\d\d)-(\d\d\d)-(\d\d\d\d)"
new_pattern = r"\1\2\3" # represent the sequence of chunks
user_input = input()
new_user_input = re.sub(pattern, new_pattern, user_input)
print(new_user_input)
