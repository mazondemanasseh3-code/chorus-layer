from openai import OpenAI
import streamlit as st

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])


client = OpenAI()

def generate_workflow(user_goal):
    prompt = f"""
You are the Director Agent in a multi-agent AI system.

Break the user goal into an executable workflow.

Rules:
- Break into ordered tasks
- Assign ONE agent per task
- Identify approval points
- Output JSON ONLY

Available Agents:
- Research Agent
- Operations Agent
- Communication Agent

Output format:
{{
  "workflow": [
    {{
      "task": "",
      "agent": "",
      "risk_level": "low | medium | high",
      "requires_approval": true/false
    }}
  ]
}}

User Goal:
{user_goal}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return json.loads(response.choices[0].message.content)

