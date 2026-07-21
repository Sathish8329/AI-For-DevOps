# 📖 AI Basics for DevOps Engineers

This document contains the AI concepts learned throughout this repository.

It will be updated as new lessons are completed.

---

# ✅ Lessons Covered

- Lesson 1 – AI, Machine Learning, Generative AI, LLM
- Lesson 2 – Tokens, Context Window, Temperature
- Lesson 3 – Embeddings
- Lesson 4 – Vector Databases
- Lesson 5 – Retrieval-Augmented Generation (RAG)
- Lesson 6 – OpenAI API, API Key, SDK, First AI Application
- Lesson 7 – Building Your First AI Application
- Lesson 8 – Prompt Engineering
- Lesson 9 – System Message, User Message, Assistant Message
- Lesson 10 – Tool Calling (Function Calling)
- Lesson 11 – AI Agents
- Lesson 12 – Memory
- Lesson 13 – Model Context Protocol (MCP)
- Lesson 14 – Planning & Reasoning

---

# 🤖 Artificial Intelligence (AI)

AI is software that performs tasks that normally require human intelligence.

### DevOps Examples

- Analyze Kubernetes logs
- Detect infrastructure issues
- Explain errors
- Suggest solutions

---

# 📊 Machine Learning (ML)

Machine Learning is a subset of AI.

Instead of writing every rule, the model learns patterns from data and makes predictions.

### Example

Predict CPU or memory usage using historical monitoring data.

---

# ✨ Generative AI

Generative AI creates new content.

Examples:

- Generate Kubernetes YAML
- Write Terraform code
- Create Shell Scripts
- Generate Documentation

---

# 🧠 Large Language Models (LLMs)

LLMs are AI models trained on massive amounts of text and code.

Examples:

- ChatGPT
- Claude
- Gemini
- Llama

They can:

- Explain Kubernetes concepts
- Generate Helm Charts
- Write Terraform modules
- Summarize logs

---

# 🧩 Tokens

A token is a small piece of text processed by an LLM.

Example

```
Kubernetes

↓

Kuber + netes
```

LLMs generate responses one token at a time.

---

# 🧠 Context Window

The context window is the maximum amount of information an LLM can consider while generating a response.

Examples

- 8K Tokens
- 32K Tokens
- 128K Tokens

If the context exceeds the limit, older information may be removed or the request may not fit.

---

# 🌡️ Temperature

Temperature controls how creative the model should be.

### Low Temperature

- Predictable
- Accurate
- Best for coding
- Best for DevOps tasks

### High Temperature

- Creative
- More variations
- Best for blogs and brainstorming

---

# 🔢 Embeddings

Embeddings convert text into numerical vectors so computers can understand semantic meaning.

Similar content produces similar embeddings.

### Example

Question

```
How do I deploy an application to Kubernetes?
```

Even if your documentation says

```
Deploy applications using kubectl apply
```

Embeddings recognize they are related.

---

# 🗄️ Vector Database

A Vector Database stores embeddings for semantic search.

Popular options

- ChromaDB
- Pinecone
- FAISS
- Weaviate
- Milvus
- pgvector

---

# 📚 Retrieval-Augmented Generation (RAG)

RAG allows an LLM to answer questions using your own documents instead of relying only on its training data.

### Flow

```
Question
    ↓
Embedding
    ↓
Vector Database
    ↓
Retrieve Relevant Documents
    ↓
LLM
    ↓
Answer
```

### DevOps Example

Ask:

```
How does our company deploy applications?
```

The LLM searches your deployment guide, runbooks, and internal documentation before answering.

---

# 🔑 API Key

An API Key identifies your application to the AI provider.

Without an API Key, your application cannot access the model.

### Best Practice

- Never hardcode API Keys.
- Store them in environment variables or a `.env` file.

---

# 🧰 OpenAI SDK

The OpenAI SDK is a Python library used to communicate with OpenAI models.

Example

```python
from openai import OpenAI
```

It works similarly to:

- boto3 for AWS
- kubernetes Python client
- Azure SDK

---

# 💬 Prompt

A Prompt is the instruction or question sent to the LLM.

Example

```
Explain why this Kubernetes Pod is in CrashLoopBackOff.
```

The quality of the prompt directly affects the quality of the answer.

---

# ✍️ Prompt Engineering

Prompt Engineering is the practice of writing better prompts to get better responses.

Instead of

```
Fix my pod.
```

Use

```
Analyze the following Kubernetes logs and events.

Identify:

- Root Cause
- Verification Steps
- Possible Fix
```

The more relevant context you provide, the better the answer.

---

# ⚙️ System Message

The System Message defines how the AI should behave.

Example

```
You are a Senior DevOps Engineer.

Always provide:

- Root Cause
- Verification
- Best Practices
```

### Why is it useful?

It ensures every user receives responses in the same format and quality.

---

# 👤 User Message

The User Message contains the user's actual request.

Example

```
Create an EC2 instance.

OS: Ubuntu
Region: ap-south-1
Instance Type: t2.medium
```

---

