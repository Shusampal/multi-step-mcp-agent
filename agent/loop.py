from agent.state import *
from agent.mcp_client import *
from agent.planner import planner
from agent.formatter import format_answer
from agent.executor import execute_action


def build_tool_descriptions(tools):
    descriptions = ""

    for tool in tools:
        descriptions += f"""
        Tool:
        {tool.name}
        Description:
        {tool.description}
        """
    return descriptions


async def run_agent_loop(user_request):

    # Step1 get all mcp tools
    client = await connect()
    tools = await discover_tools(client)
    tool_descriptions = build_tool_descriptions(tools)

    # Step2 create initial state
    state = create_state(user_request)

    # Step3 Loop starts
    while can_continue(state):
        action = planner(state, tool_descriptions)
        print("Planner selected: ", action)
        if action == "FINISH":
            answer = format_answer(state)
            finish(state, answer)
            break

        observation = await execute_action(action, client)

        add_action(state, action)
        record_observation(state, action, observation)
        next_step(state)

    return state
