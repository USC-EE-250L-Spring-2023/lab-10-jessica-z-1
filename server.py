from flask import Flask, request, jsonify

from main import process1, process2


app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({'message': 'Welcome'})

# TODO: Create a flask app with two routes, one for each function.
# The route should get the data from the request, call the function, and return the result.

@app.route('/process1', methods=['POST'])
def process1():
    data = request.json()
    def foo(x):
        """Find the next largest prime number."""
        while True:
            x += 1
            if all(x % i for i in range(2, x)):
                return x
    result = [foo(x) for x in data]
    
    return jsonify(result)

@app.route('/process2', methods=['POST'])
def process2():
    data = request.json()
    def foo(x):
        """Find the next largest prime number."""
        while True:
            x += 1
            if int(np.sqrt(x)) ** 2 == x:
                return x
    result =  [foo(x) for x in data]
    
    return jsonify(result)
    
if __name__ == '__main__':
    app.run(port=5000, debug=True)
    
    
