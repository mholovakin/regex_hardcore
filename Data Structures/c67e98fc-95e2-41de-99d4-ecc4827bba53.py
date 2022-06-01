# Course: Python Course
# Section: Data Structures
# Chapter: Common List Operations
# Task Number: 2

try:
    my_list
except NameError:
    print("Variable \"my_list\" not defined", file=sys.stderr)
    sys.exit(0)

try:
    copy_my_list
except NameError:
    print("Variable \"copy_my_list\" not defined", file=sys.stderr)
    sys.exit(0)

if not (my_list == [11,22,33,44,55,66,77,88,99] and copy_my_list == [11,22,33,44,55,66,77,88,99]):
    print("Please, use provided initial values of variables", file=sys.stderr)
    sys.exit(0)

is_print = False
for line in user_print_lines:
    if len(my_list) == len(copy_my_list):
        if re.search('Equal', line):
            is_print = True
    else:
        if re.search('Not Equal', line):
            is_print = True

if not is_print:
    print("Please, print \"Equal\" or \"Not Equal\"", file=sys.stderr)
    sys.exit(0)

passed = False
for line in user_code_lines:
    if re.search('(\s*if\s*len\s*\(\s*my_list\s*\)\s*\s(\=\=|\!\=)\s*len\s*\(\s*copy_my_list\s*\))|(\s*if\s*len\s*\(\s*copy_my_list\s*\)\s*\s(\=\=|\!\=)\s*len\s*\(\s*my_list\s*\))', line):
        passed = True

if not passed:
    print("Please, compare length of lists", file=sys.stderr)
    sys.exit(0)

print(json.dumps({ 'token': '{{token}}', 'passed': True }))