from swarm import Swarm, Agent

client = Swarm()

jarvis = Agent(
    name="Jarvis",
    instructions="""
    You are Jarvis, a coding assistant. When the user asks for a program,
    respond with the full Python script. Do not include any explanations.
    """,
)

if __name__ == "__main__":
    prompt = "Write a Python script that prints Hello, world!"
    messages = [{"role": "user", "content": prompt}]
    response = client.run(agent=jarvis, messages=messages)
    print(response.messages[-1]["content"])
