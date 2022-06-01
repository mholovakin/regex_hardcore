# Course: Python Course
# Section: Errors and Exceptions
# Chapter: What are clean-up actions?
# Task Number: 1

code_string = '\n'.join(user_code_lines)

var_1 = ''
for line in user_code_lines:
    if re.search('def\s*divide', line):
        var_1 = line

if var_1 == '':
    print("function \"divide\" not defined", file=sys.stderr)
    sys.exit(0)

first = var_1.index('('[-1])
second = var_1.index(')')
variable = var_1[first+1:second]
variable = variable.strip()

if not re.search('\s*try\s*:\s*.*\s*{}\s*/\s*3\s*except\s*TypeError\s*:\s*.*print\s*\(.*\)\s*.*\s*else\s*:\s*.*\s*print\s*\(.*\)\s*.*\s*finally\s*:\s*.*\s*print\s*\(.*\)\s*'.format(variable), code_string):
    print('Please, use \"try\", \"except\",\"else\" and \"finally\" statements', file=sys.stderr)
    sys.exit(0)

print(json.dumps({ 'token': '{{token}}', 'passed': True }))