from swarm import Agent
from swarm.repl import run_demo_loop

jarvis = Agent(
    name="Jarvis",
    instructions="You are Jarvis, Tony Stark's helpful AI assistant. Respond politely and helpfully to the user."
)

if __name__ == "__main__":
    run_demo_loop(jarvis)
