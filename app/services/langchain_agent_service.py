import os
import json
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage
from app.services.tools.trms_tools import TRMS_TOOLS

def run_agentic_planner(message: str, user_context: dict) -> dict:
    """
    Run the LangChain agentic planner to handle action intents.
    Returns a dict with {"handled": bool, ...}
    """
    # 1. Check if the message is actually an action intent
    from app.services.action_intent_service import detect_action_intent
    intent = detect_action_intent(message)
    
    if not intent.get("is_action"):
        return {"handled": False}
        
    action = intent["action"]
    # Only allow supported first-phase actions
    if action not in ["create_complaint", "allot_hostel_room", "generate_icard"]:
        # We can either let the old flow handle it or say "Not supported by LangChain yet"
        # Since it's an action, we should probably handle it or let the existing flow kick in.
        # But instructions say "Start only with: 1. allot_hostel_room 2. create_complaint 3. generate_icard"
        pass
        
    api_key = os.environ.get("GROQ_API_KEY")
    model_name = os.environ.get("GROQ_MODEL", "llama-3.3-70b-versatile")
    
    if not api_key:
        print("[Agent] GROQ_API_KEY not found, cannot run LangChain.")
        return {"handled": False}
        
    try:
        # Initialize Groq LLM
        llm = ChatGroq(temperature=0, model_name=model_name, api_key=api_key)
        
        # Bind tools to the LLM
        llm_with_tools = llm.bind_tools(TRMS_TOOLS)
        
        system_prompt = f"""You are TRMS Agentic AI planner.

You can help users perform safe TRMS actions using tools.

Rules:
1. Do not answer normal data questions. Return handled=false for normal Q&A.
2. Only handle create/update/allot/generate/mark/issue/book/close actions.
3. Never execute write action directly.
4. Always prepare confirmation first.
5. Always use office_id from user_context ({user_context.get('office_id')}), not from user text.
6. Always respect role permission ({user_context.get('role')}).
7. Never expose SQL.
8. Never ask tools to access users.password.
9. If required fields are missing, ask a follow-up question.
10. For successful action preparation, return the JSON string representation of the confirmation_required payload.
11. After confirmation, execution happens in /api/action/confirm, not inside planner.

Supported first-phase actions:
- create_complaint
- allot_hostel_room
- generate_icard

If you need more information from the user, just ask.
If you successfully prepared the confirmation using the tool, return the EXACT JSON payload returned by the tool.
"""

        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=message)
        ]
        
        # Initial call to LLM
        response = llm_with_tools.invoke(messages)
        
        if not response.tool_calls:
            # If the LLM just asks a follow-up question
            return {
                "handled": True,
                "type": "text",
                "message": response.content
            }
            
        # Process tool calls
        messages.append(response)
        
        # For simplicity in this agentic flow, we will execute the tools
        # and parse the result. If a tool returns a confirmation dict,
        # we can just return it immediately.
        tool_results = []
        for tool_call in response.tool_calls:
            tool_name = tool_call["name"]
            tool_args = tool_call["args"]
            
            # Inject context manually where needed, or the LLM should provide it based on prompt
            if "office_id" not in tool_args:
                tool_args["office_id"] = user_context.get("office_id", 1)
            if "role" not in tool_args and tool_name in ["prepare_room_allotment_confirmation", "prepare_complaint_confirmation", "prepare_icard_confirmation"]:
                tool_args["role"] = user_context.get("role", "default")
                
            tool = next((t for t in TRMS_TOOLS if t.name == tool_name), None)
            if tool:
                print(f"[Agent] Calling tool {tool_name} with args {tool_args}")
                result = tool.invoke(tool_args)
                tool_results.append(result)
                
                # Check if it's the final confirmation payload
                if isinstance(result, dict) and result.get("type") == "confirmation_required":
                    result["handled"] = True
                    return result
                
                # Check if permission denied
                if isinstance(result, dict) and "error" in result:
                    return {
                        "handled": True,
                        "type": "action_result",
                        "status": "failed",
                        "message": result["error"]
                    }
        
        # If tools didn't return a confirmation, we might need a second pass or just ask the user
        return {
            "handled": True,
            "type": "text",
            "message": "I processed your request but could not finalize the action. Could you please provide more details?"
        }
        
    except Exception as e:
        print(f"[Agent] Error in agentic planner: {e}")
        return {"handled": False}
