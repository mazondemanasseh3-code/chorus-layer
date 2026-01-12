import openai

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
Reason about processes, rules, or inventory.
Flag uncertainty clearly.
""",

        "Communication Agent": f"""
You are a Communication Agent.
Task: {task}
Context: {context}
Draft a professional message.
DO NOT send it. Draft only.
"""
    }

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompts[agent_name]}]
    )

    return response["choices"][0]["message"]["content"]
