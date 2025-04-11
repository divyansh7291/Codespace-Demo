from crewai import Agent, Task, Crew
from openai import OpenAI
import os

def run_sales_agent(lead_info: str):
    from langchain.llms import OpenAI as LangOpenAI

    agent = Agent(
        role="Sales Email Expert",
        goal="Write a personalized cold outreach email to convert the lead",
        backstory="You are an expert sales copywriter who writes converting emails.",
        verbose=True,
        allow_delegation=False,
        llm=LangOpenAI(temperature=0.7)
    )

    task = Task(
        description=f"Write a personalized cold email for this lead:\n\n{lead_info}",
        expected_output="An effective sales email",
        agent=agent
    )

    crew = Crew(
        agents=[agent],
        tasks=[task],
        verbose=True
    )

    result = crew.kickoff()
    return result
