# Course: Python Course
# Section: Types and Variables
# Chapter: Logical Operators
# Task Number: 4

try:
    lion_age
except NameError:
    print("Variable \"lion_age\" not defined", file=sys.stderr)
    sys.exit(0)

try:
    giraffe_age
except NameError:
    print("Variable \"giraffe_age\" not defined", file=sys.stderr)
    sys.exit(0)

if not (lion_age == 20 and giraffe_age == 18):
    print('Please, use provided initial values of variables', file=sys.stderr)
    sys.exit(0)

passed = False
for line in user_code_lines:
    if re.match('\s*print\s*\(\s*not\s*lion_age\s*<\s*giraffe_age\)\s*', line):
        passed = True

if not passed:
    print("Please, add \"not\" before comparison", file=sys.stderr)
    sys.exit(0)

is_print = False
for line in user_print_lines:
    if line == "True":
        is_print = True

if not is_print:
    print("Output must be True only", file=sys.stderr)
    sys.exit(0)

print(json.dumps({'token': '{{token}}', 'passed': True}))