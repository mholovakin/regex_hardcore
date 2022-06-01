# Course: Python Course
# Section: Types and Variables
# Chapter: Numbers in Python
# Task Number: 3

try:
    century
except NameError:
    print('Variable \"century\" not defined', file=sys.stderr)
    sys.exit(0)

if century != -21.2:
    print('Wrong number. Please, change the value of variable', file=sys.stderr)
    sys.exit(0)

if not type(century) is float:
    print('Variable type is not float', file=sys.stderr)
    sys.exit(0)

is_print = False
is_print_type = False
for line in user_code_lines:
    if re.search('\s*print\s*\(.*century\s*\)\s*', line):
        is_print = True
    if re.search('\s*print\s*\(.*type\s*\(\s*century\s*\)\s*', line):
        is_print_type = True

if not is_print:
    print("Please, print \"century\" variable", file=sys.stderr)
    sys.exit(0)

if not is_print_type:
    print("Please, print type of \"century\" variable", file=sys.stderr)
    sys.exit(0)

print(json.dumps({ 'token': '{{token}}', 'passed': True }))