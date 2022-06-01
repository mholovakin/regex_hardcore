# Course: Python Course
# Section: Data Structures
# Chapter: Set Theory Operations
# Task Number: 1

try:
    set_A
except NameError:
    print("Variable \"set_A\" not defined", file=sys.stderr)
    sys.exit(0)

try:
    set_B
except NameError:
    print("Variable \"set_B\" not defined", file=sys.stderr)
    sys.exit(0)

if not (set_A == {3, 5, 7, 9}, set_B == {2, 4, 6, 8}):
    print("Please, use provided initial values of variables", file=sys.stderr)
    sys.exit(0)

code_string = '\n'.join(user_code_lines)
if not re.search('\s*print\(\s*set_B\s*((\.difference\s*\(\s*set_A\s*)|\-\s*set_A\s*)\s*', code_string):
    print("Please, use subtraction of variables", file=sys.stderr)
    sys.exit(0)

is_print = False
for line in user_print_lines:
    if re.search('\s*\{8, 2\}\s*', line):
        is_print = True

if not is_print:
    print("Please, print elements, that are in set_B but not in set_A", file=sys.stderr)
    sys.exit(0)


print(json.dumps({ 'token': '{{token}}', 'passed': True }))