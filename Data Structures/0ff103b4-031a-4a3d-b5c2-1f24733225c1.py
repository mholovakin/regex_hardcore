# Course: Python Course
# Section: Data Structures
# Chapter: Set Theory Operations
# Task Number: 2

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

try:
    set_C
except NameError:
    print("Variable \"set_C\" not defined", file=sys.stderr)
    sys.exit(0)

if not (set_A == {'a', 'b', 'c', 'd'}, set_B == {'c', 'd', 'e'}, set_C == {'a', 'f'}):
    print("Please, use provided initial values of variables", file=sys.stderr)
    sys.exit(0)

code_string = '\n'.join(user_code_lines)

if not re.search('(\s*union_AB\s*\=\s*set_A\s*.union\s*\(\s*set_B\s*\)\s*)|(\s*union_AB\s*\=\s*set_B\s*.union\s*\(set_A\s*\)\s*)', code_string):
    print("Please, find the union of set_A and set_B and store result in variable set_AB", file=sys.stderr)
    sys.exit(0)

if not re.search('(\s*union_AB\s*\s*.\s*intersection\s*\(\s*set_C\s*\)\s*)|(\s*set_C\s*.\s*intersection\s*\(\s*union_AB\s*\)\s*)', code_string):
    print("Please, find the intersection of union_AB and set_C", file=sys.stderr)
    sys.exit(0)

is_print = False
for line in user_print_lines:
    if re.search('{\'a\'}', line):
        is_print = True

if not is_print:
    print("Please, print the intersection", file=sys.stderr)
    sys.exit(0)

print(json.dumps({ 'token': '{{token}}', 'passed': True }))