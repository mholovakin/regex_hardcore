# Course: Python Course
# Section: Types and Variables
# Chapter: Comparison Operators
# Task Number: 2

try:
    my_grade
except NameError:
    print("Variable \"my_grade\" not defined", file=sys.stderr)
    sys.exit(0)

try:
    sister_grade
except NameError:
    print("Variable \"sister_grade\" not defined", file=sys.stderr)
    sys.exit(0)

if not (my_grade == 8 and sister_grade == 8):
    print("Please, don\'t change variables initial value", file=sys.stderr)
    sys.exit(0)

is_print = False
for line in user_print_lines:
    if line == 'True':
        is_print = True

if not is_print:
    print("Please, print comparison of two variables with \"True\" value", file=sys.stderr)
    sys.exit(0)

passed = False
for line in user_code_lines:
    if re.match('\s*print\s*\(\s*my_grade\s*\=\=\s*sister_grade\s*\)\s*', line):
        passed = True

if not passed:
    print("Please, check variables \"my_grade\" and \"sister_grade\" on equality", file=sys.stderr)
    sys.exit(0)

print(json.dumps({ 'token': '{{token}}', 'passed': True }))