# Course: Python Course
# Section: Functions
# Chapter: Function Creation
# Task Number: 2

try:
    variable_a
except NameError:
    print("Variable \"variable_a\" not defined", file=sys.stderr)
    sys.exit(0)

try:
    variable_b
except NameError:
    print("Variable \"variable_b\" not defined", file=sys.stderr)
    sys.exit(0)

if not (variable_a == 5 and variable_b == 10):
    print("Please, use provided initial values of variables", file=sys.stderr)
    sys.exit(0)

code_string = '\n'.join(user_code_lines)
is_def = False
if re.search('\s*def\s*compare\s*\(\s*value_1\s*,\s*value_2\s*\):', code_string):
    is_def = True

if not is_def:
    print("Please, don't change function declaration", file=sys.stderr)
    sys.exit(0)

counter = 0
for line in user_code_lines:
    if re.search('if\s*(\s*.*value_1\s*>\s*value_2\s*|.*value_2\s*>\s*value_1\s*)', line):
        counter = counter + 1

if counter < 1:
    print("Please, compare two variables and return the largest one", file=sys.stderr)
    sys.exit(0)

is_ret_value_1 = False
is_ret_value_2 = False

if re.search('\s*return\s*\(\s*value_1\s*\)\s*', code_string):
    is_ret_value_1 = True
if re.search('\s*return\s*\(\s*value_2\s*\)\s*', code_string):
    is_ret_value_2 = True

if not (is_ret_value_1 and is_ret_value_2):
    print("Please, return value_1 or value_2", file=sys.stderr)
    sys.exit(0)

is_print = False
if re.search('\s*print\s*\(\s*compare\s*\(\s*variable_a\s*,\s*variable_b\s*\)\s*\)\s*', code_string):
    is_print = True

if not is_print:
    print("Please, call your function in \"print\" function", file=sys.stderr)
    sys.exit(0)

print(json.dumps({ 'token': '{{token}}', 'passed': True }))
