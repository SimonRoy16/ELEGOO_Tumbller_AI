# RAG Jupyter Notebook Environment Setup

This guide explains how to set up the environment for running the RAG (Retrieval Augmented Generation) Jupyter notebooks.

## Prerequisites

- Python 3.10 or higher
- pip (Python package installer)
- conda (recommended for environment management)

## Environment Setup

1. Create a new conda environment (recommend use the latest conda for conda-libmamba-solver)):

```bash
conda create -n langchain python=3.10
conda activate langchain
```

2. Install required packages:
check here for all the packages used in the [tutorial](https://python.langchain.com/docs/tutorials/rag/)

```bash
pip install jupyter
pip install langchain
pip install langchain-openai
pip install langchain-community
pip install langchain-core
pip install langgraph
pip install langchain-text-splitters
pip install langchain-community
pip install typing-extensions
pip install beautifulsoup4
pip install openai
pip install langchain-unstructured
pip install unstructured-client
pip install unstructured
pip install unstructured[pdf]
pip install python-magic
```

## Environment Variables

Set up your OpenAI API key:

```bash
export OPENAI_API_KEY='your-api-key-here'
```
To use the Unstructured.io API with normal installation, you need to set up an account and get an API key (more details [here](https://python.langchain.com/docs/integrations/document_loaders/unstructured_file/))

```bash
export UNSTRUCTURED_API_KEY='your-api-key-here'
```

## Notebooks Overview

- `rag_unstructured.ipynb`: Demonstrates RAG implementation using basic LangChain (following this [tutorial](https://python.langchain.com/docs/tutorials/rag/))
  - Loads and processes PDF documents
  - Creates embeddings using OpenAI's text-embedding-3-large model
  - Implements similarity search for question answering
  - Uses OpenAI's GPT models for generating responses



## Additional Resources

- [LangChain Documentation](https://python.langchain.com/docs/get_started/introduction)
- [OpenAI API Documentation](https://platform.openai.com/docs/introduction)
- [Unstructured Documentation](https://python.langchain.com/docs/integrations/document_loaders/unstructured_file/)
