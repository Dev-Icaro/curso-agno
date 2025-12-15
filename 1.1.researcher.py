from agno.agent import Agent
from agno.tools.tavily import TavilyTools
from agno.models.groq import Groq
from dotenv import load_dotenv
from agno.models.openai import OpenAIChat

load_dotenv()


def celsius_to_fahrenheit(celsius: float):
    """
    Convert a temperature from Celsius to Fahrenheit.

    Args:
        celsius (float): Temperature in degrees Celsius.

    Returns:
        float: Temperature converted to degrees Fahrenheit.
    """
    return (celsius * 9 / 5) + 32


agent = Agent(
    # model=Groq(id="llama-3.3-70b-versatile"),
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[TavilyTools(), celsius_to_fahrenheit],
)

agent.print_response(
    "Use suas ferramentas para buscar quantos graus estão em São Paulo hoje e depois converter para Fahrenheit"
)
