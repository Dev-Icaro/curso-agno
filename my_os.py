from doctest import debug
from agno.agent.agent import Agent
from agno.models.openai import OpenAIChat
from agno.os import AgentOS
from agno.tools.tavily import TavilyTools
from dotenv import load_dotenv
from agno.models.groq import Groq

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


research_agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    # model=OpenAIChat(id="gpt-4o-mini"),
    tools=[TavilyTools(), celsius_to_fahrenheit],
)

agent_os = AgentOS(
    name="My AgentOS",
    description="My Multi-Agent Runtime",
    agents=[research_agent],
    # teams=[basic_team],
    # workflows=[basic_workflow],
)

app = agent_os.get_app()

if __name__ == "__main__":
    agent_os.serve(app="my_os:app", reload=True, access_log=True)
