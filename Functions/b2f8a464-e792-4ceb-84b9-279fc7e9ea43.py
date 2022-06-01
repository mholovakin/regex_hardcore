# Course: Python Course
# Section: Functions
# Chapter: Functions as Arguments
# Task Number: 2


code_string = '\n'.join(user_code_lines)

if not re.search('\s*def\s*base_heigth\s*\(\)\s*:\s*.*base\s*\=\s*10.*\s*height\s*\=\s*12\s*.*return\s*base\s*\*\s*height\s*', code_string):
    print("Please, don\'t change initial function", file=sys.stderr)
    sys.exit(0)

if not re.search('\s*def\s*area_triangle\s*\(\s*[a-zA-Z]+\s*\):\s*.*\s*return\s*base_heigth\s*\(\)\s*/\s*2\s*', code_string):
    print("Please, create function area_triangle, which takes argument and return base_heigth()/2", file=sys.stderr)
    sys.exit(0)

if not re.search('\s*print\s*\(\s*area_triangle\s*\(\s*base_heigth\(\)\)\)\s*', code_string):
    print("Please, print the result of function", file=sys.stderr)
    sys.exit(0)

print(json.dumps({ 'token': '{{token}}', 'passed': True }))
