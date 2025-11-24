import streamlit as st
import pandas as pd
import numpy as np

# 1. 시맨틱 UI 느낌을 위한 사용자 정의 CSS
def set_semantic_style():
    """시맨틱 UI 스타일링을 모방한 CSS 주입"""
    st.markdown("""
        <style>
            /* 전체 페이지 배경 및 기본 글꼴 설정 */
            .main {
                background-color: #f7f7f7; /* 약간 회색 배경 */
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            }

            /* 제목 스타일링 */
            .stApp header {
                background-color: #1b1c1d; /* Semantic UI Header Color */
                color: white;
                padding: 1rem;
                margin-bottom: 2rem;
            }

            /* 컨테이너 (카드) 스타일링 */
            .stContainer {
                background-color: white;
                border-radius: 0.28571429rem; /* Semantic UI Border Radius */
                box-shadow: 0 1px 2px 0 rgba(34,36,38,.15); /* Semantic UI Box Shadow */
                border: 1px solid rgba(34,36,38,.15);
                padding: 1.5rem;
                margin-bottom: 1.5rem;
            }

            /* 선택 정보 강조 (Metric/Statistic 느낌) */
            div[data-testid="stMetricValue"] {
                font-size: 2.5rem;
                font-weight: 700;
                color: #2185d0; /* Semantic UI Primary Blue */
            }

            /* 멘트 및 설명 섹션 */
            h3 {
                color: #007bb6; /* 조금 더 강조된 색상 */
            }
            blockquote {
                border-left: 5px solid #2185d0;
                background: #f9f9f9;
                padding: 0.5em 10px;
                margin: 0.5em 0;
            }
        </style>
        """, unsafe_allow_html=True)

# 2. MBTI 유형별 간단한 설명 데이터 (이전과 동일)
MBTI_DESCRIPTIONS = {
    'ISTJ': "세상의 소금형: 현실적이고 사실적이며 논리적입니다. 책임감이 강합니다.",
    'ISFJ': "용감한 수호자: 조용하고 헌신적이며 책임감이 강합니다. 사려 깊습니다.",
    'INFJ': "선의의 옹호자: 통찰력이 뛰어나고 이상적인 세상을 꿈꿉니다. 인류애가 있습니다.",
    'INTJ': "전략가: 독립적이고 분석적입니다. 모든 일에 계획을 세웁니다.",
    'ISTP': "만능 재주꾼: 조용하고 과묵하며, 논리적이고 분석적입니다. 기계를 잘 다룹니다.",
    'ISFP': "호기심 많은 예술가: 따뜻하고 유연하며 호기심이 많습니다. 예술적 감각이 뛰어납니다.",
    'INFP': "열정적인 중재자: 창의적이고 사려 깊습니다. 자신의 가치관에 충실합니다.",
    'INTP': "논리적인 사색가: 지적인 호기심이 많고 비판적 사고 능력이 뛰어납니다.",
    'ESTP': "모험을 즐기는 사업가: 활동적이고 문제 해결 능력이 뛰어납니다. 즉흥적입니다.",
    'ESFP': "자유로운 영혼의 연예인: 넘치는 에너지를 가진 자유로운 영혼입니다. 사교적입니다.",
    'ENFP': "재기 발랄한 활동가: 상상력이 풍부하고 개방적입니다. 열정적입니다.",
    'ENTP': "변론가: 똑똑하고 도전적이며 지적인 도전을 즐깁니다. 논쟁을 즐깁니다.",
    'ESTJ': "사업가: 체계적이고 리더십이 있습니다. 현실적이며 조직적입니다.",
    'ESFJ': "사교적인 외교관: 친절하고 사교적입니다. 사람들을 돕는 것을 좋아합니다.",
    'ENFJ': "정의로운 사회운동가: 카리스마 있고 이타적입니다. 사람들의 성장에 기여합니다.",
    'ENTJ': "대담한 통솔자: 대담하고 통솔력이 있습니다. 목표 달성을 위해 계획을 세웁니다."
}

# 3. 멘트 생성 함수 (이전과 동일)
def generate_compliment(mbti, percentage):
    """
    MBTI 유형과 통계 비율을 기반으로 격려 및 특징 멘트를 생성하는 함수
    """
    trait = MBTI_DESCRIPTIONS.get(mbti, "").split(':')[0].strip()
    
    if percentage >= 10:
        stat_msg = "가장 흔한 유형 중 하나"
        stat_adj = "많은 사람들과 공감대를 형성하기 쉽습니다"
    elif percentage >= 5:
        stat_msg = "비교적 흔한 유형"
        stat_adj = "주변에서 쉽게 찾아볼 수 있어 적응력이 뛰어납니다"
    else:
        stat_msg = "희귀한 편에 속하는 특별한 유형"
        stat_adj = "당신만의 고유한 관점과 강점을 가졌습니다"

    compliment = (
        f"**✨ {mbti} 유형이신 당신**은 **{trait}** 분이시군요! "
        f"전 세계 평균 인구의 약 **{percentage:.1f}%**를 차지하는 **{stat_msg}**입니다. "
        f"이러한 비율은 당신이 {stat_adj}는 것을 의미합니다. "
        f"당신의 고유한 강점을 마음껏 펼쳐나가시길 응원합니다! 🚀"
    )
    return compliment

