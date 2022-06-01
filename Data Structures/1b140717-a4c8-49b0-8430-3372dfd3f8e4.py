# Course: Python Course
# Section: Data Structures
# Chapter: Sets
# Task Number: 2

try:
    fruits
except NameError:
    print('Variable \"fruits\" not defined', file=sys.stderr)
    sys.exit(0)

if not (fruits == {'apple', 'banana', 'mango'}):
    print('Please, initialize variable \"fruits\" with set of fruits', file=sys.stderr)
    sys.exit(0)

passed = False
for line in user_code_lines:
    if re.search('\s*.*sorted.*reverse\s*\=\s*True', line):
        passed = True

is_print = False
for line in user_print_lines:
    if re.search('[\'mango\', \'banana\', \'apple\']', line):
        is_print = True

if not is_print:
    print("Please, print sorted reversed set", file=sys.stderr)
    sys.exit(0)

print(json.dumps({ 'token': '{{token}}', 'passed': True }))
