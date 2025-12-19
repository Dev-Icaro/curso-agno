from agno.agent import Agent
from agno.tools.yfinance import YFinanceTools

# from agno.models.groq import Groq
from agno.models.openai import OpenAIChat
from agno.db.postgres import PostgresDb
from dotenv import load_dotenv

load_dotenv()

# Statar o container docker
#  docker run -d `
# >> -e POSTGRES_DB=ai `
# >> -e POSTGRES_USER=ai `
# >> -e POSTGRES_PASSWORD=ai `
# >> -e PGDATA=/var/lib/postgresql/data/pgdata `
# >> -v pgvolume:/var/lib/postgresql/data `
# >> -p 5532:5432 `
# >> --name pgvector `
# >> agnohq/pgvector:16

db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"
db = PostgresDb(db_url)

agent = Agent(
    model=OpenAIChat(id="gpt-5-nano"),
    tools=[YFinanceTools()],
    instructions="Voce é um especialista em investimentos e deve me ajudar consultando ações no mercado financeiro",
    db=db,
    # add_history_to_context=True,
    enable_user_memories=True,
    add_memories_to_context=True,
)

# agent.print_response(
#     "Eu prefiro minhas respostas em tabelas",
#     stream=True,
#     session_id="session_id",
#     user_id="preta_user",
# )

# agent.print_response(
#     "Qual a cotação da Apple?",
#     stream=True,
#     session_id="session_id",
#     user_id="preta_user",
# )


# agent.print_response(
#     "Eu prefiro minhas resposta simples e diretas",
#     stream=True,
#     session_id="session_id",
#     user_id="apple_user",
# )

agent.print_response(
    "Qual a cotação da Apple?",
    stream=True,
    session_id="session_id",
    user_id="apple_user",
)
