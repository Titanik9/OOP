import re

pattern = "I want Audi"

detect = r"Audi"
new_var = r"Volkswagen Polo"

newstr = re.sub(detect, new_var, pattern)

print(newstr)
