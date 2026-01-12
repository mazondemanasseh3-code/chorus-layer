import streamlit as st
from director import generate_workflow
from agents import run_agent

st.set_page_config(page_title="Chorus Layer", layout="wide")
st.title("Chorus Layer — AI Operations Manager")

if "workflow" not in st.session_state:
    st.session_state.workflow = None

if "logs" not in st.session_state:
    st.session_state.logs = []

user_goal = st.text_area(
    "What do you want the AI team to do?",
    height=200,
    placeholder="Example: Respond to a new Instagram DM asking about available dining tables."
)

if st.button("Generate Plan"):
    if user_goal.strip():
        st.session_state.workflow = generate_workflow(user_goal)
        st.session_state.logs = []

if st.session_state.workflow:
    st.subheader("🧠 Director Plan")
    st.json(st.session_state.workflow)

    if st.button("Run Workflow"):
        context = user_goal

        for step in st.session_state.workflow["workflow"]:
            agent = step["agent"]
            task = step["task"]

            output = run_agent(agent, task, context)

            st.session_state.logs.append({
                "agent": agent,
                "task": task,
                "output": output,
                "requires_approval": step["requires_approval"]
            })

            if step["requires_approval"]:
                st.warning("Human Approval Required")
                st.write(output)
                approved = st.button("Approve & Continue")
                if not approved:
                    st.stop()

            context += f"\n{output}"

    st.subheader("📜 Execution Audit Log")

    for log in st.session_state.logs:
        st.markdown(f"### {log['agent']}")
        st.write("**Task:**", log["task"])
        st.write("**Output:**", log["output"])

