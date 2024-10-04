from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return parameter  # Just return the parameter

@app.route('/count/<int:parameter>')
def count(parameter):
    # Create a string with numbers from 0 to parameter - 1, adding a trailing newline
    numbers = '\n'.join(str(i) for i in range(parameter)) + '\n'  # Add a newline at the end
    return numbers

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '%':
        result = num1 % num2
    elif operation == 'div':
        if num2 == 0:
            return 'Cannot divide by zero', 400
        result = num1 / num2
    else:
        return 'Invalid operation', 400

    return str(result)

if __name__ == '__main__':
    app.run(port=5555)
