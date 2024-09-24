from flask import Flask, render_template, request, jsonify

app = Flask("Mathematics Problem Solver")

def get_numbers():
    """
    Retrieves and validates the 'num1' and 'num2' query parameters.
    Returns:
        tuple: Two valid numbers or an error message and status code.
    """
    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
        return num1, num2
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid input, please provide valid numbers."}), 400

@app.route("/sum", methods=["GET"])
def sum_route():
    numbers = get_numbers()
    if isinstance(numbers, tuple) and len(numbers) == 2:
        num1, num2 = numbers
        return jsonify({"result": num1 + num2}), 200
    return numbers  # returns the error message if validation fails

@app.route("/sub", methods=["GET"])
def sub_route():
    numbers = get_numbers()
    if isinstance(numbers, tuple) and len(numbers) == 2:
        num1, num2 = numbers
        return jsonify({"result": num1 - num2}), 200
    return numbers  # returns the error message if validation fails

@app.route("/mul", methods=["GET"])
def mul_route():
    numbers = get_numbers()
    if isinstance(numbers, tuple) and len(numbers) == 2:
        num1, num2 = numbers
        return jsonify({"result": num1 * num2}), 200
    return numbers  # returns the error message if validation fails

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
