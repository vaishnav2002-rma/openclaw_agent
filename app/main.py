from app.agent.orchestrator import Orchestrator
from app.output.formatter import format_output


def run(query):
    agent = Orchestrator()
    memory = agent.run(query)

    final_output = format_output(memory, query)

    with open("output.json", "w", encoding="utf-8") as f:
        f.write(final_output)

    print("\n===== FINAL OUTPUT =====\n")
    print(final_output)
