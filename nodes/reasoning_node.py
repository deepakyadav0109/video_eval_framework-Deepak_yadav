from agents.reasoning_agent import ReasoningAgent
from state_schema import VideoEvalState
from shared_memory import shared_data

def reasoning_node(state: VideoEvalState) -> VideoEvalState:
    _ = shared_data.get(state["perception_key"])
    result = ReasoningAgent(
        "frames",
        state["prompt"],
        state["criteria"].get("reasoning", {})
    ).run()
    shared_data["reasoning_output"] = result
    return {
        **state,
        "reasoning_key": "reasoning_output"
    }