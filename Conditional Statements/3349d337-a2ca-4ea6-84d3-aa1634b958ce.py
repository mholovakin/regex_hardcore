# Course: Python Course
# Section: Conditional Statements
# Chapter: The if, if-else, and if-elif-else statements
# Task Number: 1

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

if not (variable_a == 55 and variable_b == 125):
    print("Please, use provided initial values of variables", file=sys.stderr)
    sys.exit(0)

is_print = False
for line in user_print_lines:
    if re.search("Hello (w|W)orld", line):
        is_print = True

if not is_print:
    print("Please, print \"Hello world\" if variable_b is greater than variable_a", file=sys.stderr)
    sys.exit(0)

passed = False
for line in user_code_lines:
    if re.search('\s*if\s*variable_b\s*>\s*variable_a\s*', line):
        passed = True

if not passed:
    print("Please, code comparison between variable_b and variable_a in \"if\" statement", file=sys.stderr)
    sys.exit(0)

print(json.dumps({ 'token': '{{token}}', 'passed': True }))