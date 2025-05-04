import json
from langgraph.graph import StateGraph, END
from state_schema import VideoEvalState
from nodes.perception_node import perception_node
from nodes.reasoning_node import reasoning_node
from nodes.reporting_node import reporting_node

from dotenv import load_dotenv
load_dotenv()

def build_graph():
    graph = StateGraph(VideoEvalState)
    graph.set_entry_point("perception")

    graph.add_node("perception", perception_node)
    graph.add_node("reasoning", reasoning_node)
    graph.add_node("reporting", reporting_node)

    graph.add_edge("perception", "reasoning")
    graph.add_edge("reasoning", "reporting")
    graph.add_edge("reporting", END)

    return graph.compile()

if __name__ == "__main__":
    # Load criteria.json
    with open("criteria.json", "r") as f:
        criteria = json.load(f)

    app = build_graph()

    input_state = {
        "video_path": "your_video.mp4",
        "criteria": criteria,
        "prompt": "a person walking under rain"
    }

    result = app.invoke(input_state)

    print("\n Full Evaluation Completed!\n")
    print(" Final Report Summary:\n", result["report_summary"])