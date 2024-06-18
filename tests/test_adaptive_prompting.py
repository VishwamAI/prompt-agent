import pytest
from scripts.adaptive_prompting import AdaptivePromptAgent

def test_adaptive_prompt_agent_initialization():
    agent = AdaptivePromptAgent()
    assert agent is not None
    assert isinstance(agent, AdaptivePromptAgent)
    assert agent.prompt_history == []

def test_generate_prompt():
    agent = AdaptivePromptAgent()
    user_input = "Hello, how are you?"
    prompt = agent.generate_prompt(user_input)
    assert prompt == "Generated prompt based on input: Hello, how are you?"
    assert agent.prompt_history == [prompt]

def test_analyze_context():
    agent = AdaptivePromptAgent()
    user_input = "I need help with my account."
    context = agent.analyze_context(user_input)
    assert "Context analysis of input: I need help with my account." in context
    assert "User is asking for help." in context
    if "Named entities recognized:" in context:
        assert "Named entities recognized:" in context
    assert "Part-of-speech tags:" in context
    assert "Grammar issues detected:" in context or "No grammar issues detected." in context

def test_update_model():
    agent = AdaptivePromptAgent()
    # This test will only check if the method runs without errors
    agent.update_model()

def test_generate_multi_textual_prompt():
    agent = AdaptivePromptAgent()
    user_inputs = ["Hello, how are you?", "What is the weather like today?"]
    prompts = agent.generate_multi_textual_prompt(user_inputs)
    assert len(prompts) == 2
    assert prompts[0] == "Generated prompt based on input: Hello, how are you?"
    assert prompts[1] == "Based on your previous input 'Generated prompt based on input: Hello, how are you?', here is a new prompt: What is the weather like today?"

def test_analyze_multi_textual_context():
    agent = AdaptivePromptAgent()
    user_inputs = ["I need help with my account.", "Tell me more about your services."]
    contexts = agent.analyze_multi_textual_context(user_inputs)
    assert len(contexts) == 2
    assert "Context analysis of input: I need help with my account." in contexts[0]
    assert "User is asking for help." in contexts[0]
    assert "Context analysis of input: Tell me more about your services." in contexts[1]
    assert "General input." in contexts[1]

def test_analyze_context_multilingual():
    agent = AdaptivePromptAgent()
    user_input_en = "I need help with my account."
    user_input_es = "Necesito ayuda con mi cuenta."
    user_input_fr = "J'ai besoin d'aide avec mon compte."
    user_input_de = "Ich brauche Hilfe mit meinem Konto."

    context_en = agent.analyze_context(user_input_en)
    context_es = agent.analyze_context(user_input_es)
    context_fr = agent.analyze_context(user_input_fr)
    context_de = agent.analyze_context(user_input_de)

    assert "Context analysis of input: I need help with my account." in context_en
    assert "User is asking for help." in context_en

    assert "Context analysis of input: Necesito ayuda con mi cuenta." in context_es
    assert "User is asking for help." in context_es

    assert "Context analysis of input: J'ai besoin d'aide avec mon compte." in context_fr
    assert "User is asking for help." in context_fr

    assert "Context analysis of input: Ich brauche Hilfe mit meinem Konto." in context_de
    assert "User is asking for help." in context_de
