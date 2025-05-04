from agents.perception_agent import PerceptionAgent
from state_schema import VideoEvalState
from shared_memory import shared_data

def perception_node(state: VideoEvalState) -> VideoEvalState:
    result = PerceptionAgent(
        state["video_path"],
        state["criteria"].get("perception", {})
    ).run()
    shared_data["perception_output"] = result
    return {
        **state,
        "perception_key": "perception_output"
    }