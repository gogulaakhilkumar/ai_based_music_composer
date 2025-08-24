import streamlit as st
from mood_analyzer import MoodAnalyzer
from music_parameters import MusicParameterProcessor
import json
import re

@st.cache_resource
def load_models():
    analyzer = MoodAnalyzer()
    processor = MusicParameterProcessor()
    return analyzer, processor

def normalize(text):
    return re.sub(r'[^\w\s]', '', text).strip().lower()

def main():
    st.set_page_config(page_title="🎵 Whispers of the Wires", layout="wide")

    st.sidebar.title("🎛️ Mood Input")

    preset_moods = {
        "Chill": "I'm feeling calm and introspective",
        "Melancholy": "I'm heartbroken and reflective",
        "Hype": "I'm super pumped and ready to dance",
        "Mysterious": "It feels like I'm floating through space",
        "Romantic": "I'm in love and everything feels magical",
        "Joyful": "I'm feeling upbeat and ready to celebrate",
        "Peaceful": "I'm meditative and want something serene",
        "Sad": "I'm feeling low and emotionally heavy",
        "Angry": "I'm frustrated and need something intense",
        "Confident": "I'm feeling bold and unstoppable",
        "Thoughtful": "I'm in a contemplative, philosophical mood",
        "Sleepy": "I'm tired and want something soft and slow",
        "Cinematic": "I want something dramatic and movie-like",
        "Nostalgic": "I'm reminiscing about old memories",
        "Focused": "I need music to help me concentrate and study",
        "Energetic": "I need a fast-paced track for working out",
        "Rainy": "It's a rainy day and I feel reflective",
        "Sunny": "I'm feeling bright and optimistic",
        "Spiritual": "I'm in a spiritual or sacred mood",
        "Anxious": "I'm overwhelmed and need something grounding",
        "Curious": "I'm exploring and want something experimental",
        "Natural": "I want something earthy and organic",
        "Playful": "I'm in a fun, quirky mood like gaming"
    }

    selected_preset = st.sidebar.selectbox("Choose a mood preset (or type your own):", options=["Type my own"] + list(preset_moods.keys()))

    if selected_preset != "Type my own":
        user_input = preset_moods[selected_preset]
        st.sidebar.text_area("Selected mood description:", value=user_input, disabled=True)
    else:
        user_input = st.sidebar.text_area("Describe your mood or musical vibe:", placeholder="e.g., I'm feeling nostalgic and peaceful...")

    st.sidebar.markdown("---")
    st.sidebar.markdown("Built by **Akhil** | Y22CO015")

    st.markdown("<h1 style='color:#6C63FF;'>🎵 Whispers of the Wires</h1>", unsafe_allow_html=True)
    st.subheader("AI-Powered Music Composition")

    with st.spinner("Loading AI models..."):
        analyzer, processor = load_models()

    if st.sidebar.button("🎼 Generate Music Parameters"):
        if not user_input.strip():
            st.warning("Please enter a mood description to proceed.")
        else:
            with st.spinner("Analyzing mood and composing music..."):
                base_params = analyzer.analyze_mood(user_input)
                enhanced_params = processor.enhance_parameters(base_params)

            st.success("✅ Music parameters generated!")

            st.markdown("### 🎼 Composition Summary")
            st.markdown(f"""
- **Mood Category:** `{enhanced_params['mood_category'].capitalize()}`
- **Energy Level:** `{enhanced_params['energy_level']}/10`
- **Tempo:** `{enhanced_params['tempo']} BPM`
- **Key:** `{enhanced_params['suggested_key']} ({enhanced_params['key']})`
- **Scale Type:** `{enhanced_params['scale_type']}`
- **Chord Progression:** `{ ' - '.join(enhanced_params['chord_progression']) }`
- **Rhythmic Pattern:** `{enhanced_params['rhythmic_pattern']}`
- **Instruments:** 🎹 `{', '.join(enhanced_params['instruments'])}`
- **Dynamics:** `{enhanced_params['dynamics']}`
- **Texture:** `{enhanced_params['texture']}`
- **Genre Style:** 🎷 `{enhanced_params['genre_style']}`
- **Sentiment Confidence:** `{enhanced_params['sentiment_confidence']}`
            """)

            st.markdown("### 🎧 Suggested Telugu Songs")

            mood_to_songs = {
                "chill": ["https://youtu.be/6sDSZwH2EpM", "https://youtu.be/nIL5fPWaMoI"],
                "melancholy": ["https://youtu.be/vuek5YvKtHU", "https://youtu.be/RZYakKBrEIw"],
                "hype": ["https://youtu.be/OXHTlMPbX7o", "https://youtu.be/IxDvpoCmAaY"],
                "mysterious": ["https://youtu.be/toTRkovRzvo", "https://youtu.be/cY3REsLgfz8"],
                "romantic": ["https://youtu.be/0n7AWxYCj9I", "https://youtu.be/BCwsSk_KKrE", "https://youtu.be/4wpCzY1LfdM"],
                "joyful": ["https://youtu.be/NFbmkNCV4K4", "https://youtu.be/eyeJtpZ0oC4"],
                "peaceful": ["https://youtu.be/dc-fOyYjtk8", "https://youtu.be/dOKQeqGNJwY"],
                "sad": ["https://youtu.be/GX-CVUrQ9tM", "https://youtu.be/PVxc5mIHVuQ"],
                "nostalgic": ["https://youtu.be/4OQtT1XnQuc", "https://youtu.be/q76ue-byDzY"],
                "focused": ["https://youtu.be/5jca-sWgemI", "https://youtu.be/il_1aAQnV_M"],
                "energetic": ["https://youtu.be/w0Sutzthn_s", "https://youtu.be/pHl_MjgPiZo", "https://youtu.be/VVBziwNCHq8"],
                "rainy": ["https://youtu.be/05HYHpDKR2k", "https://youtu.be/QL1ho2RzUkA", "https://youtu.be/k9DMXBFHEH4"],
                "sunny": ["https://youtu.be/dIzbJ-brpkA", "https://youtu.be/C-Cf0ZWdyEE"],
                "spiritual": ["https://youtu.be/HwBRWbQP_CU", "https://youtu.be/Hn9VoVh0vvM", "https://youtu.be/g7rTZNIXhSs"],
                "anxious": ["https://youtu.be/VgdAcENXy84"],
                "curious": ["https://youtu.be/llqWa8gukho", "https://youtu.be/HUj9R44Zk-k"],
                "natural": ["https://youtu.be/2a34XyiZO14", "https://youtu.be/lFAiFov5pP8"],
                "playful": ["https://youtu.be/hYFzyK9ExuM", "https://youtu.be/Z86KFuKrckc"]
            }

            mood_aliases = {
                "peacefull": "peaceful",
                "low mood": "sad",
                "heartbroken": "melancholy",
                "high energy": "hype",
                "calm": "chill",
                "relaxed": "peaceful",
                "nostalgia": "nostalgic",
                "curious mood": "curious",
                "happy": "joyful",
                "excited": "energetic",
                "romance": "romantic",
                "introspective": "thoughtful"
            }

            valid_moods = list(mood_to_songs.keys())
            raw_mood = normalize(enhanced_params.get("mood_category", ""))
            mapped_mood = mood_aliases.get(raw_mood, raw_mood)
            mood_key = mapped_mood if mapped_mood in valid_moods else None

            suggested_songs = mood_to_songs.get(mood_key, [])

            if suggested_songs:
                for i, song in enumerate(suggested_songs):
                    with st.expander(f"🎧 Preview {i+1}"):
                        st.video(song)
            else:
                st.info(f"No specific Telugu songs found for mood: `{raw_mood}`. Try a different vibe!")

            st.download_button(
                label="📥 Download Composition",
                data=json.dumps(enhanced_params, indent=2),
                file_name="composition.json",
                mime="application/json"
            )

if __name__ == "__main__":
    main()
