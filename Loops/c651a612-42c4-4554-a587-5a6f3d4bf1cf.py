# Course: Python Course
# Section: Loops
# Chapter: What are Loops
# Task Number: 1

print_string = ''.join(user_print_lines)
if print_string != '123456':
    print("Please, make sure that boundaries is (1,7)", file=sys.stderr)
    sys.exit(0)

print(json.dumps({ 'token': '{{token}}', 'passed': True }))