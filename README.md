# prompt-agent

This is the prompt agent, part of VishwamAI.

## Introduction

The prompt agent is designed to auto-generate prompts and self-update. It leverages advanced NLP techniques to analyze user input and generate contextually relevant prompts. The agent is built using Python and includes mechanisms for adaptive prompting and self-updating.

## Project Structure

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

## Installation

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

5. Install the SpaCy language model:
   ```bash
   python -m spacy download en_core_web_sm
   ```

## Usage

To run the prompt agent, execute the following command:
```bash
python3 scripts/prompt_agent.py
```

The agent will prompt you to enter your input. Type your prompt and press Enter. To exit the agent, type `exit`.

## Development

### Adaptive Prompting

The adaptive prompting logic is implemented in the `adaptive_prompting.py` script. The `AdaptivePromptAgent` class includes methods for generating prompts, analyzing context, and updating the model.

### Self-Update Mechanism

The self-update mechanism is implemented in the `update_model` method of the `AdaptivePromptAgent` class. It uses system calls to perform `git pull` and `pip install -r requirements.txt` commands to update the code and dependencies.

### CI/CD Workflow

The CI/CD workflow is defined in the `.github/workflows/ci_cd.yml` file. It includes steps for setting up Python, installing dependencies, running tests, and deploying the application.

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
- [Requests](https://docs.python-requests.org/en/latest/)
- [NLTK](https://www.nltk.org/)
- [SpaCy](https://spacy.io/)
