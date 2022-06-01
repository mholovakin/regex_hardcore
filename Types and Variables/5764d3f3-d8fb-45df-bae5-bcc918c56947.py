# Course: Python Course
# Section: Types and Variables
# Chapter: Strings and String Slicing
# Task Number: 1

try:
    full_name
except NameError:
    print("Variable \"full_name\" not defined", file=sys.stderr)
    sys.exit(0)

if full_name != "Michael Clarke":
    print('Please, use provided initial value of variable', file=sys.stderr)
    sys.exit(0)

is_print = False
for line in user_print_lines:
    if re.search('Michael', line):
        is_print = True

if not is_print:
    print("Please, print the name using right indices", file=sys.stderr)
    sys.exit(0)

passed = False
for line in user_code_lines:
    if re.search('\s*print\s*\(\s*full_name\s*\[\s*(0|)\s*:\s*7\s*\]\s*\)\s*', line):
        passed = True

if not passed:
    print('Please, use right indices to print the name', file=sys.stderr)
    sys.exit(0)

print(json.dumps({ 'token': '{{token}}', 'passed': True }))