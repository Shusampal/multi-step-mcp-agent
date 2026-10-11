import asyncio
from agent.loop import run_agent_loop

print("=" * 40)
print("Multi Step AI Agent With MCP")
print("=" * 40)


async def main():

    while True:
        user_request = input("USER: ").strip().lower()

        if user_request in ["exit", "bye", "quit"]:
            print("AI: GoodBye !!")
            break

        result = await run_agent_loop(
            user_request
        )

        print("AI: ", result["final_answer"])


if __name__ == "__main__":
    asyncio.run(main())
