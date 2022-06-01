# Course: Python Course
# Section: Types and Variables
# Chapter: Logical Operators
# Task Number: 3

try:
    lion_age
except NameError:
    print("Variable \"lion_age\" not defined", file=sys.stderr)
    sys.exit(0)

try:
    giraffe_age
except NameError:
    print("Variable \"giraffe_age\" not defined", file=sys.stderr)
    sys.exit(0)


if not (lion_age == 20 and giraffe_age == 18):
    print('Please, use provided initial values of variables', file=sys.stderr)
    sys.exit(0)

is_print = False
for line in user_print_lines:
    if line == "False":
        is_print = True

if not is_print:
    print("Output must be False only", file=sys.stderr)
    sys.exit(0)


code_string = '\n'.join(user_code_lines)

is_giraffe_lion = False
if re.search('(\s*lion_age\s*(>=|>|<=|<)\s*giraffe_age\s*)|(\s*giraffe_age\s*(>=|>|<=|<)\s*lion_age\s*)', code_string):
    is_giraffe_lion = True

if not is_giraffe_lion:
    print("Please, compare lion_age with giraffe_age", file=sys.stderr)
    sys.exit(0)


passed = False
for line in user_code_lines:
    if re.search('\s*print\s*\(\s*[a-z0-9].*\s*(<|>|<=|>=)\s*[a-z0-9].*', line):
        passed = True

if not passed:
    print("Please, print the result of comparison of \"giraffe_age\" and \"lion_age\" variables", file=sys.stder)
    sys.exit(0)

passed_print = True
for line in user_code_lines:
    if re.match('\s*print\s*\(\s*False\s*\)\s*', line):
        passed_print = False

passed_print_true = True
for line in user_code_lines:
    if re.search("\s*print\s*\(\s*not\s*True\s*\)\s*", line):
        passed_print_true = False

if not passed_print_true:
    print("Please, Please, print the result of comparison of \"giraffe_age\" and \"lion_age\" variables", file=sys.stderr)
    sys.exit(0)

if not passed_print:
    print("Sorry, print(False) does\'t work here :)", file=sys.stderr)
    sys.exit(0)

print(json.dumps({'token': '{{token}}', 'passed': True}))