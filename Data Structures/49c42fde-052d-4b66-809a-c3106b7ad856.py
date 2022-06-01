# Course: Python Course
# Section: Data Structures
# Chapter: Common List Operations
# Task Number: 1

try:
    fruits
except NameError:
    print("Variable \"fruits\" not defined", file=sys.stderr)
    sys.exit(0)

if not (fruits == ["apple", "banana", "cherry"]):
    print("Please, use provided initial value of variable", file=sys.stderr)
    sys.exit(0)

is_print = False
for line in user_print_lines:
    if re.search('banana', line):
        is_print = True

if not is_print:
    print("Please, print the second item in the fruits list", file=sys.stderr)
    sys.exit(0)

passed = False
for line in user_code_lines:
    if re.search('\s*print\s*\(\s*fruits\s*\[\s*1\s*\]\s*\)\s*', line):
        passed = True

if not passed:
    print("Please, choose second index of the list", file=sys.stderr)
    sys.exit(0)

print(json.dumps({ 'token': '{{token}}', 'passed': True }))