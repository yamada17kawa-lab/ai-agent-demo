from typing import Dict, Any, Optional, List
from uuid import UUID

from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.callbacks import BaseCallbackHandler
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.tools import tool
from langchain_ollama import ChatOllama

class MyCallBack(BaseCallbackHandler):
    def on_tool_start(
        self,
        serialized: Dict[str, Any],
        input_str: str,
        *,
        run_id: UUID,
        parent_run_id: Optional[UUID] = None,
        tags: Optional[List[str]] = None,
        metadata: Optional[Dict[str, Any]] = None,
        inputs: Optional[Dict[str, Any]] = None,
        **kwargs: Any,
    ) -> Any:
        print("MyCallBack on_tool_start")
        print(input_str)

    def on_tool_end(
        self,
        output: Any,
        *,
        run_id: UUID,
        parent_run_id: Optional[UUID] = None,
        **kwargs: Any,
    ) -> Any:
        print("MyCallBack on_tool_end")
        print(output)

chatModel = ChatOllama(model="llama3.1:8b", temperature=0)

chatPrompt = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一名全能助手，可以调用工具回答问题"),
        ("human", "{question}"),
        # 必须包含这个占位符，用于记录中间思考过程
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ]
)

# 工具方法必须加上描述，不然模型不知道方法是干什么的
@tool()
def get_weather(city: str):
    """查询指定城市的实时天气情况。"""
    return f"{city}的天气是晴朗"

@tool
def get_temperature(city: str):
    """查询指定城市的实时温度。"""
    return f"{city}的温度是22℃"

#如果方法不需要传参，需要在方法中表明为None，比如query: str = None
@tool
def get_weight(query: str = None):
    """获取体重"""
    return "55公斤"

@tool
def get_hight(query: str = None):
    """获取身高"""
    return "1.68m"



tools = [get_weather, get_temperature, get_weight, get_hight]

myAgent = create_tool_calling_agent(chatModel, tools, chatPrompt)

myCallBack = MyCallBack()

agentExecutor = AgentExecutor(
    agent=myAgent,
    tools=tools,
    verbose=True,
    handle_parsing_errors=True,
    callbacks=[myCallBack], #agent加上回调配置
)

# results = agentExecutor.stream({"question": "分别查询今天广西的天气和温度怎么样？"})

#输出里也要加上回调配置
results = agentExecutor.stream({"question": "算出我的BMI是多少"},
                               {"callbacks": [myCallBack]} )

for result in results:
    if result is not None and len(result) > 0:
        print(result)
    if "output" in result:
        print("=" * 20)
        print(result["output"])



