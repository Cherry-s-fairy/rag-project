# 1. 导入模型LangChain包
from langchain_community.llms.tongyi import Tongyi
# 2. 创建模型对象
model = Tongyi(model="qwen-max")
# # invoke：一次性返回完整结果
# # 3. 调用模型
# res = model.invoke(input="你是一个什么大模型？")
# # 4. 输出结果
# print(res)
# stream：流式输出
res = model.stream(input="你是一个什么大模型")
for chunk in res:
    print(chunk, end="", flush=True)