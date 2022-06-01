# Course: Python Course
# Section: Data Structures
# Chapter: Sets
# Task Number: 1

try:
    fruits
except NameError:
    print('Variable \"fruits\" not defined', file=sys.stderr)
    sys.exit(0)

if not (fruits == set(['apple', 'banana', 'mango'])):
    print('Please, initialize variable \"fruits\" with set of fruits', file=sys.stderr)
    sys.exit(0)

passed = False
for line in user_code_lines:
    if re.search('\s*print\s*\(\s*fruits\s*\)\s*$', line):
        passed = True

if not passed:
    print("Please, print set of fruits", file=sys.stderr)
    sys.exit(0)

print(json.dumps({ 'token': '{{token}}', 'passed': True }))