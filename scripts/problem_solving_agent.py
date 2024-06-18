import sympy as sp
import re
import time

class ProblemSolvingAgent:
    def __init__(self):
        pass

    def solve_math_problem(self, problem):
        try:
            # Use sympy to solve the math problem
            solution = sp.sympify(problem).evalf()
            return f"The solution to the math problem '{problem}' is: {solution}"
        except Exception as e:
            return f"Error solving math problem: {str(e)}"

    def solve_coding_problem(self, problem):
        # Placeholder for coding problem-solving logic
        return "Coding problem-solving functionality is under development."

    def parse_input(self, user_input):
        # Determine if the input is a math problem or a coding problem
        if re.search(r'[+\-*/^=]', user_input):
            return self.solve_math_problem(user_input)
        else:
            return self.solve_coding_problem(user_input)

if __name__ == "__main__":
    agent = ProblemSolvingAgent()

    while True:
        user_input = input("Enter a math or coding problem (or 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break
        result = agent.parse_input(user_input)
        print(result)
