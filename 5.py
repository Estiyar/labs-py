import re
pattern = r'ab*'
text = input("Write здесь: ").split()
for s in text:
    if re.fullmatch(pattern, s):
        print("yes:", s)


import re
pattern = r'ab{2,3}'
text = input("Write здесь: ").split()
for s in text:
    if re.fullmatch(pattern, s):
        print("Matched:", s)


import re
pattern = r'[a-z]+_[a-z]+'
text = input("Write здесь: ").split()
print(re.findall(pattern, text))


import re
pattern = r'[A-Z][a-z]+'
text = input("Write здесь: ").split()
print(re.findall(pattern, text))

import re
pattern = r'a.*b$'
text = input("Write здесь: ").split()
for s in test_strings:
    if re.fullmatch(pattern, s):
        print("Matched:", s)


import re
text = input("Write здесь: ").split()
result = re.sub(r'[ ,.]', ':', text)
print(result)



import re
def snake_to_camel(text):
    parts = text.split('_')
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])

print(snake_to_camel("this_is_snake_case"))


import re
text = input("Write здесь: ").split()
print(re.split(r'(?=[A-Z])', text))


import re
text = input("Write здесь: ").split()
result = re.sub(r'(?=[A-Z])', ' ', text).strip()
print(result)


import re
def camel_to_snake(text):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', text).lower()

print(camel_to_snake("camelCaseToSnakeCase"))
