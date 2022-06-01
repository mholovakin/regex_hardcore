# Course: Python Course
# Section: Types and Variables
# Chapter: Bitwise Operators
# Task Number: 3

try:
    binary_number
except NameError:
    print("Variable \"binary_number\" not defined", file=sys.stderr)
    sys.exit(0)

try:
    mask
except NameError:
    print("Variable \"mask\" not defined", file=sys.stderr)
    sys.exit(0)

try:
    flipped
except NameError:
    print("Variable \"flipped\" not defined", file=sys.stderr)
    sys.exit(0)

if not (binary_number == 0b00111011 and mask == 0b11111111):
    print('Please, use provided initial values of variables', file=sys.stderr)
    sys.exit(0)

is_print = False
for line in user_print_lines:
    if line == '0b11000100':
        is_print = True

if not is_print:
    print("Please, print binary flipped variable using \"bin\" operator", file=sys.stderr)
    sys.exit(0)

passed = False
for line in user_code_lines:
    if re.search('\s*flipped\s*\=\s*((\s*binary_number\s*\^\s*mask\s*)|(\s*mask\s*\^\s*binary_number\s*))\s*', line):
        passed = True

if not passed:
    print("Please, use \"XOR\" operator to flip bits", file=sys.stderr)
    sys.exit(0)

print(json.dumps({'token': '{{token}}', 'passed': True}))