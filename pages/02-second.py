import streamlit as st
import datetime

# (생략: set_semantic_style, get_meal_info 함수 및 CSS 정의는 이전과 동일합니다.)
# ...

# 3. Streamlit 앱 메인 함수
def main():
    
    # (생략: set_semantic_style() 호출)
    # ...
    
    st.title("🍜 미림마이스터고 급식 메뉴 조회")
    
    # 📌 핵심 수정/강조 부분: st.date_input을 사용하여 사용자에게 날짜를 직접 선택하게 합니다.
    # 초기값은 오늘 날짜(2025-11-24)로 설정합니다.
    today = datetime.date(2025, 11, 24) 
    
    selected_date = st.date_input(
        "**🗓️ 조회할 날짜를 직접 선택하세요:**", # 사용자에게 날짜 선택을 요청하는 레이블
        value=today,                           # 기본값 설정
        min_value=datetime.date(2025, 1, 1),   # 선택 가능한 최소 날짜
        max_value=datetime.date(2026, 12, 31)  # 선택 가능한 최대 날짜
    )

    st.markdown("---")
    st.markdown("<div class='stContainer'>", unsafe_allow_html=True) 

    # 메뉴 정보 가져오기 (실제 검색 대신 안내 기능을 수행)
    meal_data = get_meal_info(selected_date)
    
    st.header(f"📅 {meal_data['date_info']} 메뉴 검색 결과")

    # (생략: 주말 경고, 검색 안내 및 가상 메뉴 출력 로직은 이전과 동일합니다.)
    # ...

    st.markdown("</div>", unsafe_allow_html=True) 

# 앱 실행
# if __name__ == "__main__":
#     main()
