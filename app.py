import gradio as gr
def greet(name):
    return "正在处理 https 域名问题，目前可在 http://101.133.161.204:18444/ 体验效果"
iface = gr.Interface(fn=greet, inputs="text", outputs="text")
iface.launch()
