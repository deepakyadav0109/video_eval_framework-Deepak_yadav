# video_eval_framework-Deepak_yadav
# LLM-based Video Evaluation Framework

This project offers a lightweight, modular framework for evaluating video content using Large Language Models (LLMs). It analyzes the optical flow of a video and uses a prompt-driven approach to generate a professional evaluation report through OpenAI’s GPT-based API.

---
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

Copy the example environment file and update it with your OpenAI API key:

cp .env.example .env

Then edit .env and add:

OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

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
 
	•	Pass it with your criteria and prompt to the LLM.
 
	•	Print the natural language evaluation report to the terminal.
 

