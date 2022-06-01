# Course: Python Course
# Section: Data Structures
# Chapter: List Comprehension
# Task Number: 1

try:
    sentence
except NameError:
    print("Variable \"sentence\" not defined", file=sys.stderr)
    sys.exit(0)

try:
    words
except NameError:
    print("Variable \"words\" not defined", file=sys.stderr)
    sys.exit(0)

if not re.search("Python is easy to learn", sentence):
    print("Please, use provided initial value of variable", file=sys.stderr)
    sys.exit(0)

var_1 = ''
for line in user_code_lines:
    if re.search('for', line):
        var_1 = line
        break

first = var_1.index('for')+2
second = var_1.index('in')
variable = var_1[first+1:second]
variable = variable.strip()

passed = False
for line in user_code_lines:
    if re.search('\s*words\s*\=\s*\[\s*{}\s*for\s*{}\s*in\s*sentence.split\s*\(\s*\)\s*\]\s*'.format(variable, variable), line):
        passed = True

if not passed:
    print("Please, iterate over the variable \"sentence\" using list comprehension", file=sys.stderr)
    sys.exit(0)

is_print = False
for line in user_code_lines:
    if re.search('\s*print\s*\(\s*words\s*\)\s*', line):
        is_print = True

if not is_print:
    print("Please, print value of \"words\"", file=sys.stderr)
    sys.exit(0)

print(json.dumps({ 'token': '{{token}}', 'passed': True }))