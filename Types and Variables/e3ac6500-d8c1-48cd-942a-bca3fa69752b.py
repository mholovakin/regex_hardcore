# Course: Python Course
# Section: Types and Variables
# Chapter: Data Type Conversion In Python
# Task Number: 1

try:
    variable_1
except NameError:
    print('Variable \"variable_1\" not defined', file=sys.stderr)
    sys.exit(0)

try:
    variable_2
except NameError:
    print("Variable \"variable_2\" not defined", file=sys.stderr)
    sys.exit(0)

try:
    total
except NameError:
    print('Variable \"total\" not defined', file=sys.stderr)
    sys.exit(0)


if not (variable_1 == '78' and variable_2 == '156'):
    print('Please, use provided initial values of variables', file=sys.stderr)
    sys.exit(0)

if not type(total) is int:
    print("Variable \"total\" must be integer", file=sys.stderr)
    sys.exit(0)

is_string = False
is_print = False
for line in user_print_lines:
    if re.search('78156', line):
        is_string = True
    if re.search('234', line):
        is_print = True

if is_string:
    print("Check the data type of variables", file=sys.stderr)
    sys.exit(0)

if not is_print:
    print('Please, output the value of \"total\" variable', file=sys.stderr)
    sys.exit(0)

passed = False
for line in user_code_lines:
    if re.search('\s*total\s*\=\s*int\s*\(\s*variable_1\s*\)\s*\+\s*int\s*\(\s*variable_2\s*\)\s*', line):
        passed = True

if not passed:
    print('Please, add integer \"variable_1\" to integer \"variable_2\"', file=sys.stderr)
    sys.exit(0)

print(json.dumps({ 'token': '{{token}}', 'passed': True }))