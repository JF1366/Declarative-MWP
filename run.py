# -*- coding = utf-8 -*-
# @Time : 2023/10/26 10:00
# @Author : JF Huang
# @File : test02.py
# @Software : PyCharm

from prompts.cot_prompt_eight_shot import COT_PROMPT_EIGHT_SHOT
from prompts.cot_prompt_three_shot import COT_PROMPT_THREE_SHOT
from prompts.pal_prompt_three_shot import PAL_PROMPT_THREE_SHOT
# 方法1:
from utils import *
from prompts.declarative_three_shot import DECLARATIVE_THREE_SHOT_AND_PRINCIPLES, DECLARATIVE_THREE_SHOT, \
    DECLARATIVE_THREE_SHOT_AND_PRINCIPLES_CODEX_SOLVE

import openai
openai.api_key = 'Your_API_Key'
openai.proxy = "http://localhost:7890"

question = "The average of four numbers is 8, and if you change one of them to 1, the average of the four numbers is 6. What is the number that was changed?"
# question = "有四个数的平均数是8，若把其中一个数改为1，则这四个数的平均数是6。这个被改动的数是多少?"
# question = "普通客车原来每小时行75千米，提速后，每小时比原来快15千米，要行驶原来6小时行的路程，现在缩短了几个小时?"
# question = 'There are 15 trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be 21 trees. How many trees did the grove workers plant today?'
# question = 'Mary had 5 apples. The next morning, she ate 2 apples. Then, in the afternoon, she bought as many apples as she had after eating those apples in the morning. How many apples did she end up with?'
# question = 'Bob says to Alice: if you give me 3 apples and then take half of my apples away, then I will be left with 13 apples. How many apples do I have now?'
# eq_list = get_declarative_equations(model='text-davinci-003', question=question, prompt=DECLARATIVE_THREE_SHOT_AND_PRINCIPLES, max_tokens=600, stop_token='\n\n\n', temperature=0)
# eq_list = get_declarative_equations(model='text-davinci-003', question=question, prompt=DECLARATIVE_THREE_SHOT, max_tokens=600, stop_token='\n\n\n', temperature=0)
eq_list = get_declarative_equations(model='text-davinci-003', question=question, prompt=COT_PROMPT_THREE_SHOT, max_tokens=600, stop_token='\n\n\n', temperature=0)
answer = get_final_using_sympy(eq_list)
print(answer)


# # 方法2:
# import time
# import requests
#
# proxies = {
#     "http": "http://localhost:7890",
#     "https": "http://localhost:7890"
# }
#
#
# def call_gpt4_api(messages, temperature=0.1):
#     # API接口的URL
#     url = "https://research-cm.openai.azure.com/openai/deployments/GPT432K/chat/completions?api-version=2023-05-15"
#     api_key = "7203ffbaecc147ca8bbd01ed323a16b9"
#
#     # 设置请求头
#     headers = {
#         "Content-Type": "application/json",
#         "api-key": api_key
#     }
#
#     # 请求的数据
#     data = {
#         "messages": messages,
#         "temperature": temperature
#     }
#
#     # 发送POST请求
#     response = requests.post(url=url, headers=headers, json=data, proxies=proxies)
#
#     # 检查响应状态
#     if response.status_code == 200:
#         return response.json()["choices"][0]["message"]["content"].strip()
#     else:
#         print(f"Error: {response.status_code}")
#         print(response.text)
#         return None
#
#
# if __name__ == "__main__":
#     start_time = time.time()
#     # question = 'four plus fifteen is ?'
#     # question = 'Bob says to Alice: if you give me 3 apples and then take half of my apples away, then I will be left with 13 apples. How many apples do I have now?'
#     # question = 'Mary had 5 apples. The next morning, she ate 2 apples. Then, in the afternoon, she bought as many apples as she had after eating those apples in the morning. How many apples did she end up with?'
#     # eq_list = get_declarative_equations(model='text-davinci-003', question=question, prompt=DECLARATIVE_THREE_SHOT_AND_PRINCIPLES, max_tokens=600, stop_token='\n\n\n', temperature=0)
#     # answer = get_final_using_sympy(eq_list)
#     question = 'one plus ninety is equal to?' # 91
#
#     answer = call_gpt4_api([{"role": "system", "content": question}], 0)
#     # answer = call_gpt4_api([{"content": question}], 0.1)
#     print("timeUse: ", time.time() - start_time, "seconds")
#     print(answer)

