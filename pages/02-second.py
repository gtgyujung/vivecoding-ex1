
import streamlit as st

# 앱의 제목 설정
st.title("🚀 Hello World 앱 (버튼 사용)")
st.write("이름을 입력하고 버튼을 눌러주세요.")

# 1. 사용자 이름 입력 받기
user_name = st.text_input("사용자의 이름을 입력해주세요:", placeholder="예: 미림 학생")

# 2. 버튼 생성 및 클릭 여부 확인
# st.button("버튼 텍스트")는 버튼이 클릭되었을 때 True를 반환합니다.
if st.button("✨ 환영 메시지 출력"):
    # 3. 버튼이 클릭되었을 때만 실행되는 로직
    if user_name:
        # 이름이 입력된 경우 메시지 출력
        st.balloons() # 축하 풍선 효과 (선택 사항)
        st.success(f"Hello World, **{user_name}**님! 환영합니다. 🎉")
    else:
        # 이름이 입력되지 않은 경우 경고 메시지 출력
        st.warning("이름을 먼저 입력해주세요!")

#
