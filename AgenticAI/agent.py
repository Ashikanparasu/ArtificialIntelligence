from agno.agent import Agent 

from agno.models.openai import OpenAIReesponses 

 from agno.models.groq import Groq

def build_agent():
return Agent(

model = OpenAIRsponses(id="gpt-5-mini"),
markdown = True,
instructions = "You are a helpful and expect travel agent "
)

open_agent = build_agent()

open_agent.print_response("My budget is 1l Inr, Should i travel goa or phuket?)