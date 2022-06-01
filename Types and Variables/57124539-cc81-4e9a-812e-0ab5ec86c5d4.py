# Course: Python Course
# Section: Types and Variables
# Chapter: String Special Operations
# Task Number: 1

try:
    variable_1
except NameError:
    print("Variable \"variable_1\" not defined", file=sys.stderr)
    sys.exit(0)

try:
    variable_2
except NameError:
    print("Variable \"variable_2\" not defined", file=sys.stderr)
    sys.exit(0)

try:
    variable_3
except NameError:
    print("Variable \"variable_3\" not defined", file=sys.stderr)
    sys.exit(0)

try:
    variable_4
except NameError:
    print("Variable \"variable_4\" not defined", file=sys.stderr)
    sys.exit(0)

try:
    variable_5
except NameError:
    print("Variable \"variable_5\" not defined", file=sys.stderr)
    sys.exit(0)

if not (variable_1 == 'easy ' and variable_2 == 'learn.' and variable_3 == 'Python ' and variable_4 == 'to ' and variable_5 == 'is '):
    print("Please, use provided initial values of variables", file=sys.stderr)
    sys.exit(0)


code_string = '\n'.join(user_code_lines)
passed = False
if re.search('\s*variable_3\s*\+\s*variable_5\s*\+\s*variable_1\s*\+\s*variable_4\s*\+\s*variable_2\s*', code_string):
    passed = True

if not passed:
    print("Please, print the variables using \'+\' operator in the correct order", file=sys.stderr)
    sys.exit(0)

is_print = False
for line in user_print_lines:
    if line == 'Python is easy to learn.':
        is_print = True

if not is_print:
    print("Output must be \"Python is easy to learn.\"", file=sys.stderr)
    sys.exit(0)

print(json.dumps({'token': '{{token}}', 'passed': True}))
