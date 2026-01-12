from openai import OpenAI

client = OpenAI()

def run_agent(agent_name, task, context):
    prompts = {
        "Research Agent": f"""
You are a Research Agent.
Task: {task}
Context: {context}
Return concise findings only.
""",

        "Operations Agent": f"""
You are an Operations Agent.
Task: {task}
Context: {context}
Reason about internal processes, rules, or logistics.
""",

        "Communication Agent": f"""
You are a Communication Agent.
Task: {task}
Context: {context}
Draft a professional message.
DO NOT send it.
"""
    }

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompts[agent_name]}]
    )

    return response.choices[0].message.content



