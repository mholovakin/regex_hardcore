# Course: Python Course
# Section: Functions
# Chapter: Recursion
# Task Number: 2

var_1 = ''
passed = False
for line in user_code_lines:
    if re.search('def\s*recursive_factorial\s*', line):
        var_1 = line
        passed = True
        break

if not passed:
    print("Please, define function \"recursive_factorial\"", file=sys.stderr)
    sys.exit(0)

first = var_1.index('(')
second = var_1.index(')')
word = var_1[first+1:second]

passed_return = False
for line in user_code_lines:
    if re.search('\s*return\s*{}\s*\*\s*recursive_factorial\s*\(\s*{}\s*\-\s*1\s*\)\s*'.format(word, word), line):
        passed_return = True

if not passed_return:
    print("Please, return your variable * function with variable-1", file=sys.stderr)
    sys.exit(0)


print(json.dumps({ 'token': '{{token}}', 'passed': True }))