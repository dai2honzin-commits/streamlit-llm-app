from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage, AIMessage
llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

import streamlit as st
st.title("LLM App")

st.markdown("""
### アプリ概要
このWebアプリは、Fishing（釣り）またはTrekking（トレッキング）の専門家AIに質問できるチャットサービスです。

### 操作方法
1. 質問相手（専門家）をラジオボタンで選択してください。
2. 質問内容をテキスト入力欄に入力してください。
3. 「実行」ボタンを押すと、選択した専門家AIが回答します。

---
""")

st.write("##### 質問相手1: Fishingの専門家")
st.write("入力フォームにテキストを入力し、「実行」ボタンを押すことで質問ができます。")
st.write("##### 質問相手2: Trekkingの専門家")
st.write("入力フォームにテキストを入力し、「実行」ボタンを押すことで質問ができます。")

def get_llm_response(input_text, selected_expert):
    
    if selected_expert == "Fishingの専門家":
        messages = [
            SystemMessage(content="あなた釣りの専門家です。"),
            HumanMessage(content=input_text),
        ]
    elif selected_expert == "Trekkingの専門家":
        messages = [
            SystemMessage(content="あなたはトレッキングの専門家です。"),
            HumanMessage(content=input_text),
        ]
    else:
        return "専門家が選択されていません。"
    result = llm(messages)
    return result.content

selected_item = st.radio(
    "質問相手を選択してください。",
    ["Fishingの専門家", "Trekkingの専門家"]
)

st.divider()
input_message = st.text_input(label="質問を入力してください。")

if st.button("実行"):
    st.divider()
    if input_message:
        with st.spinner(f"{selected_item}が考え中..."):
            response = get_llm_response(input_message, selected_item)
            st.write(f"回答: {response}")
    else:
        st.error("質問を入力してください。")
            