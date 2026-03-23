from app.agent.planner import decide
from app.agent.executor import execute
from app.memory.short_term import Memory


class Orchestrator:
    def __init__(self):
        self.memory = Memory()
        self.visited_urls = set()

    def run(self, query, max_steps=5):
        context = f"Research target: {query}"

        for step in range(max_steps):
            print(f"\n[Step {step+1}]")

            action = decide(context)
            print("Action:", action)

            result = execute(action)

            if result["type"] == "search":
                context += f"\nSearch results: {result['data']}"

            elif result["type"] == "open":
                url = result["url"]

                if url in self.visited_urls:
                    continue

                self.visited_urls.add(url)
                self.memory.add(result)

                context += f"\nExtracted: {result['data'][:500]}"

            elif result["type"] == "finish":
                print("Finishing research...")
                break

        return self.memory.get_all()
