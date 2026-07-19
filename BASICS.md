# 📖 AI Basics for DevOps Engineers

This document contains the AI concepts learned throughout this repository.

It will be updated as new lessons are completed.

---

## ✅ Lessons Covered

* Lesson 1 – AI, Machine Learning, Generative AI, LLM
* Lesson 2 – Tokens, Context Window, Temperature
* Lesson 3 – Embeddings
* Lesson 4 – Vector Databases
* Lesson 5 – Retrieval-Augmented Generation (RAG)
* Lesson 6 – *(Coming Soon)*

---

### 🤖 Artificial Intelligence (AI)

AI is software that performs tasks that normally require human intelligence.

**DevOps Examples**

* Analyze Kubernetes logs
* Detect infrastructure issues
* Explain errors
* Suggest solutions

---

### 📊 Machine Learning (ML)

Machine Learning is a subset of AI.

Instead of writing every rule, the model learns patterns from data and makes predictions.

**Example**
Predict CPU or memory usage using historical monitoring data.

---

### ✨ Generative AI

Generative AI creates new content.

Examples:

* Generate Kubernetes YAML
* Write Terraform code
* Create Shell Scripts
* Generate Documentation

---

### 🧠 Large Language Models (LLMs)

LLMs are AI models trained on massive amounts of text and code.

Examples:

* ChatGPT
* Claude
* Gemini
* Llama

They can:

* Explain Kubernetes concepts
* Generate Helm Charts
* Write Terraform modules
* Summarize logs

---

### 🧩 Tokens

A token is a small piece of text processed by an LLM.

Example:

"Kubernetes"

↓

"Kuber" + "netes"

LLMs generate responses one token at a time.

---

### 🧠 Context Window

The context window is the maximum amount of information an LLM can consider while generating a response.

Examples:

* 8K Tokens
* 32K Tokens
* 128K Tokens

---

### 🌡️ Temperature

Temperature controls how creative the model should be.

**Low Temperature**

* Predictable responses
* Best for code and infrastructure

**High Temperature**

* Creative responses
* Best for writing and brainstorming

---

### 🔢 Embeddings

Embeddings convert text into numerical vectors so that computers can understand semantic meaning.

Similar text produces similar embeddings.

---

### 🗄️ Vector Database

Stores embeddings and enables semantic search.

Popular options:

* ChromaDB
* Pinecone
* FAISS
* Weaviate
* Milvus
* pgvector

---

### 📚 Retrieval-Augmented Generation (RAG)

RAG allows an LLM to answer questions using your own documents.

Flow:

Question → Embedding → Vector Database → Retrieve Documents → LLM → Final Answer

---

📌 This document will continue to grow as more AI concepts are added.
