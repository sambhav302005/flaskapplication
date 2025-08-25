<<<<<<< HEAD
from flask import Flask, render_template, request, jsonify, redirect, url_for
from datetime import datetime

# Initialize Flask app (default: templates/ for HTML, static/ for CSS/JS)
app = Flask(__name__)

# Problems dataset (added more problems)
problems = {
    "Two Sum": {
        "description": "Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.",
        "difficulty": "Easy",
        "category": "Array, Hash Table",
        "examples": [
            {"input": "nums = [2,7,11,15], target = 9", "output": "[0,1]", "explanation": "Because nums[0] + nums[1] == 9"}
        ],
        "constraints": [
            "2 <= nums.length <= 10⁴",
            "-10⁹ <= nums[i] <= 10⁹",
            "-10⁹ <= target <= 10⁹",
            "Only one valid answer exists."
        ],
        "hints": [
            "Try brute force first.",
            "Optimize using a HashMap."
        ]
    },
    "Reverse String": {
        "description": "Write a function that reverses a string.",
        "difficulty": "Easy",
        "category": "String, Two-Pointer",
        "examples": [
            {"input": "s = 'hello'", "output": "'olleh'"}
        ],
        "constraints": [
            "1 <= s.length <= 10⁵"
        ],
        "hints": [
            "Use two pointers.",
            "Try Python slicing."
        ]
    },
    "Valid Parentheses": {
        "description": "Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.",
        "difficulty": "Medium",
        "category": "Stack, String",
        "examples": [
            {"input": "s = '()[]{}'", "output": "true"},
            {"input": "s = '(]'", "output": "false"}
        ],
        "constraints": [
            "1 <= s.length <= 10⁴"
        ],
        "hints": [
            "Use a stack.",
            "Push opening brackets and match with closing."
        ]
    }
}

# Keep track of recent submissions
submissions = []


def analyze_solution(solution_code):
    """Basic static code analysis."""
    analysis = {
        "language": "Unknown",
        "has_comments": False,
        "line_count": 0,
        "estimated_complexity": "Unknown",
        "suggestions": []
    }

    if not solution_code.strip():
        return analysis

    lines = solution_code.strip().split('\n')
    analysis["line_count"] = len(lines)

    # Detect language (simple heuristic)
    if any(k in solution_code for k in ['def ', 'import ', 'print(', 'len(']):
        analysis["language"] = "Python"
    elif any(k in solution_code for k in ['public class', 'System.out']):
        analysis["language"] = "Java"
    elif any(k in solution_code for k in ['#include', 'printf']):
        analysis["language"] = "C/C++"
    elif any(k in solution_code for k in ['function', 'console.log']):
        analysis["language"] = "JavaScript"

    # Comments
    if any(line.strip().startswith(('#', '//', '/*')) for line in lines):
        analysis["has_comments"] = True

    # Complexity guess
    if solution_code.count('for') > 1:
        analysis["estimated_complexity"] = "O(n²) or higher"
    elif 'for' in solution_code or 'while' in solution_code:
        analysis["estimated_complexity"] = "O(n)"
    else:
        analysis["estimated_complexity"] = "O(1) or O(log n)"

    # Suggestions
    if not analysis["has_comments"]:
        analysis["suggestions"].append("Add comments for clarity.")
    if analysis["line_count"] > 50:
        analysis["suggestions"].append("Try simplifying your solution.")
    elif analysis["line_count"] < 5:
        analysis["suggestions"].append("Add edge case handling.")

    return analysis


