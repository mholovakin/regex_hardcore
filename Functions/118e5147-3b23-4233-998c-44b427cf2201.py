# Course: Python Course
# Section: Functions
# Chapter: Built-In Function
# Task Number: 1

try:
    numbers_list
except NameError:
    print("Variable \"numbers_list\" not defined", file=sys.stderr)
    sys.exit(0)

try:
    maximum
except NameError:
    print("Variable \"maximum\" not defined", file=sys.stderr)
    sys.exit(0)

if not (numbers_list == [5,11,20,3,48,74,10,35]):
    print("Please, don\'t change initial variable value", file=sys.stderr)
    sys.exit(0)

is_print = False
for line in user_print_lines:
    if "74" in line:
        is_print = True

if not is_print:
    print("Please, print the value of maximum variable", file=sys.stderr)
    sys.exit(0)

is_max = False
code_print = False
for line in user_code_lines:
    if re.search('\s*maximum\s*\=\s*max\s*\(\s*numbers_list\s*\)\s*', line):
        is_max = True
    if re.search("\s*print\s*\(.*maximum\)\s*", line):
        code_print = True

if not code_print:
    print("Please, print the \"maximum\" variable", file=sys.stderr)
    sys.exit(0)

if not is_max:
    print("Please, declare the maximum variable and assign the value of the maximum element of the array via the max function", file=sys.stderr)
    sys.exit(0)


print(json.dumps({ 'token': '{{token}}', 'passed': True }))