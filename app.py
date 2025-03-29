from collections import defaultdict, Counter
from heapq import nlargest
from string import punctuation
from typing import Optional
import spacy
from spacy.lang.en.stop_words import STOP_WORDS as en_sw
from spacy.lang.pt.stop_words import STOP_WORDS as pt_sw
import streamlit as st


# Configure page settings
st.set_page_config(
    page_title="Summarize Text with NLP",
    page_icon="🌍",
    layout="wide"
)

# Load spaCy model once at module level (not inside function)
nlp_eng = spacy.load('en_core_web_lg', disable=['ner'])
nlp_eng.add_pipe('sentencizer')

def en_summarize_text(
    original_text: str,
    n_sentences: int,
    spacy_model: Optional[spacy.Language] = None
) -> str:
    """
    Generates a text summary from english text, by extracting key sentences based on keyword frequency.

    Args:
        original_text: Input text to be summarized
        n_sentences: Number of sentences to include in the summary
        spacy_model: Optional pre-loaded spaCy model (default: English model)

    Returns:
        str: Generated summary concatenated from top sentences

    Raises:
        ValueError: If n_sentences is not a positive integer
    """
    # Input validation
    if n_sentences <= 0:
        raise ValueError("n_sentences must be a positive integer")

    # Use provided model or default
    model = spacy_model or nlp_eng
    
    # Text preprocessing
    cleaned_text = ' '.join(original_text.strip().split())
    doc = model(cleaned_text)
    
    # Configuration
    stopwords = set(en_sw)
    pos_tags = {'PROPN', 'ADJ', 'NOUN', 'VERB'}
    keywords = []
    sentence_scores = defaultdict(float)  # Use float for normalized scores

    # Keyword extraction with combined checks
    for token in doc:
        text_lower = token.text.lower()
        if (
            token.pos_ in pos_tags and
            text_lower not in stopwords and
            token.text not in punctuation
        ):
            keywords.append(text_lower)

    # Handle empty keyword case
    if not keywords:
        return ""
    
    # Normalize frequencies
    keyword_freq = Counter(keywords)
    max_freq = keyword_freq.most_common(1)[0][1]
    normalized_freq = {k: (v/max_freq) for k, v in keyword_freq.items()}

    # Score sentences
    for sent in doc.sents:
        score = sum(
            normalized_freq.get(token.text.lower(), 0)
            for token in sent
            if token.text.lower() in normalized_freq
        )
        sentence_scores[sent] = score

    # Preserve original order while selecting top sentences
    top_sentences = {
        sent: idx for idx, sent in enumerate(doc.sents)
        if sent in sentence_scores
    }
    ranked = sorted(
        sentence_scores.keys(),
        key=lambda x: (-sentence_scores[x], top_sentences[x])
    )[:n_sentences]

    # Join sentences in original order
    return ' '.join(
        sent.text for sent in sorted(ranked, key=lambda x: top_sentences[x])
    )

def main():
    st.header('Summarize texts with NLP :robot_face:')
    st.subheader("Choose a series of sentences and enter the text you want summarize!")

    st.write('')

    # Variable for user input
    if "user_input" not in st.session_state:
        st.session_state.user_input = ""

    # Button to clear text
    if st.button("Clear Text"):
        st.session_state.user_input = ""  # Clear text

    # Adding the user input (must be after clearing logic)
    user_input = st.text_area("Type or paste here:", st.session_state.user_input, height=300)
    st.session_state.user_input = user_input  # Update session state

    # Sidebar
    language = ["English"]

    with st.sidebar:
        st.image("reports/figures/summarize.jpg")
        menu = st.sidebar.selectbox("Select the Language", language)
        n_sentences = st.sidebar.slider('Number of sentences (default is 5).', value=5)

    # Button to summarize
    if st.button("Summarize"):
        if st.session_state.user_input.strip():  # Avoid running code if empty
            if menu == "English":
                st.header("This is the summary of your text.")
                summary = en_summarize_text(st.session_state.user_input, n_sentences)
                st.write(summary)
                st.download_button("Download your text", summary, file_name="summary.txt", mime="text/plain")
            elif menu == "Portuguese":
                st.header("Confira o resumo do seu texto abaixo:")
                summary = pt_summarize_text(st.session_state.user_input, n_sentences)
                st.write(summary)
                st.download_button("Download your text", summary, file_name="summary.txt", mime="text/plain")
        else:
            st.warning("Please enter some text before summarizing!")  # Warning if empty

if __name__ == '__main__':
    main()
    # Hide default Streamlit elements
    st.markdown("""<style> #MainMenu, footer, header {visibility: hidden;} </style>""", unsafe_allow_html=True)