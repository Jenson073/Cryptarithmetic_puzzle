from itertools import permutations

def is_valid_solution(mapping, words, result):
    """Check if the mapping satisfies the cryptarithmetic equation"""
    def get_value(word):
        return int("".join(str(mapping[char]) for char in word))
    
    # Ensure no word has leading zeros
    for word in words + [result]:
        if mapping[word[0]] == 0:
            return False

    return sum(get_value(word) for word in words) == get_value(result)

def solve_cryptarithmetic(words, result):
    """Solve the cryptarithmetic equation and generate an HTML output"""
    unique_chars = set("".join(words) + result)
    if len(unique_chars) > 10:
        print("Too many unique characters for a valid solution!")
        return

    for perm in permutations(range(10), len(unique_chars)):
        mapping = dict(zip(unique_chars, perm))
        if is_valid_solution(mapping, words, result):
            generate_html(words, result, mapping)
            return

    print("No solution found.")

def generate_html(words, result, mapping):
    """Generate an interactive HTML file for displaying the solution"""
    equation = " + ".join(words) + " = " + result
    solved_equation = " + ".join(["".join(str(mapping[c]) for c in word) for word in words]) + " = " + "".join(str(mapping[c]) for c in result)

    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Cryptarithmetic Solution</title>
        <style>
            body {{
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                text-align: center;
                margin: 50px;
                background: linear-gradient(to right, #ff9a9e, #fad0c4);
            }}
            h1 {{ color: #ffffff; }}
            .container {{
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                padding: 20px;
                background: white;
                border-radius: 10px;
                box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            }}
            table {{
                margin: 20px auto;
                border-collapse: collapse;
                width: 300px;
                background: white;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                border-radius: 8px;
                overflow: hidden;
            }}
            th, td {{
                padding: 12px;
                border: 1px solid #dee2e6;
                text-align: center;
            }}
            th {{
                background: #ff6f61;
                color: white;
            }}
            .solution {{
                font-size: 24px;
                font-weight: bold;
                color: blue;
                margin-top: 20px;
            }}
            .highlight {{
                font-size: 24px;
                font-weight: bold;
                color: #dc3545;
            }}
        </style>
    </head>
    <body>
        <h1>Cryptarithmetic Puzzle - AI</h1>
        <div class="container">
            <p><b>Given Equation:</b> <span class="highlight">{equation}</span></p>
            <p class="solution">Solved: {solved_equation}</p>
            <table>
                <tr><th>Letter</th><th>Digit</th></tr>
                {"".join(f"<tr><td>{letter}</td><td>{digit}</td></tr>" for letter, digit in mapping.items())}
            </table>
        </div>
    </body>
    </html>
    """

    # Save as an HTML file
    file_name = "cryptarithmetic_solution.html"
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(html_content)

    print(f"\nSolution saved! Open '{file_name}' in a browser to view.")

# Taking user input
equation = input("Enter your cryptarithmetic equation (e.g., SEND + MORE = MONEY): ")
parts = equation.replace(" ", "").split("=")

if "+" in parts[0]:
    words = parts[0].split("+")
    result = parts[1]
    solve_cryptarithmetic(words, result)
else:
    print("Invalid input format! Use 'WORD + WORD = RESULT'.")
