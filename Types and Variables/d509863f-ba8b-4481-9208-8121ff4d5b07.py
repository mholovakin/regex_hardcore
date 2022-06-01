# Course: Python Course
# Section: Types and Variables
# Chapter: Logical Operators
# Task Number: 2

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

try:
    elephant_age
except NameError:
    print("Variable \"elephant_age\" not defined", file=sys.stderr)
    sys.exit(0)


if not (lion_age == 20 and giraffe_age == 18 and elephant_age == 32):
    print("Please, use provided initial values of variables", file=sys.stderr)
    sys.exit(0)

is_print = False
if user_print_lines == ["False"]:
    is_print = True

if not is_print:
    print("Output must be False only", file=sys.stderr)
    sys.exit(0)


code_string = '\n'.join(user_code_lines)

is_elephant_lion = False
if re.search('(\s*lion_age\s*(>=|>|<=|<)\s*elephant_age)|(\s*elephant_age\s*(>=|>|<=|<)\s*lion_age\s*)', code_string):
    is_elephant_lion = True

is_elephant_giraffe = False
if re.search('(\s*elephant_age\s*(>=|>|<=|<)\s*giraffe_age)|(\s*giraffe_age\s*(>=|>|<=|<)\s*elephant_age\s*)', code_string):
    is_elephant_giraffe = True

if not (is_elephant_lion and is_elephant_giraffe):
    print("Please, compare lion_age with elephant_age and giraffe_age with elephant_age", file=sys.stderr)
    sys.exit(0)

passed = False
for line in user_code_lines:
    if re.search('\s*print\s*\([a-z0-9><=].*\s*or\s*[a-z0-9<>=].*$', line):
        passed = True

if not passed:
    print("Please, print the comparison of variables with \"or\" operator", file=sys.stderr)
    sys.exit(0)

passed_print = True
for line in user_code_lines:
    if re.match('\s*print\s*\(\s*False\s*\)\s*$', line):
        passed_print = False

if not passed_print:
    print("Please, compare lion_age with elephant_age and giraffe_age with elephant_age", file=sys.stderr)
    sys.exit(0)

print(json.dumps({'token': '{{token}}', 'passed': True}))