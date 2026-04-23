from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

# 创建模型对象
model = ChatTongyi(model="qwen3-max")

# 消息列表
messages = [
    SystemMessage(content="你是一名边塞诗人"), # 系统角色
    HumanMessage(content="帮我写一首诗"), # 用户角色
    AIMessage(content="锄禾日当午，汗滴禾下土，谁知盘中餐，粒粒皆辛苦。"), # 模拟ai回答
    HumanMessage(content="按照如上格式帮我写一首诗")
]
'''
# 消息的简写形式：二元组(角色，内容)，角色只有：system、human、ai
messages = [
    ("system", "你是一名边塞诗人"), # 系统角色
    ("human", "帮我写一首诗"), # 用户角色
    ("ai", "锄禾日当午，汗滴禾下土，谁知盘中餐，粒粒皆辛苦。"), # 模拟ai回答
    ("human", "按照如上格式帮我写一首诗")
]
'''

# 流式输出
res = model.stream(input = messages)

for chunk in res:
    print(chunk.content, end="", flush=True)