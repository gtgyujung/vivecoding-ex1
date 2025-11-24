import streamlit as st

st.title("🚀 Hello World 앱 (가로 배치)")

# ---

# 1. 3:1 비율로 두 개의 열(Column)을 생성합니다.
# col1(입력창)은 넓게, col2(버튼)는 좁게 설정합니다.
col1, col2 = st.columns([3, 1])

# 2. 첫 번째 열(col1)에 텍스트 입력창 배치
# label_visibility="collapsed"를 사용하여 입력창 위의 라벨을 숨겨 깔끔하게 만듭니다.
with col1:
    user_name = st.text_input(
        "사용자의 이름을 입력해주세요:", 
        placeholder="예: 미림 학생", 
        label_visibility="collapsed" # 라벨을 숨겨서 버튼과 수평 정렬을 돕습니다.
    )
    
# 3. 두 번째 열(col2)에 버튼 배치
with col2:
    # 버튼이 입력창과 수직으로 잘 정렬되도록 st.button()만 사용합니다.
    button_clicked = st.button("✨출력✨")

# ---

# 4. 버튼 클릭 및 이름 입력 로직 처리 (열 외부에서 처리)
if button_clicked:
    if user_name:
        st.balloons()
        st.success(f"Hello World, **{user_name}**님! 환영합니다. 🎉")
    else:
        st.warning("이름을 먼저 입력해주세요!")
