import os
from agno.agent import Agent
from agno.db.postgres import PostgresDb
from agno.knowledge import Knowledge
from agno.models.openai import OpenAIChat
from dotenv import load_dotenv
from agno.vectordb.chroma import ChromaDb
from agno.knowledge.embedder.openai import OpenAIEmbedder
from agno.knowledge.reader.pdf_reader import PDFReader
from agno.knowledge.chunking.semantic import SemanticChunking
from openai.types.shared import metadata

load_dotenv()

db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"
db = PostgresDb(db_url)

vector_db = ChromaDb(
    collection="empresas_relatorios",
    path="tmp/chroma",
    embedder=OpenAIEmbedder(
        id="text-embedding-3-small", api_key=os.getenv("OPENAI_API_KEY")
    ),
    persistent_client=True,
)

knowledge = Knowledge(
    vector_db=vector_db,
)

knowledge.add_content(
    path="files/petrobras/",
    reader=PDFReader(chunking_strategy=SemanticChunking()),
    skip_if_exists=True,
    metadata={
        "company": "Petrobras",
        "sector": "Petróleo e Gás",
        "year": 2025,
        "country": "Brazil",
    },
)

agent = Agent(
    name="Analista Financeiro",
    model=OpenAIChat(id="gpt-5-nano"),
    instructions="Você é um especialista em análise de relatórios financeiros e deve me ajudar a analisar o relatório da Petrobras",
    knowledge=knowledge,
    add_knowledge_to_context=True,
)

agent.print_response(
    "Qual foi a produção média de óleo, LGN e gás natural da pretrobras e qual foi seu aumento em relação ao 2T25?",
    session_id="session_id",
    user_id="user_id",
)
