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

# 🏗️ High-Level AI Application Architecture

```
User
   │
   ▼
Prompt
   │
   ▼
System Prompt
   │
   ▼
LLM
   │
   ├── Answer directly
   │
   ├── Need Company Knowledge?
   │         │
   │         ▼
   │       RAG
   │
   └── Need Live Data or Action?
             │
             ▼
       Tool Calling
             │
             ▼
      Python Application
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
     Friendly Response
```

---

# 📌 Key Takeaways

- AI provides intelligence.
- ML learns from data.
- GenAI creates new content.
- LLMs understand and generate language.
- Tokens are how LLMs process text.
- Context Window limits how much information an LLM can process.
- Temperature controls creativity.
- Embeddings convert text into vectors.
- Vector Databases store embeddings.
- RAG retrieves company knowledge.
- API Keys authenticate applications.
- SDKs connect applications to LLMs.
- Prompt Engineering improves responses.
- System Messages define AI behavior.
- User Messages define the request.
- Assistant Messages contain the AI's response.
- Tool Calling enables AI to use external tools.
- Python orchestrates everything.
- LLMs reason; applications execute.

---

📌 This document will continue to grow as more AI concepts are added.
