import streamlit as st
import datetime

# 1. 시맨틱 UI 느낌을 위한 사용자 정의 CSS (이전 MBTI 앱과 동일)
def set_semantic_style():
    """시맨틱 UI 스타일링을 모방한 CSS 주입"""
    st.markdown("""
        <style>
            /* 전체 페이지 배경 및 기본 글꼴 설정 */
            .main {
                background-color: #f7f7f7; 
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            }
            /* 헤더 스타일링 */
            .stApp header {
                background-color: #1b1c1d; 
                color: white;
                padding: 1rem;
                margin-bottom: 2rem;
            }
            /* 컨테이너 (카드) 스타일링 */
            .stContainer {
                background-color: white;
                border-radius: 0.28571429rem; 
                box-shadow: 0 1px 2px 0 rgba(34,36,38,.15); 
                border: 1px solid rgba(34,36,38,.15);
                padding: 1.5rem;
                margin-bottom: 1.5rem;
            }
            /* 멘트 및 안내 섹션 */
            h3 {
                color: #007bb6; 
            }
            .stInfo { /* st.info 박스 스타일 */
                border-left: 5px solid #2185d0;
                background-color: #f0f8ff;
                padding: 10px;
                border-radius: 4px;
            }
            .meal-box {
                border: 1px solid #ddd;
                padding: 15px;
                margin-bottom: 10px;
                border-radius: 5px;
                background-color: #fff;
            }
            .meal-box h4 {
                color: #007bb6;
                margin-top: 0;
            }
        </style>
        """, unsafe_allow_html=True)

# 2. 메뉴 데이터 조회 함수 (실제 검색 불가로 안내 기능만 구현)
def get_meal_info(date: datetime.date):
    """
    미림마이스터고 급식 메뉴 정보를 검색하는 안내 함수.
    실제 메뉴를 가져오지 않고, 사용자에게 안내 메시지와 검색 쿼리를 제공합니다.
    """
    date_str = date.strftime("%Y-%m-%d")
    day_name = date.strftime("%A")
    korean_day = {"Monday": "월요일", "Tuesday": "화요일", "Wednesday": "수요일", 
                  "Thursday": "목요일", "Friday": "금요일", "Saturday": "토요일", "Sunday": "일요일"}
    
    # 검색 쿼리 예시
    search_query = f"미림마이스터고 급식 {date.month}/{date.day}({korean_day[day_name][:1]})"
    
    # 템플릿 데이터 (실제 데이터 아님)
    template_data = {
        "date_info": f"{date_str} ({korean_day[day_name]})",
        "search_query": search_query
    }
    
    return template_data

# 3. Streamlit 앱 메인 함수
def main():
    
    # 시맨틱 UI 스타일 적용
    set_semantic_style()
    
    st.title("🍜 미림마이스터고 급식 메뉴 조회")
    
    # 날짜 입력 위젯
    # 기본값은 오늘 날짜
    today = datetime.date(2025, 11, 24) # 요청 날짜인 2025-11-24로 고정
    selected_date = st.date_input(
        "**🗓️ 조회할 날짜를 선택하세요:**",
        value=today,
        min_value=datetime.date(2025, 1, 1),
        max_value=datetime.date(2026, 12, 31)
    )

    st.markdown("---")
    st.markdown("<div class='stContainer'>", unsafe_allow_html=True) 

    # 메뉴 정보 가져오기
    meal_data = get_meal_info(selected_date)
    
    st.header(f"📅 {meal_data['date_info']} 메뉴 검색 결과")

    if selected_date.weekday() >= 5: # 토요일(5) 또는 일요일(6)
        st.warning(f"⚠️ {meal_data['date_info']}는 주말이므로 급식이 제공되지 않을 수 있습니다.")
    
    
    # 4. 검색 안내 및 결과 출력 영역
    st.markdown("### 🔍 메뉴 조회 안내")
    
    st.info(f"""
        **미림마이스터고등학교의 급식 메뉴는 실시간 API가 없어 자동으로 표시할 수 없습니다.**

        하지만 아래 검색어를 복사하여 **Google** 또는 **학교 홈페이지**에서 검색하시면 **가장 정확한 메뉴 정보**를 찾으실 수 있습니다.
    """)
    
    # 검색어 표시
    st.code(meal_data['search_query'], language='text')

    st.markdown("---")
    
    # 5. 가상의 급식 메뉴 박스 (UI 예시)
    st.markdown("### 🍱 급식 메뉴 (UI 예시)")
    
    col_break, col_lunch, col_dinner = st.columns(3)

    with col_break:
        st.markdown("<div class='meal-box'>", unsafe_allow_html=True)
        st.markdown("#### 조식 (Breakfast)")
        st.markdown("* 흰밥/죽")
        st.markdown("* 씨리얼 & 우유")
        st.markdown("* 햄치즈 샌드위치")
        st.markdown("* 배추김치")
        st.markdown("</div>", unsafe_allow_html=True)

    with col_lunch:
        st.markdown("<div class='meal-box'>", unsafe_allow_html=True)
        st.markdown("#### 중식 (Lunch)")
        st.markdown("* **차조밥**")
        st.markdown("* 시원한 콩나물국")
        st.markdown("* **닭갈비 덮밥**")
        st.markdown("* 오징어초무침")
        st.markdown("* 포기김치, 오렌지주스")
        st.markdown("</div>", unsafe_allow_html=True)

    with col_dinner:
        st.markdown("<div class='meal-box'>", unsafe_allow_html=True)
        st.markdown("#### 석식 (Dinner)")
        st.markdown("* 잡곡밥")
        st.markdown("* 순두부찌개")
        st.markdown("* **돈육 고추장 불고기**")
        st.markdown("* 계란찜")
        st.markdown("* 깍두기, 옥수수 콘샐러드")
        st.markdown("</div>", unsafe_allow_html=True)

    st.caption("위에 표시된 메뉴는 실제 메뉴가 아닌, UI 구성을 위한 예시 데이터입니다.")

    st.markdown("</div>", unsafe_allow_html=True) # 컨테이너 끝

# 앱 실행
if __name__ == "__main__":
    main()
