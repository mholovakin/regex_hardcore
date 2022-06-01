# Course: Python Course
# Section: Types and Variables
# Chapter: Arithmetic Operators in Python
# Task Number: 2

try:
    a
    b
    a_squared
    b_squared
    c_squared
except NameError:
    print("Variables are not defined", file=sys.stderr)
    sys.exit(0)

if a != 5 and b != 3:
    print("Please, use variables initial value", file=sys.stderr)
    sys.exit(0)

if a_squared != 25 and b_squared != 9:
    print("Wrong squared values of variables", file=sys.stderr)
    sys.exit(0)

if c_squared != 34:
    print("Wrong value of \"c_squared\"", file=sys.stderr)
    sys.exit(0)

is_print = False
for line in user_print_lines:
    if line == '34':
        is_print = True

if not is_print:
    print("Please, print value of \"c_squared\" variable", file=sys.stderr)
    sys.exit(0)

passed = False
for line in user_code_lines:
    if re.match('\s*print\s*\(\s*c_squared\s*\)\s*$', line):
        passed = True

if not passed:
    print("Please, don't change \"print\" argument", file=sys.stderr)
    sys.exit(0)

print(json.dumps({ 'token': '{{token}}', 'passed': True }))