# Course: Python Course
# Section: Types and Variables
# Chapter: Booleans
# Task Number: 3

try:
    checking
except NameError:
    print("Variable \"checking\" not defined", file=sys.stderr)
    sys.exit(0)

if checking != False:
    print("Wrong variable value. Please, change the value", file=sys.stderr)
    sys.exit(0)

is_print = False
for line in user_print_lines:
    if line == 'False':
        is_print = True

if not is_print:
    print('Please, print the value of the variable', file=sys.stderr)
    sys.exit(0)

passed = False
for line in user_code_lines:
    if re.match('\s*print\s*\(\s*checking\s*\)\s*$', line):
        passed = True

if not passed:
    print("Please, print variable", file=sys.stderr)
    sys.exit(0)

print(json.dumps({ 'token': '{{token}}', 'passed': True }))