# Course: Python Course
# Section: Functions
# Chapter: Nested Functions
# Task Number: 2

var_1 = ''
passed = False
for line in user_code_lines:
    if re.search('def\s*function_a\s*', line):
        var_1 = line
        passed = True
        break

first = var_1.index('(')
second = var_1.index(')')
word = var_1[first+1:second]

code_string = '\n'.join(user_code_lines)

passed_func = False
if re.search("\s*def\s*function_b\s*\(\s*\):.*\s*return\s*.*{}\s*\s*.*\s*return\s*function_b\s*\(\s*\)\s*".format(word), code_string):
    passed_func = True

if not passed_func:
    print("Please, create nested function nambed \"function_b\" and return the value of argument of \"function_a\"", file=sys.stderr)
    sys.exit(0)

is_print = False
for line in user_code_lines:
    if re.search('\s*print\s*\(\s*function_a\(\s*\d\s*\)\)', line):
        is_print = True

if not is_print:
    print("Please, print \"function_a\"", file=sys.stderr)
    sys.exit(0)

print(json.dumps({ 'token': '{{token}}', 'passed': True }))