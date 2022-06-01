# Course: Python Course
# Section: Conditional Statements
# Chapter: Nested if Conditions
# Task Number: 2

try:
    age
except NameError:
    print("Variable \"age\" not defined", file=sys.stderr)
    sys.exit(0)

try:
    have_CNIC
except NameError:
    print("Variable \"have_CNIC\" not defined", file=sys.stderr)
    sys.exit(0)

is_print = False
for line in user_print_lines:
    if age >= 18:
        if have_CNIC == True:
            if re.search('Congrats! You can cast your vote', line):
                is_print = True
        else:
            if re.search('You cannot cast your vote', line):
                is_print = True
    else:
        if re.search('You cannot cast your vote', line):
            is_print = True

if not is_print:
    print("Please, print lines which are indicated in the task, using \"if-else\" statements", file=sys.stderr)
    sys.exit(0)

age_passed = False
CNIC_passed = False
for line in user_code_lines:
    if re.search('\s*age\s*>=\s*18\s*', line):
        age_passed = True
    if re.search('\s*have_CNIC\s*(\=\=|\!\=)\s*(True|False)\s*', line):
        CNIC_passed = True

if not age_passed:
    print("Please, code expression \"age greater than equal to 18\"", file=sys.stderr)
    sys.exit(0)

if not CNIC_passed:
    print('Please, code expression \"have_CNIC equals/not equals to True/False\"', file=sys.stderr)
    sys.exit(0)

print(json.dumps({ 'token': '{{token}}', 'passed': True }))