# Course: Python Course
# Section: Types and Variables
# Chapter: Numbers in Python
# Task Number: 2

try:
    century
except NameError:
    print('Variable \"century\" not defined', file=sys.stderr)
    sys.exit(0)

if century != -21:
    print('Wrong number. Please, add minus before value', file=sys.stderr)
    sys.exit(0)

if not type(century) is int:
    print('Variable type is not integer', file=sys.stderr)
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