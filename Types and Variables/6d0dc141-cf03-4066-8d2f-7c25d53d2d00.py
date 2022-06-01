# Course: Python Course
# Section: Types and Variables
# Chapter: Numbers in Python
# Task Number: 1

try:
    century
except NameError:
    print('Variable \"century\" not defined', file=sys.stderr)
    sys.exit(0)

if century != 21:
    print('Please, use provided initial value of variable', file=sys.stderr)
    sys.exit(0)

if not type(century) is int:
    print('Please, create integer variable \"century\"', file=sys.stderr)
    sys.exit(0)

is_print = False
is_print_type = False
for line in user_print_lines:
    if re.search("21", line):
        is_print = True
    if re.search('\s*<class \'int\'>\s*', line):
        is_print_type = True

if not is_print:
    print("Please, print \"century\" value", file=sys.stderr)
    sys.exit(0)

if not is_print_type:
    print("Please, print type of \"century\"", file=sys.stderr)
    sys.exit(0)

flag = False
for line in user_code_lines:
    if re.search('\s*print\s*\(.*century\s*\)\s*', line):
        flag = True

if not flag:
    print("Please, print \"century\" variable", file=sys.stderr)
    sys.exit(0)

types = False
for line in user_code_lines:
    if re.search('\s*type\s*\(century\s*\)\s*', line):
        types = True

if not types:
    print("Please, print type of \"century\" variable", file=sys.stderr)
    sys.exit(0)



print(json.dumps({ 'token': '{{token}}', 'passed': True }))