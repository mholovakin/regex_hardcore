# Course: Python Course
# Section: Types and Variables
# Chapter: Bitwise Operators
# Task Number: 1

try:
    value_1
except NameError:
    print("Variable \"value_1\" not defined", file=sys.stderr)
    sys.exit(0)

try:
    value_2
except NameError:
    print('Variable \"value_2\" not defined', file=sys.stderr)
    sys.exit(0)

try:
    value_3
except NameError:
    print("Variable \"value_3\" not defined", file=sys.stderr)
    sys.exit(0)

if not (value_1 == 6 and value_2 == 45 and value_3 == 90):
    print("Please, use provided initial values of variables", file=sys.stderr)
    sys.exit(0)

print_string = '\n'.join(user_print_lines)

if not re.match('\s*0b110\s*.*0b101101\s*.*0b1011010\s*', print_string):
    print("Please, print binary numbers of variables using \"bin\" operator", file=sys.stderr)
    sys.exit(0)

counter = 0
for line in user_code_lines:
    if re.search('\s*print\s*\(\s*bin\s*\(\s*value_(1|2|3)\s*\)\s*\)\s*', line):
        counter = counter + 1

if counter != 3:
    print('Please, print all binary numbers of variables using \"bin\" operator', file=sys.stderr)
    sys.exit(0)

print(json.dumps({'token': '{{token}}', 'passed': True}))