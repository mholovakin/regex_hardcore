# Course: Python Course
# Section: Types and Variables
# Chapter: Data Type Conversion In Python
# Task Number: 2

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
    total
except NameError:
    print('Variable \"total\" not defined', file=sys.stderr)
    sys.exit(0)

try:
    new_total
except NameError:
    print("Variable \"new_total\" not defined", file=sys.stderr)
    sys.exit(0)

if not (variable_1 == '78' and variable_2 == '156' and total == 234):
    print('Please, use variables initial values', file=sys.stderr)
    sys.exit(0)

is_print_one = False
is_print_two = False
for line in user_print_lines:
    if re.search('384.55', line):
        is_print_one = True
    if re.search('<class \'float\'>', line):
        is_print_two = True

if not (is_print_one and is_print_two):
    print('Please, output the value of \"new_total\" variable and it\'s type', file=sys.stderr)
    sys.exit(0)

passed_add = False
passed_print_one = False
passed_print_two = False
for line in user_code_lines:
    if re.search('\s*new_total\s*\=\s*(\s*total\s*\+\s*150.55\s*|\s*150.55\s*\+\s*total\s*)\s*', line):
        passed_add = True
    if re.search('\s*print\s*\(\s*new_total\s*\)\s*', line):
        passed_print_one = True
    if re.search('\s*print\s*\(\s*type\s*\(\s*new_total\s*\)\s*\)\s*', line):
        passed_print_two = True

if not passed_add:
    print("Please, add 150.55 to \"total\" variable", file=sys.stderr)
    sys.exit(0)

if not passed_print_one:
    print("Please, print \"new_total\" variable", file=sys.stderr)
    sys.exit(0)

if not passed_print_two:
    print("Please, print type of \"new_total\" variable", file=sys.stderr)
    sys.exit(0)

passed = False
if new_total == 384.55:
    passed = True

if not passed:
    print('Wrong value of \"new_total\" variable', file=sys.stderr)
    sys.exit(0)

print(json.dumps({ 'token': '{{token}}', 'passed': True }))