
"""
注意：
1. 请替换API_KEY为自己的私有密钥，私有密钥暂不公开。
2. 请替换API_URL为自己的API地址。
3. 请确保已安装ttkthemes库，并将主题设置为"radiance"。
4. 请确保已安装requests库。
5. 请确保已安装tkinter库。
6. 请确保已安装scrolledtext库。
7. 请确保已安装ttk库。
8. 请确保已安装json库。
9. 请确保已安装Microsoft YaHei字体。
10. 请确保已安装Python 3.x环境。
11. 请确保已安装IDLE编辑器。       
更多注释请查看：https://xgouo.cn/ai2.html """

import tkinter as tk
from tkinter import scrolledtext
from ttkthemes import ThemedTk
from tkinter import ttk
import requests
import json

# API配置
API_URL = "https://api.openai-hk.com/v1/chat/completions"#国内不允许接入openai，这是我选择的一个中转站
API_KEY = "hk-ha558u100001416706b28dabe9e4480cecda26d21746c3f0"#私有密钥暂不公开
# 定义发送消息的函数
def send_message():
    user_message = user_input.get()
    if not user_message.strip():
        return
    # 显示用户输入的消息
    chat_window.config(state='normal')
    chat_window.insert(tk.END, f"You: {user_message}\n", 'user')
    chat_window.yview(tk.END)
    chat_window.config(state='disabled')
    send_button.config(state='disabled')
    root.update_idletasks()

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-3.5-turbo",  # 替换模型
        "messages": [{"role": "user", "content": user_message}]
    }
    try:
        response = requests.post(API_URL, headers=headers, json=data)
        response_data = response.json()

        # 显示AI的回复
        chat_window.config(state='normal')
        if "choices" in response_data and response_data["choices"]:
            ai_message = response_data["choices"][0]["message"]["content"]
            chat_window.insert(tk.END, f"AI: {ai_message}\n", 'ai')
            chat_window.yview(tk.END)
        else:
            chat_window.insert(tk.END, "AI: 我不知道你在说什么\n", 'error')
    except Exception as e:
        chat_window.insert(tk.END, f"Error: {str(e)}\n", 'error')
        chat_window.yview(tk.END)
    finally:
        chat_window.config(state='disabled')
        send_button.config(state='normal')
        user_input.delete(0, tk.END)
# 主程序
root = ThemedTk(theme="radiance")# 设置主题
root.title("AI---对话")# 设置窗口标题
root.geometry("700x600")# 设置窗口大小

# 窗口居中
window_width = root.winfo_reqwidth()# 获取窗口宽度
window_height = root.winfo_reqheight()# 获取窗口高度
position_right = int(root.winfo_screenwidth()/2 - window_width/2)
position_down = int(root.winfo_screenheight()/2 - window_height/2)
root.geometry(f"+{position_right}+{position_down}")# 设置窗口位置

# 设置支持中文的字体
chinese_font = ("Microsoft YaHei", 10, "normal")
chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled', font=chinese_font)
chat_window.pack(pady=10)

# 配置文本显示风格
chat_window.tag_configure('user', foreground='blue', font=chinese_font)
chat_window.tag_configure('ai', foreground='green', font=chinese_font)
chat_window.tag_configure('error', foreground='red', font=chinese_font)
# 输入框与按钮的字体设置
user_input = ttk.Entry(root, font=chinese_font)# 创建输入框
user_input.focus()# 自动获取焦点
user_input.pack(fill=tk.X, padx=10, pady=5)
send_button = ttk.Button(root, text="发送", command=send_message, style="Accent.TButton")# 创建按钮
send_button.pack(pady=5)
# 绑定回车键到发送功能
root.bind('<Return>', lambda event: send_message())
root.mainloop()
"""
参考：
openai-python文档：
    https://github.com/openai/openai-python
openai-python API文档：
    https://beta.openai.com/docs/api-reference/introduction
腾讯混元大模型接入文档：
    https://cloud.tencent.com/document/product/1729/111007
    https://cloud.tencent.com/document/product/1729/101848
openai-hk接入文档：
    https://www.openai-hk.com/docs/getting-started.html#python-%E5%AE%9E%E4%BE%8B
学术优化ai工具：
    https://github.com/binary-husky/gpt_academic
菜鸟教程：
    https://www.runoob.com/python/python-gui-tkinter.html
"""