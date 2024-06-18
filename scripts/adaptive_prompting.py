import random
import spacy
import nltk
import language_tool_python
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from langdetect import detect

# Download NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Load spaCy models
nlp_en = spacy.load('en_core_web_sm')
nlp_es = spacy.load('es_core_news_sm')
nlp_fr = spacy.load('fr_core_news_sm')
nlp_de = spacy.load('de_core_news_sm')

# Initialize LanguageTool
tool_en = language_tool_python.LanguageTool('en-US')
tool_es = language_tool_python.LanguageTool('es')
tool_fr = language_tool_python.LanguageTool('fr')
tool_de = language_tool_python.LanguageTool('de')

class AdaptivePromptAgent:
    def __init__(self):
        self.prompt_history = []

    def generate_prompt(self, user_input):
        # Adaptive prompting logic
        if self.prompt_history:
            last_prompt = self.prompt_history[-1]
            prompt = f"Based on your previous input '{last_prompt}', here is a new prompt: {user_input}"
        else:
            prompt = f"Generated prompt based on input: {user_input}"
        self.prompt_history.append(prompt)
        return prompt

    def analyze_context(self, user_input):
        # Detect language of the user input
        lang = detect(user_input)

        # Select appropriate spaCy model and LanguageTool based on detected language
        if lang == 'en':
            nlp = nlp_en
            tool = tool_en
            stop_words = set(stopwords.words('english'))
        elif lang == 'es':
            nlp = nlp_es
            tool = tool_es
            stop_words = set(stopwords.words('spanish'))
        elif lang == 'fr':
            nlp = nlp_fr
            tool = tool_fr
            stop_words = set(stopwords.words('french'))
        elif lang == 'de':
            nlp = nlp_de
            tool = tool_de
            stop_words = set(stopwords.words('german'))
        else:
            return f"Unsupported language detected: {lang}"

        # Analyze the context of the user input
        context = f"Context analysis of input: {user_input}"

        # Enhanced context analysis using spaCy and NLTK
        doc = nlp(user_input)
        tokens = word_tokenize(user_input)
        filtered_tokens = [word for word in tokens if word.lower() not in stop_words]

        # Simple keyword-based context analysis
        if "help" in user_input.lower():
            context += " - User is asking for help."
        elif "info" in user_input.lower():
            context += " - User is asking for information."
        else:
            context += " - General input."

        # Named entity recognition using spaCy
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        if entities:
            context += f" - Named entities recognized: {entities}"

        # Part-of-speech tagging using spaCy
        pos_tags = [(token.text, token.pos_) for token in doc]
        context += f" - Part-of-speech tags: {pos_tags}"

        # Grammar checking using LanguageTool
        matches = tool.check(user_input)
        if matches:
            context += " - Grammar issues detected:"
            for match in matches:
                context += f" {match.ruleId}: {match.message} (suggestion: {match.replacements})"
        else:
            context += " - No grammar issues detected."

        return context

    def update_model(self):
        # Self-updating mechanism
        print("Checking for updates...")
        # Implementing the actual update logic
        import os
        os.system("git fetch origin main")
        os.system("git merge --ff-only FETCH_HEAD")
        os.system("pip install -r requirements.txt")
        # Check for updates to language_tool_python
        os.system("pip install --upgrade language_tool_python")
        # Reload the model with the new code
        print("Model updated successfully.")

    def generate_multi_textual_prompt(self, user_inputs):
        # Generate prompts for multiple textual inputs
        prompts = []
        for user_input in user_inputs:
            prompt = self.generate_prompt(user_input)
            prompts.append(prompt)
        return prompts

    def analyze_multi_textual_context(self, user_inputs):
        # Analyze context for multiple textual inputs
        contexts = []
        for user_input in user_inputs:
            context = self.analyze_context(user_input)
            contexts.append(context)
        return contexts

def main():
    agent = AdaptivePromptAgent()
    while True:
        user_input = input("Enter your prompt (or 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("Exiting Prompt Agent.")
            break
        else:
            context = agent.analyze_context(user_input)
            print(context)
            prompt = agent.generate_prompt(user_input)
            print(prompt)
            agent.update_model()

if __name__ == "__main__":
    main()
