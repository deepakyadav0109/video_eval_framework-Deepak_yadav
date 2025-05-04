from typing import TypedDict, Optional, Dict, Any

class VideoEvalState(TypedDict):
    video_path: str
    criteria: Dict[str, Any]
    prompt: str
    perception_key: Optional[str]
    reasoning_key: Optional[str]
    report_summary: Optional[str]