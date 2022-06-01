# Course: Python Course
# Section: Types and Variables
# Chapter: Arithmetic Operators in Python
# Task Number: 1

try:
    brother_age
except NameError:
    print('Variable\"brother_age\" not defined', file=sys.stderr)
    sys.exit(0)

try:
    sister_age
except NameError:
    print("Variable \"sister_age\" not defined", file=sys.stderr)
    sys.exit(0)

try:
    combine_age
except NameError:
    print("Variable \"combine_age\" not defined", file=sys.stderr)
    sys.exit(0)

if not (brother_age == 15 and sister_age == 17):
    print('Please, use variables initial values', file=sys.stderr)
    sys.exit(0)

if combine_age != 32:
    print("Wrong age. Please, add \"brother_age\" to \"sister_age\".", file=sys.stderr)
    sys.exit(0)

is_print = False
for line in user_print_lines:
    if line == "32":
        is_print = True

if not is_print:
    print("Please, print \"combine_age\" value", file=sys.stderr)
    sys.exit(0)

passed = False
passed_print = False
for line in user_code_lines:
    if re.search('(.*sister_age.*brother_age.*)|(.*brother_age.*sister_age.*)', line):
        passed = True
    if re.search('\s*print\s*\(\s*combine_age\s*\)\s*', line):
        passed_print = True

if not passed:
    print("Please, add \"brother_age\" to \"sister_age\"", file=sys.stderr)
    sys.exit(0)

if not passed_print:
    print("Please, print \"combine_age\" variable", file=sys.stderr)
    sys.exit(0)

print(json.dumps({ 'token': '{{token}}', 'passed': True }))