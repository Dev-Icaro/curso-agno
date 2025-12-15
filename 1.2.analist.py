from agno.agent import Agent
from agno.tools.yfinance import YFinanceTools
from agno.models.groq import Groq
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools()],
    instructions="Responda sempre utilizando uma tabela",
)

agent.print_response(
    "Use suas ferramentas para buscar a cotação do banco do Brasil", stream=True
)
