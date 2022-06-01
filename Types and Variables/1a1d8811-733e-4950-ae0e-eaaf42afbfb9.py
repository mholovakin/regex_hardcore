# Course: Python Course
# Section: Types and Variables
# Chapter: Strings and String Slicing
# Task Number: 3

try:
    information
except NameError:
    print('Variable \"information\" not defined', file=sys.stderr)
    sys.exit(0)

try:
    skype
except NameError:
    print("Variable \"skype\" not defined", file=sys.stderr)
    sys.exit(0)

if information != 'Phone number = +90 12345678. Email = asdf123@yahoo.com. Skype ID = qwerty456':
    print('Please, use variable initial value', file=sys.stderr)
    sys.exit(0)

is_print = False
for line in user_print_lines:
    if line == 'Skype ID: qwerty456':
        is_print = True

if not is_print:
    print("Please, print skype ID", file=sys.stderr)
    sys.exit(0)

passed = False
passed_print = False
for line in user_code_lines:
    if re.search('\s*skype\s*\=\s*information\s*\[\s*-\s*9\s*:\s*\]\s*', line):
        passed = True
    if re.search('\s*print\s*\(.*skype\s*\)\s*', line):
        passed_print = True

if not passed:
    print("Please, set the right slice to skype ID", file=sys.stderr)
    sys.exit(0)

if not passed_print:
    print("Please, print \"skype\" variable", file=sys.stderr)
    sys.exit(0)

print(json.dumps({ 'token': '{{token}}', 'passed': True }))