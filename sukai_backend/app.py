from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Sudoku Solver Backend"

@app.route('/solve', methods=['POST'])
def solve():
    # Placeholder pour la logique de résolution de Sudoku
    data = request.json
    # Ajoute la logique pour résoudre le Sudoku ici
    return jsonify({"solution": "Sudoku solution here"})

if __name__ == '__main__':
    app.run(debug=True)
