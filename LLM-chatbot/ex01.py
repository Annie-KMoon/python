import gradio as gr
import ollama

# 대화 기록 저장용 리스트
chat_history = []

# 시스템 프롬프트 (필요에 따라 수정 가능)
system_prompt = "당신은 친절하고 유용한 한국어 AI 어시스턴트입니다."

# Gradio와 연결할 함수
def chat(user_input, history):
    if len(chat_history) == 0:
        chat_history.append({"role": "system", "content": system_prompt})
    
    chat_history.append({"role": "user", "content": user_input})
    
    response = ollama.chat(
        model="qwen3:1.7b",
        messages=chat_history,
    )
    
    answer = response['message']['content']
    chat_history.append({"role": "assistant", "content": answer})
    
    return answer


# Gradio 인터페이스 정의
iface = gr.ChatInterface(fn=chat, title="Qwen3:1.7b 챗봇 (로컬)", examples=["안녕", "날씨 어때?", "파이썬으로 리스트 정렬하는 법 알려줘"], theme="soft")

# 앱 실행
if __name__ == "__main__":
    iface.launch()
