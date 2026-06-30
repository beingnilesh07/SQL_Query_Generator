# 🧠 SQL Query Generator using Ollama

A simple AI-powered application that converts natural language into SQL queries using an open-source LLM running locally with **Ollama**. The project provides a clean **Streamlit** interface, allowing users to generate SQL queries without relying on paid APIs.

## 🚀 Features

- Convert plain English into SQL queries
- Runs locally using Ollama (no API key required)
- Supports common SQL operations like `SELECT`, `JOIN`, `GROUP BY`, and `ORDER BY`
- Simple and interactive Streamlit interface
- Fast, private, and cost-free inference

## 🛠️ Tech Stack

- Python
- Streamlit
- Ollama
- LangChain
- SQL

## 📂 Project Structure

```text
SQL-Query-Generator/
├── app.py
├── requirements.txt
├── .env
└── README.md
```

## ⚙️ Getting Started

1. Clone the repository

```bash
git clone https://github.com/yourusername/SQL-Query-Generator.git
cd SQL-Query-Generator
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Pull an Ollama model

```bash
ollama pull  qwen2.5
```

4. Run the application

```bash
streamlit run app.py
```

## 💬 Example

**Input:**

> Show all employees whose salary is greater than 50000.

**Output:**

```sql
SELECT * FROM employees
WHERE salary > 50000;
```

## 🔮 Future Improvements

- Database schema upload
- Query execution support
- SQL explanation
- Multi-database support

## 👨‍💻 Author

**Nilesh Biladi**

*AI/ML Enthusiast | Data Science | Generative AI | Python | SQL*
