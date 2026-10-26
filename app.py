from uuid import uuid4

from agent import get_agent


agent = get_agent()
thread_id = str(uuid4())

print("\n📧 ===== GMAIL AI AGENT =====")
print("🤖 Your Personal Email Assistant")
print("🚀 Agent is Ready!")
print("Type 'quit' or 'exit' to end the conversation.\n")

while True:

    try:
           user_input = input("You: ").strip()
    except (EOFError, KeyboardInterrupt):
            print("\nChat ended.")
            break

    if not user_input:
            print("Please enter a message.")
            continue

    if user_input.lower() in ["quit", "exit"]:
            print("Chat ended.")
            break

    response = agent.invoke(
            {"messages": [{"role": "user", "content": user_input}]},
            config={"configurable": {"thread_id": thread_id}},
        )
    messages = response.get("messages", [])
    if not messages:
        raise RuntimeError("The agent returned no messages.")

    reply = messages[-1].content
    print(f"Agent: {reply}\n")