@app.route("/", methods=["GET", "POST"])
def index():
    """Home page with problem selection and solution submission."""
    if request.method == "POST":
        problem_title = request.form.get("problem")
        solution = request.form.get("solution", "")

        details = problems.get(problem_title, {
            "description": "This problem is not in the database.",
            "difficulty": "N/A", "category": "N/A",
            "examples": [], "constraints": [], "hints": []
        })

        analysis = analyze_solution(solution)

        # Save submission
        submissions.append({
            "problem": problem_title,
            "solution": solution,
            "analysis": analysis,
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

        return render_template("result.html",
                               title=problem_title,
                               details=details,
                               solution=solution,
                               analysis=analysis,
                               timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    return render_template("index.html", problems=problems)


@app.route("/problems")
def problem_list():
    """Page listing all problems."""
    return render_template("problems.html", problems=problems)


@app.route("/submissions")
def view_submissions():
    """View recent submissions."""
    return render_template("submissions.html", submissions=submissions)


@app.route("/api/analyze", methods=["POST"])
def api_analyze():
    """API endpoint for analyzing code (JSON input/output)."""
    data = request.get_json()
    code = data.get("solution", "")
    result = analyze_solution(code)
    return jsonify(result)


@app.errorhandler(404)
def page_not_found(e):
    """Custom 404 error page."""
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)
=======
from flask import Flask, render_template, request, jsonify, redirect, url_for
from datetime import datetime

# Initialize Flask app (default: templates/ for HTML, static/ for CSS/JS)
app = Flask(__name__)

# Problems dataset (added more problems)
problems = {
    "Two Sum": {
        "description": "Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.",
        "difficulty": "Easy",
        "category": "Array, Hash Table",
        "examples": [
            {"input": "nums = [2,7,11,15], target = 9", "output": "[0,1]", "explanation": "Because nums[0] + nums[1] == 9"}
        ],
        "constraints": [
            "2 <= nums.length <= 10⁴",
            "-10⁹ <= nums[i] <= 10⁹",
            "-10⁹ <= target <= 10⁹",
            "Only one valid answer exists."
        ],
        "hints": [
            "Try brute force first.",
            "Optimize using a HashMap."
        ]
    },
    "Reverse String": {
        "description": "Write a function that reverses a string.",
        "difficulty": "Easy",
        "category": "String, Two-Pointer",
        "examples": [
            {"input": "s = 'hello'", "output": "'olleh'"}
        ],
        "constraints": [
            "1 <= s.length <= 10⁵"
        ],
        "hints": [
            "Use two pointers.",
            "Try Python slicing."
        ]
    },
    "Valid Parentheses": {
        "description": "Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.",
        "difficulty": "Medium",
        "category": "Stack, String",
        "examples": [
            {"input": "s = '()[]{}'", "output": "true"},
            {"input": "s = '(]'", "output": "false"}
        ],
        "constraints": [
            "1 <= s.length <= 10⁴"
        ],
        "hints": [
            "Use a stack.",
            "Push opening brackets and match with closing."
        ]
    }
}

# Keep track of recent submissions
submissions = []


def analyze_solution(solution_code):
    """Basic static code analysis."""
    analysis = {
        "language": "Unknown",
        "has_comments": False,
        "line_count": 0,
        "estimated_complexity": "Unknown",
        "suggestions": []
    }

    if not solution_code.strip():
        return analysis

    lines = solution_code.strip().split('\n')
    analysis["line_count"] = len(lines)

    # Detect language (simple heuristic)
    if any(k in solution_code for k in ['def ', 'import ', 'print(', 'len(']):
        analysis["language"] = "Python"
    elif any(k in solution_code for k in ['public class', 'System.out']):
        analysis["language"] = "Java"
    elif any(k in solution_code for k in ['#include', 'printf']):
        analysis["language"] = "C/C++"
    elif any(k in solution_code for k in ['function', 'console.log']):
        analysis["language"] = "JavaScript"

    # Comments
    if any(line.strip().startswith(('#', '//', '/*')) for line in lines):
        analysis["has_comments"] = True

    # Complexity guess
    if solution_code.count('for') > 1:
        analysis["estimated_complexity"] = "O(n²) or higher"
    elif 'for' in solution_code or 'while' in solution_code:
        analysis["estimated_complexity"] = "O(n)"
    else:
        analysis["estimated_complexity"] = "O(1) or O(log n)"

    # Suggestions
    if not analysis["has_comments"]:
        analysis["suggestions"].append("Add comments for clarity.")
    if analysis["line_count"] > 50:
        analysis["suggestions"].append("Try simplifying your solution.")
    elif analysis["line_count"] < 5:
        analysis["suggestions"].append("Add edge case handling.")

    return analysis


@app.route("/", methods=["GET", "POST"])
def index():
    """Home page with problem selection and solution submission."""
    if request.method == "POST":
        problem_title = request.form.get("problem")
        solution = request.form.get("solution", "")

        details = problems.get(problem_title, {
            "description": "This problem is not in the database.",
            "difficulty": "N/A", "category": "N/A",
            "examples": [], "constraints": [], "hints": []
        })

        analysis = analyze_solution(solution)

        # Save submission
        submissions.append({
            "problem": problem_title,
            "solution": solution,
            "analysis": analysis,
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

        return render_template("result.html",
                               title=problem_title,
                               details=details,
                               solution=solution,
                               analysis=analysis,
                               timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    return render_template("index.html", problems=problems)


@app.route("/problems")
def problem_list():
    """Page listing all problems."""
    return render_template("problems.html", problems=problems)


@app.route("/submissions")
def view_submissions():
    """View recent submissions."""
    return render_template("submissions.html", submissions=submissions)


@app.route("/api/analyze", methods=["POST"])
def api_analyze():
    """API endpoint for analyzing code (JSON input/output)."""
    data = request.get_json()
    code = data.get("solution", "")
    result = analyze_solution(code)
    return jsonify(result)


@app.errorhandler(404)
def page_not_found(e):
    """Custom 404 error page."""
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)
>>>>>>> e0e8506aa982e6f36ceac79299eacda6aa8fb5f7
