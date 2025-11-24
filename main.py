import streamlit as st

# 1. 배경 이미지 파일명 설정 (사용하시는 파일명으로 변경해 주세요!)
IMAGE_FILE = "cat_background.jpg" 

# 2. CSS 스타일 정의 (백그라운드 이미지 설정)
css_style = f"""
<style>
/* Streamlit 앱의 주 컨테이너를 타겟팅합니다. */
[data-testid="stAppViewContainer"] {{
    background-image: url("{IMAGE_FILE}"); 
    background-size: cover; /* 이미지가 배경 전체를 덮도록 설정 */
    background-position: center; /* 이미지를 중앙에 배치 */
    background-repeat: no-repeat; /* 이미지 반복 방지 */
    background-attachment: fixed; /* 스크롤해도 배경 고정 */
}}

/* 만약 사이드바에도 배경을 적용하고 싶다면 아래 주석을 해제하세요. */
/*
[data-testid="stSidebar"] {{
    background-image: url("{IMAGE_FILE}");
    background-size: cover;
    background-attachment: fixed;
}}
*/
</style>
"""

# 3. CSS 코드 삽입 (HTML 허용)
st.markdown(css_style, unsafe_allow_html=True)

# 4. 앱의 내용 (배경 확인용)
st.title("🐈 고양이 배경화면 웹앱")
st.header("배경에 귀여운 고양이 이미지가 보입니다!")
st.write("텍스트가 이미지 위에 잘 보이도록 하려면 텍스트 배경색을 조정할 수 있습니다.")
