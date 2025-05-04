from agents.reporting_agent import ReportingAgent
from state_schema import VideoEvalState
from shared_memory import shared_data

def reporting_node(state: VideoEvalState) -> VideoEvalState:
    perception_result = shared_data.get(state["perception_key"])
    reasoning_result = shared_data.get(state["reasoning_key"])
    summary = ReportingAgent(
        perception_result,
        reasoning_result,
        state["criteria"].get("reporting", {})
    ).run()
    return {
        **state,
        "report_summary": summary
    }