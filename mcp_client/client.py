import asyncio
from langchain_core.messages import SystemMessage, HumanMessage
import uuid
from messages import ENGLISH_CHAT, PORTUGUESE_CHAT
from utils import select_language
from agent import create_mcp_agent

async def run_agent_loop():
    agent = await create_mcp_agent()

    language = select_language()
    
    content = f"""
                You are a helpful and friendly assistant that provides information about cars.
                You can use the "cars" tool to get information about a specific car.
                Show the answer in {language} and in a friendly and helpful way, based on the response of the tools..
              """ 

    system_message = SystemMessage(content=content)
    messages = [system_message]

    print(ENGLISH_CHAT if language == "English" else PORTUGUESE_CHAT)
    
    conversation_id = str(uuid.uuid4())
    while True:
        user = input("👤 User: " if language == "English" else "👤 Usuário")
        if user.strip().lower() in {"exit","sair","quit"}:
            break
        user = user.encode('utf-8', 'ignore').decode('utf-8')
        messages.append(HumanMessage(content=f"{user}\n"))
        
        resp = await agent.ainvoke({
            "messages":[
                {"role":"user",
                 "content":user}
            ]}, 
            config = {
                "configurable": {
                    "thread_id": conversation_id
                }
            }
        )
        message = resp["messages"]  

        role_names = {
            "human": "👤 Usuário",
            "ai": "🤖 Assistente",
            "unknown": "❓ Desconhecido"
        }
        trole = getattr(message[-1], "type", "unknown")
        role_display = role_names.get(trole, trole)
        if trole == "ai":
            print(f"{role_display}: {message[-1].content}\n")

if __name__ == "__main__":
    try:
        asyncio.run(run_agent_loop())
    except KeyboardInterrupt:
        print("\nEncerrando o chat. Até mais!")