# 🤖 Assistant Message

The Assistant Message is the AI's response.

It follows the rules defined in the System Message while answering the User Message.

---

# 🔧 Tool Calling (Function Calling)

Tool Calling allows an LLM to use external tools through your application.

The LLM decides which tool to use.

Your Python application executes it.

Example

```
User

↓

Scale deployment payment-api to 5 replicas

↓

LLM

↓

scale_deployment()

↓

Python

↓

Kubernetes

↓

Result

↓

LLM

↓

User
```

The LLM never executes Kubernetes commands directly.

Python performs the action.

---

# 🐍 Python Application

The Python application acts as the orchestrator.

Responsibilities

- Read API Key
- Call OpenAI API
- Query Kubernetes
- Query AWS
- Query GitHub
- Execute Tool Calls
- Build Prompts
- Send Responses back to the LLM

---

# 🤖 AI Agent

An AI Agent is an application that can plan, reason, use tools, retrieve knowledge, and complete multi-step tasks.

Unlike a normal LLM that simply answers questions, an AI Agent decides what actions are required to complete a task.

### Example

User:

Deploy version 2.1 of the payment application.

The AI Agent may:

- Check the current version
- Find the Docker image
- Update the Kubernetes Deployment
- Verify Pods are healthy
- Notify the team

Instead of giving instructions, it performs the workflow using available tools.


---

# 🧠 Memory

Memory allows an AI application to remember useful information across conversations.

The LLM itself does not permanently remember information.

Instead, the application stores memory in a database and provides it to the LLM when needed.

### Examples

- Default AWS Region = ap-south-1
- Default Cluster = prod-eks
- Default Namespace = payments-prod
- Preferred Cloud = AWS

Memory stores user or application preferences—not company documents.

---

# 🔌 Model Context Protocol (MCP)

MCP is a standard way for AI applications to communicate with external tools.

Instead of every application writing custom integrations, MCP Servers expose tools in a consistent way.

### Examples

- Kubernetes MCP Server
- GitHub MCP Server
- Jira MCP Server
- Slack MCP Server

The AI Agent communicates with MCP Servers, and each server interacts with its respective system.

---


# 📝 Planning

Planning is the process of breaking a complex task into smaller steps before execution.

### Example

Upgrade Kubernetes Cluster

1. Check current version
2. Read upgrade guide
3. Upgrade control plane
4. Upgrade worker nodes
5. Verify cluster health
6. Notify the team

Planning happens before execution.
---


# 🧠 Reasoning

Reasoning is how the AI Agent analyzes information and decides what to do next during execution.

### Example

Pod Status

↓

CrashLoopBackOff

↓

Read Logs

↓

OOMKilled

↓

Increase Memory

↓

Restart Deployment

Reasoning happens throughout the workflow, not just once.
---
# 🏗️ High-Level AI Application Architecture
```

                                    👤 User
                                       │
                                       ▼
                           💬 User Prompt (Prompt)
                                       │
                                       ▼
              ⚙️ System Prompt (Defines AI Behavior & Response Format)
                                       │
                                       ▼
                          🤖 AI Agent (Plans & Reasons)
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
      (RAG)                                                 (Tool Calling / MCP)
         │                                                           │
         ▼                                                           ▼
 🔢 Generate Embedding                                   🛠️ Select Appropriate Tool
         │                                                           │
         ▼                                                           ▼
 🗄️ Search Vector Database                         🐍 Python App / MCP Client
         │                                                           │
         ▼                                                           ▼
Retrieve Relevant Documents              Kubernetes / AWS / GitHub / Jira / Slack
         │                                                           │
         └───────────────────────────────┬───────────────────────────┘
                                         │
                                         ▼
                              🧠 Memory (Application Database)
                                         │
                                         ▼
                        AI Agent Combines Everything & Reasons
                                         │
                                         ▼
                             🤖 Assistant Message (Response)
```

---

# 📌 Key Takeaways

- AI performs tasks that normally require human intelligence.
- Machine Learning learns patterns from data.
- Generative AI creates new content.
- LLMs understand and generate natural language.
- Tokens are the units an LLM processes.
- Context Window defines how much information an LLM can consider.
- Temperature controls the creativity of responses.
- Embeddings convert text into vectors for semantic understanding.
- Vector Databases store embeddings for similarity search.
- RAG enables LLMs to use company-specific knowledge.
- API Keys authenticate applications with AI providers.
- SDKs simplify communication with LLMs.
- Prompt Engineering improves response quality.
- System Messages define the AI's behavior.
- User Messages contain the user's request.
- Assistant Messages are the AI's responses.
- Tool Calling allows AI to interact with external systems.
- AI Agents plan, reason, and complete multi-step tasks.
- Memory stores user or application preferences outside the LLM.
- MCP provides a standardized way to connect AI with external tools.
- Planning breaks complex tasks into manageable steps.
- Reasoning helps the AI make decisions throughout execution.
- Python applications orchestrate tools, memory, RAG, and LLM interactions.---

📌 This document will continue to grow as more AI concepts are added.
