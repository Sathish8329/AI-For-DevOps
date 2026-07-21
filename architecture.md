# 🏗️ AI Architectures for DevOps Engineers (v1.0)

This document contains the architectures and workflows learned throughout this repository.

As we progress through the lessons, new architectures will be added.

---

# 📚 Architectures Covered

- End-to-End AI Application Architecture
- Retrieval-Augmented Generation (RAG) Architecture
- Tool Calling Architecture
- AI Agent Architecture
- Memory Architecture
- Model Context Protocol (MCP) Architecture
- Planning & Reasoning Workflow
- Enterprise AI Agent Architecture

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
Kubernetes#
    ↓
Deployment Scaled
    ↓
LLM
    ↓
User
```
---

---

# 4️⃣ AI Agent Architecture

```text
                    👤 User
                       │
                       ▼
                  💬 Prompt
                       │
                       ▼
                  🤖 AI Agent
                       │
                       ▼
                 📝 Planning
                       │
                       ▼
                 🧠 Reasoning
                       │
       ┌───────────────┼────────────────┐
       │               │                │
       ▼               ▼                ▼
📚 Need Knowledge? 🔧 Need Action? 🧠 Need Memory?
       │               │                │
       ▼               ▼                ▼
      RAG        Tool Calling       Memory
       │               │                │
       └───────────────┼────────────────┘
                       │
                       ▼
                  🧠 LLM
                       │
                       ▼
             🤖 Assistant Response
```

## 📖 Purpose

An AI Agent is more than an LLM. It can:

- Create plans
- Reason through problems
- Retrieve company knowledge (RAG)
- Use Memory
- Call external tools
- Complete multi-step tasks

---

# 5️⃣ Memory Architecture

```text
        👤 User
           │
           ▼
      🤖 AI Agent
           │
           ▼
   🧠 Memory Database
           │
           ▼
 Retrieve User Preferences
           │
           ▼
          🧠 LLM
           │
           ▼
   🤖 Assistant Response
```

## 📖 Purpose

Memory stores useful user or application preferences outside the LLM.

### Examples

- Default namespace
- Preferred cloud
- Default AWS region
- Preferred Kubernetes cluster

---

# 6️⃣ MCP Architecture

```text
              🤖 AI Agent
                   │
                   ▼
            🔧 Tool Calling
                   │
                   ▼
              🔌 MCP Client
                   │
     ┌─────────────┼─────────────┐
     │             │             │
     ▼             ▼             ▼
Kubernetes     GitHub         Jira
    MCP          MCP           MCP
     │             │             │
     ▼             ▼             ▼
 AWS MCP      Slack MCP   Prometheus MCP
     │             │             │
     └─────────────┼─────────────┘
                   │
                   ▼
          🌍 External Systems
                   │
                   ▼
              Return Results
                   │
                   ▼
                 🧠 LLM
                   │
                   ▼
          🤖 Assistant Response
```

## 📖 Purpose

MCP (Model Context Protocol) provides a standard way for AI Agents to communicate with external systems.

---

# 7️⃣ Planning & Reasoning Workflow

```text
        👤 User
           │
           ▼
      🤖 AI Agent
           │
           ▼
      📝 Create Plan
           │
           ▼
      📋 Task List
           │
           ▼
      ▶ Execute Step
           │
           ▼
      🧠 Reason
           │
           ▼
    Need Another Tool?
           │
      Yes──┘
           │
           ▼
   🔧 Tool Calling / MCP
           │
           ▼
      Return Result
           │
           ▼
      🧠 Reason Again
           │
           ▼
         ✅ Finished
```

## 📖 Purpose

Planning breaks work into steps.

Reasoning analyzes the result of each step and decides what to do next.

---

# 8️⃣ Enterprise AI Agent Architecture

```text
                                👤 User
                                   │
                                   ▼
                           💬 User Prompt
                                   │
                                   ▼
                              🤖 AI Agent
                        (Planning + Reasoning)
                                   │
                                   ▼
                          🧠 LLM (Decision Making)
                                   │
        ┌──────────────────────────┼──────────────────────────┐
        │                          │                          │
        ▼                          ▼                          ▼
     📚 RAG                   🧠 Memory               🔧 Tool Calling
        │                          │                          │
        ▼                          ▼                          ▼
 Vector Database            Application DB              MCP Client
        │                          │                          │
        └───────────────┬──────────┴──────────┬───────────────┘
                        │                     │
                        ▼                     ▼
               Kubernetes MCP          GitHub MCP
               AWS MCP                 Jira MCP
               Slack MCP               Prometheus MCP
                        │
                        ▼
                🌍 External Systems
                        │
                        ▼
                📥 Results Returned
                        │
                        ▼
                🧠 AI Agent Reasons
                        │
                        ▼
             🤖 Friendly Final Response
```

## 📖 Purpose

This architecture combines everything learned:

- Prompt Engineering
- LLM
- AI Agent
- Planning
- Reasoning
- RAG
- Memory
- Tool Calling
- MCP
- External Systems

It represents a modern enterprise AI application.
