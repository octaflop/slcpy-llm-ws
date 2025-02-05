---
marp: true
theme: default
paginate: true
class: lead
backgroundColor: #fff
---

# Getting Started with Local LLMs Using llm
## A Practical Guide to Running Language Models on Your Machine

---

# Act 1: Getting Started 🚀

## Installation and Setup

```bash
pip install llm
pip install llm[gpt4all]
pip install llm[llama]
```

---

# Basic Usage

Command line:
```bash
llm "What is the capital of France?"
```

Python:
```python
import llm

response = llm.complete("What is the capital of France?")
print(response)
```

---

# Act 2: Working with Models ⚡

## Installing Models

```bash
llm models install gpt4all-j
llm models install llama-2-7b-chat
```

---

# Selecting Models

```python
import llm

# Use a specific model
model = llm.get_model("gpt4all-j")
response = model.complete("Explain quantum computing")

# Set a default model
llm.set_default_model("gpt4all-j")
```

---

# Act 3: Advanced Features 🎭

## System Prompts and Templates

```python
import llm

template = """You are a helpful assistant.
Question: {question}
Answer: Let me help you with that."""

response = llm.complete(
    template.format(question="What is machine learning?"),
    system="You are an expert in AI and ML"
)
```

---

# Conversation History

```python
import llm

conversation = llm.Conversation()
conversation.append_message("user", "Hi, who are you?")
conversation.append_message("assistant", "I'm a helpful AI assistant.")
conversation.append_message("user", "What did I just ask you?")

response = llm.complete_conversation(conversation)
```

---

# Working with Chat Formats

```python
import llm

chat = llm.ChatCompletion()
messages = [
    {"role": "system", "content": "You are a helpful assistant"},
    {"role": "user", "content": "Hello!"},
]
response = chat.create(messages=messages)
```

---

# Best Practices & Tips 🎯

1. **Model Selection**
   - Consider hardware capabilities
   - Balance model size and performance
   - Test different models for specific use cases

2. **Resource Management**
   - Monitor memory usage
   - Use appropriate batch sizes
   - Consider quantized models

---

# Error Handling

```python
import llm

try:
    response = llm.complete("Your prompt here")
except llm.ModelError as e:
    print(f"Model error: {e}")
except llm.ResourceError as e:
    print(f"Resource error: {e}")
```

---

# Useful Commands

```bash
# List available models
llm models list

# Get model information
llm models info gpt4all-j

# Set default model
llm models default gpt4all-j

# Save and use templates
llm templates save my-template "You are a {role}. {question}"
llm --template my-template --param role="teacher" --param question="What is 2+2?"
```

---

# Resources 📚

- Official llm Documentation: [github.com/simonw/llm](https://github.com/simonw/llm)
- Simon Willison's Blog: [simonwillison.net](https://simonwillison.net)
- GPT4All Models: [gpt4all.io](https://gpt4all.io)
- LlamaCpp: [github.com/ggerganov/llama.cpp](https://github.com/ggerganov/llama.cpp)

---

# Troubleshooting

1. **Model Loading Failures**
   - Check model path configuration
   - Verify model compatibility
   - Ensure sufficient system resources

2. **Memory Issues**
   - Use smaller models
   - Enable model offloading
   - Clear conversation history periodically

3. **Performance Optimization**
   - Use quantized models
   - Adjust context window size
   - Implement caching strategies