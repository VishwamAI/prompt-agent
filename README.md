# prompt-agent

## Abstract

The prompt agent is designed to auto-generate prompts and self-update. It leverages advanced NLP techniques to analyze user input and generate contextually relevant prompts. The agent is built using Python and includes mechanisms for adaptive prompting, self-updating, multi-textual prompt engineering, multilingual support, math-solving capabilities (including algebra, calculus, and statistics), and auto data collection.

## Introduction

The prompt agent is part of VishwamAI and aims to provide a comprehensive solution for generating and managing prompts. It includes advanced features such as adaptive prompting, multi-textual prompt engineering, multilingual support, math and coding problem-solving, auto data collection, and a self-update mechanism.

## System Overview

### Project Structure

```
VishwamAI/
├── data/               # Directory for datasets
├── models/             # Directory for storing trained models
├── scripts/            # Directory for scripts (e.g., training, preprocessing, model conversion, auto-update)
├── notebooks/          # Directory for Jupyter notebooks
├── logs/               # Directory for training logs and metrics
├── docs/               # Directory for documentation
├── config/             # Directory for configuration files
├── utils/              # Directory for utility scripts and functions
├── setup.sh            # Script for setting up the environment
├── requirements.txt    # File for specifying required dependencies
└── README.md           # Project overview and instructions
```

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/VishwamAI/prompt-agent.git
   cd prompt-agent
   ```

2. Set up a Python virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required dependencies:
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. Download necessary NLTK data:
   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('stopwords')
   ```

5. Install the SpaCy language models:
   ```bash
   python -m spacy download en_core_web_sm
   python -m spacy download es_core_news_sm
   python -m spacy download fr_core_news_sm
   python -m spacy download de_core_news_sm
   ```

## Usage

To run the prompt agent, execute the following command:
```bash
python3 scripts/prompt_agent.py
```

The agent will prompt you to enter your input. Type your prompt and press Enter. To exit the agent, type `exit`.

### Math and Coding Problem Solving

To run the problem-solving agent, execute the following command:
```bash
python3 scripts/problem_solving_agent.py
```

The agent will prompt you to enter a math or coding problem. Type your problem and press Enter. The agent can solve algebra, calculus, and statistics problems using `sympy`. To exit the agent, type `exit`.

### Auto Data Collection

To run the data collection agent, execute the following command:
```bash
python3 scripts/data_collection_agent.py
```

The agent will collect data from configured web sources and log its activity.

## Usage

To run the prompt agent, execute the following command:
```bash
python3 scripts/prompt_agent.py
```

The agent will prompt you to enter your input. Type your prompt and press Enter. To exit the agent, type `exit`.

### Math and Coding Problem Solving

To run the problem-solving agent, execute the following command:
```bash
python3 scripts/problem_solving_agent.py
```

The agent will prompt you to enter a math or coding problem. Type your problem and press Enter. The agent can solve algebra, calculus, and statistics problems using `sympy`. To exit the agent, type `exit`.

### Auto Data Collection

To run the data collection agent, execute the following command:
```bash
python3 scripts/data_collection_agent.py
```

The agent will collect data from configured web sources and log its activity.

## Development

### Adaptive Prompting

The adaptive prompting logic is implemented in the `adaptive_prompting.py` script. The `AdaptivePromptAgent` class includes methods for generating prompts, analyzing context, and updating the model.

### Multi-Textual Prompt Engineering

The multi-textual prompt engineering capabilities are implemented in the `adaptive_prompting.py` script. The `AdaptivePromptAgent` class includes methods for generating prompts and analyzing context for multiple textual inputs:
- `generate_multi_textual_prompt(user_inputs)`: Generates prompts for multiple textual inputs.
- `analyze_multi_textual_context(user_inputs)`: Analyzes context for multiple textual inputs.

### Multilingual Support

The multilingual support is implemented in the `adaptive_prompting.py` script. The `AdaptivePromptAgent` class includes methods for analyzing context in multiple languages, including English, Spanish, French, and German.

### Math and Coding Problem Solving

The math and coding problem-solving capabilities are implemented in the `problem_solving_agent.py` script. The `ProblemSolvingAgent` class includes methods for solving math problems using `sympy`, including algebra, calculus, and statistics problems. The coding problem-solving functionality is currently under development.

### Auto Data Collection

The auto data collection capabilities are implemented in the `data_collection_agent.py` script. The agent collects data from configured web sources and logs its activity.

### Self-Update Mechanism

The self-update mechanism is implemented in the `update_model` method of the `AdaptivePromptAgent` class. It uses system calls to perform `git pull` and `pip install -r requirements.txt` commands to update the code and dependencies.

## Results

### Running Tests Locally

To run the tests locally and replicate the CI/CD environment, use the `run_tests.sh` script. This script sets up a virtual environment, installs the required dependencies, and runs the tests using `pytest`.

1. Ensure the `run_tests.sh` script has executable permissions:
   ```bash
   chmod +x run_tests.sh
   ```

2. Execute the `run_tests.sh` script:
   ```bash
   ./run_tests.sh
   ```

The script will set up the environment, install dependencies, and run the tests. If any test fails, the script will exit immediately with an error message.

### CI/CD Workflow

The CI/CD workflow is defined in the `.github/workflows/ci_cd.yml` file. It includes steps for setting up Python, installing dependencies, running tests, and deploying the application.

## Conclusion

The prompt agent provides a robust solution for generating and managing prompts, with advanced features such as adaptive prompting, multi-textual prompt engineering, multilingual support, math and coding problem-solving, auto data collection, and a self-update mechanism. It is designed to be easily extensible and adaptable to various use cases.

## References

- [NumPy](https://numpy.org/)
- [NLTK](https://www.nltk.org/)
- [SpaCy](https://spacy.io/)
- [language_tool_python](https://github.com/jxmorris12/language_tool_python)
- [SymPy](https://www.sympy.org/)
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and push them to your fork.
4. Create a pull request to the main repository.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements

This project uses the following libraries and tools:
- [NumPy](https://numpy.org/)
- [NLTK](https://www.nltk.org/)
- [SpaCy](https://spacy.io/)
- [language_tool_python](https://github.com/jxmorris12/language_tool_python)
- [SymPy](https://www.sympy.org/)
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
