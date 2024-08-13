import streamlit as st

# 제목 설정
st.title("🎶 MBTI 기반 수학 공부 음악 추천 🎧")

# MBTI 입력받기
mbti = st.text_input("당신의 MBTI를 입력하세요! 🔤", "").upper()

# MBTI별 음악 추천
music_recommendations = {
    "INTJ": {
        "music": "클래식 음악 (바흐, 모차르트 등)",
        "description": "🧠 **INTJ**는 집중력이 중요한 유형입니다. 클래식 음악은 깊은 집중을 돕고, 수학 문제 해결에 도움을 줄 수 있어요."
    },
    "INFP": {
        "music": "로파이 힙합",
        "description": "🌸 **INFP**는 감성적이고 차분한 로파이 힙합이 수학 공부 중 편안한 분위기를 만들어 줄 거예요."
    },
    "ENTP": {
        "music": "인디 록",
        "description": "💡 **ENTP**는 활기차고 창의적인 인디 록이 수학 공부를 더욱 흥미롭게 만들 거예요!"
    },
    "ESFJ": {
        "music": "팝 음악",
        "description": "🤗 **ESFJ**는 경쾌한 팝 음악이 학습을 즐겁게 만들어주고, 에너지를 유지하는 데 도움을 줄 거예요."
    },
    # 다른 MBTI 유형도 추가할 수 있습니다.
}

# 결과 출력
if mbti in music_recommendations:
    st.subheader(f"📊 {mbti}에게 추천하는 음악")
    st.write(music_recommendations[mbti]["description"])
    st.write(f"🎵 추천 음악: {music_recommendations[mbti]['music']}")
else:
    st.write("⚠️ 유효한 MBTI 유형을 입력해주세요! (예: INTJ, INFP, ENTP, ESFJ)")
