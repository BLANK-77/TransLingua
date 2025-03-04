from deep_translator import GoogleTranslator
import streamlit as st
from gtts import gTTS
import os

# Set page config
st.set_page_config(page_title="🌍 Language Translator", layout="centered")

# Title
st.markdown("<h1 style='text-align: center;'>🌍 Language Translator</h1>", unsafe_allow_html=True)
st.write("---")

# Supported languages
languages = {
    "Afrikaans": "af", "Albanian": "sq", "Amharic": "am", "Arabic": "ar",
    "Azerbaijani": "az", "Basque": "eu", "Belarusian": "be", "Bengali": "bn", "Bosnian": "bs",
    "Bulgarian": "bg", "Catalan": "ca", "Cebuano": "ceb", "Chichewa": "ny", "Chinese (Simplified)": "zh-CN",
    "Chinese (Traditional)": "zh-TW", "Corsican": "co", "Croatian": "hr", "Czech": "cs", "Danish": "da",
    "Dutch": "nl", "English": "en", "Esperanto": "eo", "Estonian": "et", "Filipino": "tl",
    "Finnish": "fi", "French": "fr", "Frisian": "fy", "Galician": "gl", "Georgian": "ka",
    "German": "de", "Greek": "el", "Gujarati": "gu", "Haitian Creole": "ht", "Hausa": "ha",
    "Hawaiian": "haw", "Hebrew": "iw", "Hindi": "hi", "Hmong": "hmn", "Hungarian": "hu",
    "Icelandic": "is", "Igbo": "ig", "Indonesian": "id", "Irish": "ga", "Italian": "it",
    "Japanese": "ja", "Javanese": "jv", "Kannada": "kn", "Kazakh": "kk", "Khmer": "km",
    "Korean": "ko", "Kurdish (Kurmanji)": "ku", "Kyrgyz": "ky", "Lao": "lo", "Latin": "la",
    "Latvian": "lv", "Lithuanian": "lt", "Luxembourgish": "lb", "Macedonian": "mk", "Malagasy": "mg",
    "Malay": "ms", "Malayalam": "ml", "Maltese": "mt", "Maori": "mi", "Marathi": "mr",
    "Mongolian": "mn", "Myanmar (Burmese)": "my", "Nepali": "ne", "Norwegian": "no", "Pashto": "ps",
    "Persian": "fa", "Polish": "pl", "Portuguese": "pt", "Punjabi": "pa", "Romanian": "ro",
    "Russian": "ru", "Samoan": "sm", "Scots Gaelic": "gd", "Serbian": "sr", "Sesotho": "st",
    "Shona": "sn", "Sindhi": "sd", "Sinhala": "si", "Slovak": "sk", "Slovenian": "sl",
    "Somali": "so", "Spanish": "es", "Sundanese": "su", "Swahili": "sw", "Swedish": "sv",
    "Tajik": "tg", "Tamil": "ta", "Telugu": "te", "Thai": "th", "Turkish": "tr",
    "Ukrainian": "uk", "Urdu": "ur", "Uzbek": "uz", "Vietnamese": "vi", "Welsh": "cy",
}

# Initialize session state
if "translated_text" not in st.session_state:
    st.session_state.translated_text = ""

# User Input
text = st.text_area("✍️ Enter text to translate:", height=150)
target_language = st.selectbox("🌐 Select Target Language", list(languages.keys()))

# Translate button
if st.button("🚀 Translate Now"):
    if text:
        translator = GoogleTranslator(source="auto", target=languages[target_language])
        st.session_state.translated_text = translator.translate(text)

        # Show translated text
        st.markdown(f"""
            <div style='padding: 10px; border-radius: 10px; background-color: #dff0d8; font-size: 18px; text-align: center;'>
                <b>✅ Translated Text:</b> {st.session_state.translated_text}
            </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("⚠️ Please enter text to translate.")

# Speak the translated text
if st.session_state.translated_text:
    if st.button("🔊 Read Aloud"):
        tts = gTTS(st.session_state.translated_text, lang=languages[target_language])
        audio_file = "translated_audio.mp3"
        tts.save(audio_file)

        # Play the audio in Streamlit
        st.audio(audio_file, format="audio/mp3")

        # Provide download link
        with open(audio_file, "rb") as f:
            audio_bytes = f.read()
        st.download_button(label="📥 Download Audio", data=audio_bytes, file_name="translated_audio.mp3", mime="audio/mp3")

# Footer
st.write("---")
st.markdown("<p style='text-align: center; color: gray;'>Created by DevMind's</p>", unsafe_allow_html=True)

