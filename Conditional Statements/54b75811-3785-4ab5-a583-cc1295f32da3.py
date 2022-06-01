# Course: Python Course
# Section: Conditional Statements
# Chapter: The if, if-else, and if-elif-else statements
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

try:
    variable_c
except NameError:
    print("Variable \"variable_c\" not defined", file=sys.stderr)
    sys.exit(0)

if not (variable_a == 40 and variable_b == 45):
    print("Please, use provided initial values of variables", file=sys.stderr)
    sys.exit(0)

is_print = False
for line in user_print_lines:
    if line == '40':
        is_print = True

if not is_print:
    print("Wrong value of \"variable_c\"", file=sys.stderr)
    sys.exit(0)

code_string = '\n'.join(user_code_lines)
passed = False
if re.search('(\s*if\s*variable_a\s*(<|>|<=|>=)\s*variable_b\s*)|(\s*if\s*variable_b\s*(<|>|<=|>=)\s*variable_a\s*)', code_string):
    passed = True

if not passed:
    print("Please, code \"if\" statements with comparison", file=sys.stderr)
    sys.exit(0)

if not re.search('\s*else\s*', code_string):
    print("Please, code \"else\" condition", file=sys.stderr)
    sys.exit(0)

is_assing = False
for line in user_code_lines:
    if re.search('\s*variable_c\s*\=\s*variable_a\s*', line):
        is_assing = True

if not is_assing:
    print("Please, assign variable_c smaller number between variable_a and variable_b in \"if\" statement", file=sys.stderr)
    sys.exit(0)

print(json.dumps({ 'token': '{{token}}', 'passed': True }))