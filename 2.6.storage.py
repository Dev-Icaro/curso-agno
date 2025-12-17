from agno.agent import Agent
from agno.tools.yfinance import YFinanceTools
from agno.models.groq import Groq
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
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools()],
    instructions="Responda sempre utilizando uma tabela",
    db=db,
    add_history_to_context=True,
)

agent.print_response(
    "Quais foram as ações já cotadas durante nossa sessão?",
    stream=True,
    session_id="session_id",
)
