import streamlit as st
from langchain_ollama import ChatOllama
from dotenv import load_dotenv

load_dotenv()

# LLM
llm = ChatOllama(
    model="qwen2.5:0.5b",
    temperature=0,
    num_predict=512
)

# Helper Function
def ask_llm(prompt):
    response = llm.invoke(prompt)
    return response.content


# Streamlit Page
st.set_page_config(
    page_title="SQL AI Generator",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI SQL Query Generator")

st.write(
    "Generate SQL queries from plain English with explanation and sample output."
)

# Sidebar
with st.sidebar:
    st.header("Settings")

    database = st.selectbox(
        "Database",
        [
            "MySQL",
            "PostgreSQL",
            "SQLite",
            "SQL Server",
            "Oracle"
        ]
    )

    temperature = st.slider(
        "Temperature",
        0.0,
        1.0,
        0.0,
        0.1
    )

    llm.temperature = temperature

# User Input
query = st.text_area(
    "Describe what you want...",
    placeholder="Example: Show top 5 employees with highest salary in each department."
)

generate = st.button(
    "🚀 Generate SQL",
    use_container_width=True
)

# Generate
if generate:

    if not query.strip():
        st.warning("Please enter a query.")
        st.stop()

    with st.spinner("Generating..."):

        sql_prompt = f"""
You are an expert SQL developer.

Database:
{database}

Generate ONLY SQL code.

Request:
{query}

Do not include markdown.
"""

        sql = ask_llm(sql_prompt)

        explanation_prompt = f"""
Explain this SQL query in very simple language.

{sql}
"""

        explanation = ask_llm(explanation_prompt)

        output_prompt = f"""
For this SQL query:

{sql}

Generate a realistic sample table showing the expected output.
"""

        sample_output = ask_llm(output_prompt)

    tab1, tab2, tab3 = st.tabs(
        [
            "💻 SQL",
            "📖 Explanation",
            "📊 Sample Output"
        ]
    )

    with tab1:
        st.code(sql, language="sql")

        st.download_button(
            "Download SQL",
            sql,
            file_name="query.sql"
        )

    with tab2:
        st.write(explanation)

    with tab3:
        st.markdown(sample_output)

    with st.expander("Prompt Used"):
        st.write(query)