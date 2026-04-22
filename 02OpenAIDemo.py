from openai import OpenAI

# 1. 创建客户端对象
client = OpenAI(
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

# 2. 调用模型
response = client.chat.completions.create(
    model="qwen3.6-plus",
    # messages=[
    #     {"role": "system", "content": "你是一个Python专家，而且从不说废话，简单专业回答"},
    #     {"role": "assistant", "content": "好的，我是不说废话的编程专家，你要问什么？"},
    #     {"role": "user", "content": "使用Python代码输出1-10数字"}
    # ],

    # 附带历史消息调用模型
    messages=[
        {"role": "system", "content": "你是一个AI助理，而且从不说废话"},
        {"role": "user",   "content": "小红有两只狗"},
        {"role": "assistant", "content": "ok"},
        {"role": "user", "content": "小明有三只猫"},
        {"role": "assistant", "content": "ok"},
        {"role": "user", "content": "一共有几只宠物"},
    ],
    stream=True
)

# 3. 处理结果
# print(response.choices[0].message.content)

# 流式输出
for message in response:
    if message.choices[0].delta.content is not None:
        print(
            message.choices[0].delta.content,
            end=" ", # 每段之间以空格分隔，否则以换行符分割
            flush=True # 立刻刷新缓冲区，否则存储在缓冲区中不会立即输出
        )