# 4. Streamlit 앱 메인 함수
def main():
    st.set_page_config(page_title="MBTI 성격 유형 분석기", layout="centered")
    
    # 시맨틱 UI 스타일 적용
    set_semantic_style()
    
    st.title("🧩 MBTI 성격 유형 분석기")
    
    # 데이터 로드 및 통계 계산 (이전과 동일)
    if 'mbti_df' not in st.session_state:
        try:
            file_path = "countriesMBTI_16types.csv"
            df = pd.read_csv(file_path)
            df.set_index(df.columns[0], inplace=True)
            df_percent = df * 100
            st.session_state['mbti_stats'] = df_percent.mean().sort_values(ascending=False)
            st.session_state['mbti_df'] = df_percent
            st.session_state['mbti_types'] = sorted(st.session_state['mbti_stats'].index.tolist())
        except Exception as e:
            st.error(f"🚨 첨부된 파일('countriesMBTI_16types.csv')을 로드하거나 처리하는 데 오류가 발생했습니다: {e}")
            return
            
    mbti_stats = st.session_state['mbti_stats']
    mbti_types = st.session_state['mbti_types']

    select_options = ['--- MBTI를 선택하세요 ---'] + mbti_types

    # MBTI 선택 박스를 상단에 배치
    selected_mbti = st.selectbox(
        "**👇 당신의 MBTI를 선택해주세요:**",
        select_options
    )

    st.markdown("<div class='stContainer'>", unsafe_allow_html=True) # 컨테이너 시작

    # 5. 선택 결과에 따른 화면 출력 (Grid Layout 적용)
    if selected_mbti == '--- MBTI를 선택하세요 ---':
        # 초기 접속 또는 미선택 시 메시지
        st.info("👆 위에 있는 드롭다운 메뉴에서 **당신의 MBTI**를 선택해주세요. 선택하시면 해당하는 MBTI에 대한 상세 정보가 여기에 나타납니다!")
        st.image("https://i.imgur.com/8Qj9n9t.png", caption="당신의 성격 유형을 찾아보세요!", use_column_width=True)
        
    elif selected_mbti in mbti_stats.index:
        
        percentage = mbti_stats.loc[selected_mbti]
        description = MBTI_DESCRIPTIONS.get(selected_mbti, "설명 정보를 찾을 수 없습니다.")
        
        st.markdown(f"## 🌟 {selected_mbti} 유형 분석 결과")
        
        # 5-1. 통계 정보 (Metrics Card)
        st.markdown("### 📊 핵심 통계 정보")
        
        # 3-Column Grid Layout (Semantic Grid 느낌)
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric(label="선택 유형 비율", value=f"{percentage:.1f}%")
            
        with col2:
            max_mbti = mbti_stats.idxmax()
            st.metric(label=f"가장 흔한 유형 ({max_mbti})", value=f"{mbti_stats.max():.1f}%")
            
        with col3:
            st.metric(label="희귀한 유형 (INFJ)", value=f"{mbti_stats.loc['INFJ']:.1f}%")
        
        st.markdown("---")
        
        # 5-2. MBTI 설명 출력 (Description Card)
        st.markdown("### 📝 유형 설명")
        st.write(f"**{selected_mbti}** 유형의 특징은 다음과 같습니다:")
        st.markdown(f"<blockquote>{description}</blockquote>", unsafe_allow_html=True)
        
        st.markdown("---")
        
        # 5-3. 맞춤 멘트 및 시각화
        
        # 2-Column Layout
        col_ment, col_chart = st.columns([1, 1])
        
        with col_ment:
            st.markdown("### 🎉 맞춤 멘트")
            compliment_message = generate_compliment(selected_mbti, percentage)
            st.markdown(compliment_message)
            
        with col_chart:
            st.markdown("### 📈 전체 비율 분포")
            plot_data = mbti_stats.rename("비율 (%)").to_frame()
            st.bar_chart(plot_data, use_container_width=True, height=200)
            
        st.caption("위 그래프는 첨부 파일에 포함된 국가들의 평균 MBTI 비율을 나타냅니다.")


    st.markdown("</div>", unsafe_allow_html=True) # 컨테이너 끝


# 앱 실행
if __name__ == "__main__":
    main()
