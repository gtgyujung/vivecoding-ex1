import streamlit as st
import pandas as pd
import numpy as np

# 1. 시맨틱 UI 느낌을 위한 사용자 정의 CSS (이전과 동일)
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
