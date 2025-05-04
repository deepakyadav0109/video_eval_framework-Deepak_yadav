# video_eval_framework-Deepak_yadav
# LLM-based Video Evaluation Framework

This project offers a Multi-Agent System to qauantitatively and Qualitatively assess video content and generates Report using Large Language Models (LLMs). It analyzes the optical flow of a video and uses a prompt-driven approach to generate a professional evaluation report through OpenAI’s GPT-based API.

---

## 🛠️ Requirements

- [Docker](https://www.docker.com/)
- OpenAI API Key (get one at https://platform.openai.com/account/api-keys)

---
# 📹 Video Evaluation Framework

A modular, multi-agent system for qualitative and quantitative video assessment using advanced computer vision, multimodal AI models, and LLM-driven reporting.

## 🚀 Overview

This framework evaluates videos through a **three-stage pipeline**:

1. **Perception Analysis**  
   Computes optical flow to measure **temporal coherence**, detecting jittery or unstable motion in videos.

2. **Semantic Reasoning**  
   Uses the **CLIP model** to score frame-to-text semantic alignment and detects **scene transitions**.

3. **LLM-Based Reporting**  
   Summarizes computed metrics into a **natural language report** using an LLM (e.g., ChatGPT or TinyLlama).

All components are orchestrated using **LangGraph**, with modular agents communicating via **shared memory** and configuration-driven logic using a `criteria.json` file.

---

## 🧠 Key Features

- 🔄 **Temporal Coherence Detection**: Calculates motion smoothness using dense optical flow (Farneback method).
- 🧠 **Semantic Alignment**: Leverages CLIP to ensure video frames stay on-topic based on user prompts.
- ✂️ **Scene Transition Detection**: Detects abrupt scene changes using pixel-wise difference thresholds.
- 📝 **Natural Language Report**: Uses an LLM to convert metrics into a stakeholder-friendly evaluation report.
- ⚙️ **JSON-Based Configuration**: Flexible evaluation criteria through an easy-to-edit `criteria.json` file.
- 🧩 **Agent-Based Modular Design**: Scalable and extensible architecture with clear task separation.

---

## 🛠️ Requirements

- [Docker](https://www.docker.com/)
- OpenAI API Key (get one at https://platform.openai.com/account/api-keys)

---


## 🚀 Setup Instructions

1. Clone the Repository

git clone https://github.com/deepakyadav0109/video_eval_framework-Deepak_yadav.git

cd video_eval_framework-Deepak_yadav


2. Add Your API Key

Make a new file with name .env in the root

Then add:

OPENAI_API_KEY= "your_actual_openai_api_key"

3. Modify Inputs in main.py

Open main.py and edit the input_state dictionary:

(i) Replace the video path with your actual video path.

(ii) Replace the criteria.json with your own criteria.json file

(iii) Change the prompt according to requirements for checking the semantic similarity of video with this prompt.


4. Build the Docker Image
   
Run the command:
docker-compose build

5. Run the Framework
   
Run the command:
docker-compose up

The system will:

	•	Process the video to compute optical flow.
 
	•	Pass it with your criteria and prompt to the Reasoning agent.
 
	•	The results will be passed on to LLM to generate Quantitative + Qualitative Assessment (Report).

 	•	Print the natural language evaluation report to the terminal..
 

