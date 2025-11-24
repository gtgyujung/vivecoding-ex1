import streamlit as st

# 1. 앱의 제목 설정
st.title("👋 Hello World 앱")

# 2. 부가 설명 (선택 사항)
st.write("이름을 입력하면 환영 메시지를 출력합니다.")

# 3. 사용자 이름 입력 받기
user_name = st.text_input("사용자의 이름을 입력해주세요:", placeholder="예: 홍길동")

# 4. 이름이 입력되었을 때 결과 출력
if user_name:
    # f-string을 사용하여 입력받은 이름과 함께 메시지 출력
    st.success(f"Hello World, {user_name}님! 반갑습니다. 🎉")
