# Course: Python Course
# Section: Types and Variables
# Chapter: Strings and String Slicing
# Task Number: 2

try:
    sentence
except NameError:
    print("Variable \"sentence\" not defined", file=sys.stderr)
    sys.exit(0)

try:
    email
except NameError:
    print("Variable \"email\" not defined", file=sys.stderr)
    sys.exit(0)

if sentence != 'My email address is clark786@gmail.com':
    print('Please, use provided initial value of variable', file=sys.stderr)
    sys.exit(0)

is_print = False
for line in user_print_lines:
    if re.search('clark786@gmail.com', line):
        is_print = True

if not is_print:
    print("Please, print the email", file=sys.stderr)
    sys.exit(0)

passed = False
passed_print = False
for line in user_code_lines:
    if re.search('\s*email\s*\=\s*sentence\s*\[\s*20\s*:\s*(38|)\s*\]\s*', line):
        passed = True
    if re.search("\s*print\s*\(\s*email\s*\)\s*", line):
        passed_print = True

if not passed:
    print("Please, set the right slice to email", file=sys.stderr)
    sys.exit(0)

if not passed_print:
    print("Please, print \"email\" value", file=sys.stderr)
    sys.exit(0)

print(json.dumps({ 'token': '{{token}}', 'passed': True }))