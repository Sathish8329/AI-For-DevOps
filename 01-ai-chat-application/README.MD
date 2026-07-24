# 🤖 AI Chat Application

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--5.5-412991?logo=openai&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-success)
![Learning](https://img.shields.io/badge/Learning-AI%20for%20DevOps-orange)
![License](https://img.shields.io/badge/License-MIT-blue)

A production-style command-line AI Chat Application built using the **OpenAI Python SDK**.

This project is the first hands-on project in the **AI for DevOps Engineers** repository and demonstrates how to build a clean, modular AI application with streaming responses, conversation history, logging, and production-ready exception handling.

---

# 🚀 Features

- 💬 Interactive AI Chat
- ⚡ Streaming Responses
- 🧠 Conversation History
- 📋 System Prompt Support
- 🔐 Environment Variable Configuration
- 🏗️ Modular Project Structure
- 📝 Application Logging
- ⚙️ Configurable Log Levels
- 🚨 Production-Style Exception Handling

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

# 📚 Concepts Covered

This project introduces the core concepts required to build AI-powered applications.

### AI Concepts

- OpenAI API
- OpenAI Python SDK
- Chat Completions API
- Large Language Models (LLMs)
- System Prompt
- User Prompt
- Assistant Response
- Conversation History
- Streaming Responses

### Python Concepts

- Python Modules
- Project Refactoring
- Environment Variables
- Virtual Environments
- Configuration Management

### Production Concepts

- Logging
- Configurable Log Levels
- Exception Handling
- Production Project Structure

---

# ⚙️ Prerequisites

- Python 3.11 or later
- OpenAI API Key

---

# 📦 Installation

## Clone the repository

```bash
git clone https://github.com/sathish8329/AI-For-DevOps.git
```

## Navigate to the project

```bash
cd AI-For-DevOps/01-ai-chat-application
```

## Create a virtual environment

```bash
python -m venv venv
```

## Activate the virtual environment

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

## Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Configuration

Create a `.env` file in the project directory.

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

# 📖 How It Works

```text
User
   │
   ▼
User Prompt
   │
   ▼
Conversation History
   │
   ▼
System Prompt
   │
   ▼
OpenAI Python SDK
   │
   ▼
GPT-5.5
   │
   ▼
Streaming Response
   │
   ▼
Assistant Response
```

---

# 🎯 What This Project Demonstrates

This project demonstrates the architecture of a production-style AI application.

- Maintains conversation history
- Uses a System Prompt to define AI behavior
- Streams responses from the OpenAI API
- Loads configuration from environment variables
- Uses structured logging
- Handles API-specific exceptions
- Separates responsibilities across multiple Python modules

---

# 🛠️ Technologies Used

- Python
- OpenAI Python SDK
- python-dotenv
- Logging
- Virtual Environment

---

# 🚀 Future Improvements

This project will be enhanced with:

- 💾 Conversation History Database
- 🧠 Long-Term Memory
- 📊 Token Usage Tracking
- 💰 Cost Estimation
- 🤖 Multiple Model Support
- 🔍 Retrieval-Augmented Generation (RAG)
- 🛠️ AI Agents
- 🔗 Model Context Protocol (MCP)

---

# 📚 Next Project

➡️ **02-devops-rag-assistant**

In the next project, we'll build a **Retrieval-Augmented Generation (RAG)** assistant that answers questions using your own DevOps documentation instead of relying solely on the model's training data.

Topics include:

- Document Loading
- Chunking
- Embeddings
- Vector Databases
- Semantic Search
- Retrieval-Augmented Generation (RAG)

---

# 🎓 Learning Journey

| Project | Status |
|----------|--------|
| ✅ 01 - AI Chat Application | Completed |
| ⏳ 02 - DevOps RAG Assistant | Coming Next |
| ⏳ 03 - AI DevOps Agent | Planned |
| ⏳ 04 - Memory | Planned |
| ⏳ 05 - Model Context Protocol (MCP) | Planned |
| ⏳ 06 - Multi-Agent Systems | Planned |
| ⏳ 07 - MLOps for DevOps Engineers | Planned |
| ⏳ 08 - Production AI Deployment | Planned |

---

## ⭐ Support

If you found this project useful, consider giving the repository a **⭐ Star**.

It motivates me to continue building practical AI projects for DevOps Engineers.

---

**Part of the 🚀 AI for DevOps Engineers learning repository.**