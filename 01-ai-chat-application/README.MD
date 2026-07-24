# 🤖 AI Chat Application

A simple command-line AI Chat Application built using the **OpenAI Python SDK**.

This project is part of the **AI for DevOps Engineers** learning repository and demonstrates how to build a production-style AI application with clean project structure, configuration management, streaming responses, logging, and exception handling.

---

# 🚀 Features

- Interactive AI chat in the terminal
- Streaming responses
- Conversation history
- System Prompt support
- Environment variable configuration
- Production-style project structure
- Python logging
- Configurable log levels
- OpenAI-specific exception handling

---

# 🏗️ Project Structure

```text
01-ai-chat-application/
│
├── app.py
├── chat.py
├── config.py
├── logger.py
├── openai_client.py
├── requirements.txt
├── .env
└── README.md
```

---

# 📚 Concepts Learned

During this project, the following concepts were covered:

- OpenAI API
- API Keys
- OpenAI Python SDK
- Environment Variables
- Python Modules
- System Prompt
- User Prompt
- Assistant Response
- Conversation History
- Streaming Responses
- Project Refactoring
- Logging
- Exception Handling

---

# ⚙️ Prerequisites

- Python 3.11+
- OpenAI API Key

---

# 📦 Installation

Clone the repository

```bash
git clone https://github.com/Sathish8329/AI-For-DevOps.git
```

Navigate to the project

```bash
cd AI-For-DevOps/01-ai-chat-application
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

### Windows (Git Bash)

```bash
source venv/Scripts/activate
```

### Windows (PowerShell)

```powershell
venv\Scripts\Activate.ps1
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Configuration

Create a `.env` file.

```env
OPENAI_API_KEY=your_api_key
MODEL=gpt-5.5
LOG_LEVEL=INFO
```

---

# ▶️ Run the Application

```bash
python app.py
```

---

# 💬 Example

```text
============================================================
🤖 AI Chat Application
Type 'exit' to quit.
============================================================

You: What is Kubernetes?

AI:
Kubernetes is an open-source container orchestration platform used to deploy, manage, and scale containerized applications.
```

---

# 📖 What This Project Demonstrates

This project shows how a production-style AI application is structured.

- User enters a prompt.
- The application maintains conversation history.
- A System Prompt defines the AI's behavior.
- The OpenAI SDK sends the request to the selected model.
- Responses are streamed back to the terminal.
- Logging records important application events.
- Exception handling provides meaningful error messages.

---

# 🚀 Future Improvements

This project will be enhanced with:

- Conversation memory
- Chat history stored in a database
- Token usage tracking
- Cost estimation
- Multiple model support
- AI Agent integration
- Retrieval-Augmented Generation (RAG)
- Model Context Protocol (MCP)

---

# 📚 Next Project

➡️ **02-devops-rag-assistant**

Build an AI assistant that answers questions using your own DevOps documentation through Retrieval-Augmented Generation (RAG).

---

Part of the **AI for DevOps Engineers** learning repository.