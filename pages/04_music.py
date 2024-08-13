import streamlit as st
from PIL import Image

# 제목 설정
st.title("🎶 MBTI 기반 수학 공부 음악 추천 🎧")

# MBTI 입력받기
mbti = st.text_input("당신의 MBTI를 입력하세요! 🔤", "").upper()

# MBTI별 음악 추천과 이미지 설정
music_recommendations = {
    "INTJ": {
        "music": "🎼 클래식 음악 (바흐, 모차르트 등)",
        "image": "classical_music.jpg",
        "description": "🧠 **INTJ**는 집중력이 중요하기 때문에 클래식 음악이 공부에 적합해요. 🎻"
    },
    "INFP": {
        "music": "🎹 로파이 힙합",
        "image": "lofi_music.jpg",
        "description": "🌸 **INFP**는 감성적인 로파이 힙합이 수학 공부에 도움이 돼요. 🌙"
    },
    "ENTP": {
        "music": "🎸 인디 록",
        "image": "indie_rock.jpg",
        "description": "💡 **ENTP**는 활기찬 인디 록 음악이 창의력을 자극해줄 거예요! 🎤"
    },
    "ESFJ": {
        "music": "🎧 팝 음악",
        "image": "pop_music.jpg",
        "description": "🤗 **ESFJ**는 밝고 경쾌한 팝 음악이 수학 공부를 더욱 즐겁게 만들어 줄 거예요! 🎵"
    },
    # 다른 MBTI 유형도 추가할 수 있습니다.
}

# 결과 출력
if mbti in music_recommendations:
    st.subheader(f"📊 {mbti}에게 추천하는 음악")
    st.write(music_recommendations[mbti]["description"])
    
    st.write(f"🎵 추천 음악: {music_recommendations[mbti]['music']}")
    
    # 음악과 관련된 이미지 표시
    image = Image.open(music_recommendations[mbti]["image"])
    st.image(image, caption=f"{music_recommendations[mbti]['music']} 🎶", use_column_width=True)
    
else:
    st.write("⚠️ 유효한 MBTI 유형을 입력해주세요! (예: INTJ, INFP, ENTP, ESFJ)")

