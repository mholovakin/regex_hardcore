# Course: Python Course
# Section: Data Structures
# Chapter: Data Structure Conversions
# Task Number: 1

try:
    list_countries
except NameError:
    print('Variable \"list_countries\" not defined', file=sys.stderr)
    sys.exit(0)

try:
    list_capitals
except NameError:
    print("Variable \"list_capitals\" not defined", file=sys.stderr)
    sys.exit(0)

try:
    countries_capitals
except NameError:
    print("Variable \"countries_capitals\" not defined", file=sys.stderr)
    sys.exit(0)

if not (list_countries == ['Australia', 'Canada', 'Germany', 'India', 'Japan'] and list_capitals == ['Canberra', 'Ottawa', 'Berlin', 'New Delhi', 'Tokyo']):
    print("Please, use provided initial values of variables", file=sys.stderr)
    sys.exit(0)

var_1 = ''
for line in user_code_lines:
    if re.search('for', line):
        var_1 = line

first = var_1.index('for'[-1])
second = var_1.index('in')
variable = var_1[first+1:second]
variable = variable.strip()

code_string = '\n'.join(user_code_lines)

is_for = False
for line in user_code_lines:
    if re.search("\s*for\s*{}\s*in\s*range\s*".format(variable), line):
        is_for = True

if not is_for:
    print("Loop through both the lists, list_countries and list_capitals", file=sys.stderr)
    sys.exit(0)

is_assign = False
for line in user_code_lines:
    if re.search('\s*countries_capitals\s*\[\s*list_countries\[\s*{}\s*\]\s*\]\s*\=\s*list_capitals\s*\[\s*{}\s*\]\s*'.format(variable,variable), line):
        is_assign = True

if not is_assign:
    print('Make a key for each country and assign the capital as the value', file=sys.stderr)
    sys.exit(0)

is_print = False
for line in user_print_lines:
    if re.search('{\'Australia\': \'Canberra\', \'Canada\': \'Ottawa\', \'Germany\': \'Berlin\', \'India\': \'New Delhi\', \'Japan\': \'Tokyo\'}', line):
        is_print = True

if not is_print:
    print("Please, print countries with capitals", file=sys.stderr)
    sys.exit(0)

print(json.dumps({ 'token': '{{token}}', 'passed': True }))