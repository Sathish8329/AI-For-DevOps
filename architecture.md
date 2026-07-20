# 🏗️ AI Architectures for DevOps Engineers

This document contains the architectures and workflows learned throughout this repository.

As we progress through the lessons, new architectures will be added.

---

# 📚 Architectures Covered

- AI Application Architecture
- RAG Architecture
- Tool Calling (Function Calling) Architecture

---

# 1️⃣ AI Application Architecture

This is the high-level flow of a modern AI application.

```text
                                    👤 User
                                       │
                                       ▼
                           💬 User Prompt (Prompt)
                                       │
                                       ▼
              ⚙️ System Prompt (Defines AI Behavior & Response Format)
                                       │
                                       ▼
                          🧠 LLM (GPT, Claude, Gemini, Llama)
                                       │
               Understands the request and decides what is needed
                                       │
         ┌─────────────────────────────┴─────────────────────────────┐
         │                                                           │
         ▼                                                           ▼
📚 Need Company Knowledge?                                 🔧 Need Live Data or Action?
      (RAG)                                                 (Tool Calling / Function Calling)
         │                                                           │
        Yes                                                         Yes
         │                                                           │
         ▼                                                           ▼
 🔢 Generate Embedding                                   🛠️ Select Appropriate Tool
    (Embeddings)                                         (Tool Calling Decision)
         │                                                           │
         ▼                                                           ▼
🗄️ Search Vector Database                             🐍 Python Application
   (Vector Database)                                 (SDK + API Key)
         │                                                           │
         ▼                                                           ▼
Retrieve Relevant Documents                  Kubernetes / AWS / GitHub / Jira
(Runbooks, SOPs, Wiki, Docs)              (subprocess, SDKs, REST APIs)
         │                                                           │
         └───────────────────────────────┬───────────────────────────┘
                                         │
                                         ▼
                        📥 Send Results Back to the LLM
                     (Retrieved Documents + Live Data)
                                         │
                                         ▼
                     🧠 LLM Reasons & Combines Everything
              (Tokens + Context Window + Temperature)
                                         │
                                         ▼
                     🤖 Assistant Message (AI Response)
                                         │
                                         ▼
                           👨‍💻 Friendly Final Response
```

## 📖 What happens?

1. The user sends a prompt.
2. The System Prompt defines how the AI should behave.
3. The LLM understands the request.
4. If company knowledge is needed, it uses **RAG**.
5. If live data or an action is required, it uses **Tool Calling**.
6. Python retrieves the required information or performs the action.
7. The LLM combines everything and generates the final response.

---

# 2️⃣ RAG Architecture

RAG (Retrieval-Augmented Generation) allows the LLM to answer using your own documents.

```text
Question
    │
    ▼
Generate Embedding
    │
    ▼
Search Vector Database
    │
    ▼
Retrieve Relevant Documents
    │
    ▼
LLM
    │
    ▼
Final Answer
```

## 📖 Purpose

Instead of relying only on the model's training data, the LLM retrieves relevant company knowledge before generating a response.

### Example

Company documents:

- Kubernetes Runbooks
- Terraform Modules
- Internal Wiki
- SOPs
- Incident Documentation

Question:

> How does our company deploy applications?

The application searches the Vector Database, retrieves the relevant documents, and sends them to the LLM before generating the answer.

---

# 3️⃣ Tool Calling (Function Calling) Architecture

Tool Calling allows the LLM to interact with external systems through your application.

```text
User
   │
   ▼
User Prompt
   │
   ▼
LLM
   │
   ▼
Decides Which Tool to Use
   │
   ▼
Python Function
   │
   ▼
Kubernetes / AWS / GitHub / Jira
   │
   ▼
Return Result
   │
   ▼
LLM
   │
   ▼
Assistant Response
```

## 📖 Purpose

The LLM does not execute commands directly.

Instead, it decides which tool or function is required, and the Python application performs the action.

### Example

User:

> Scale deployment payment-api to 5 replicas.

Flow:

```
User
    ↓
LLM
    ↓
scale_deployment()
    ↓
Python
    ↓
Kubernetes
    ↓
Deployment Scaled
    ↓
LLM
    ↓
User
```

---

# 🎯 Key Learnings

✅ LLMs are responsible for reasoning.

✅ Python applications are responsible for execution.

✅ RAG retrieves company knowledge.

✅ Tool Calling interacts with external systems.

✅ Embeddings convert text into vectors.

✅ Vector Databases store embeddings for semantic search.

✅ Prompts define the user's request.

✅ System Prompts define how the AI should behave.

✅ Assistant Messages are the AI's responses.

---

# 🚀 Upcoming Architectures

As we continue learning, this document will be expanded with:

- AI Agents
- Memory
- Multi-Agent Systems
- MCP (Model Context Protocol)
- Agentic RAG
- AI Observability
- AI Workflows
- Planning & Reasoning
- AI Security
- AI Deployment Patterns

---

📌 This document will continue to evolve as new lessons and projects are added.
