# Course: Python Course
# Section: Functions
# Chapter: Built-In Function
# Task Number: 2

try:
    germany_capital
except NameError:
    print("Variable \"germany_capital\" not defined", file=sys.stderr)
    sys.exit(0)

if not (germany_capital == 'Berlin'):
    print("Please, don\'t change variable initial value", file=sys.stderr)
    sys.exit(0)

is_len = False
for line in user_code_lines:
    if re.search('\s*length_capital\s*\=\s*len\s*\(\s*germany_capital\s*\)', line):
        is_len = True

if not is_len:
    print("Please, declare the length_capital variable and assign the value of the length of the array via the len function", file=sys.stderr)
    sys.exit(0)

is_print = False
for line in user_code_lines:
    if re.search('\s*print\s*\(\s*.*length_capital\s*\)$', line):
        is_print = True

if not is_print:
    print("Please, print the value of length_capital", file=sys.stderr)
    sys.exit(0)

print(json.dumps({ 'token': '{{token}}', 'passed': True }))