from agno.agent import Agent 

from agno.models.openai import OpenAIReesponses 

from agno.models.groq import Groq
from agno.tools.yfinance import YFinanceTools

load_dotenv()

def build_agent():
return Agent(

model = OpenAIRsponses(id="gpt-5-mini"),
tools = [YFinanceTools()],
markdown = True,
instructions = "You are a investment analystys that researches "
)

open_agent = build_agent()

open_agent.print_response("Share the NVDA stoc price and analysts recomanaded")