# Summarize Text with NLP

## Overview
This project is a web application that summarizes text using Natural Language Processing (NLP). It supports English and Portuguese and allows users to extract key sentences from a given text based on keyword frequency. The application is built using `spaCy` for NLP processing and `Streamlit` for the user interface.

## Features
- Supports text summarization in **English** and **Portuguese**.
- Uses `spaCy` for sentence parsing and keyword extraction.
- Provides an interactive web interface built with `Streamlit`.
- Allows users to select the number of sentences to include in the summary.
- Supports **downloading** the generated summary as a `.txt` file.

## Technologies Used
- **Python** (Main programming language)
- **spaCy** (Natural Language Processing)
- **Streamlit** (Web framework for interactive UI)
- **Counter & defaultdict** (For keyword frequency analysis)

## Installation
To run this project locally, follow these steps:

1. Clone the repository:
   ```sh
   git clone https://github.com/RPerottoni/Summarize_Text_NLP.git
   ```
2. Navigate to the project directory:
   ```sh
   cd Summarize_Text_NLP
   ```
3. Create a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate  # On Windows
   ```
4. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
5. Run the application:
   ```sh
   streamlit run app.py
   ```

## Usage
1. Open the app in your browser.
2. Enter the text you want to summarize.
3. Choose the language (**English** or **Portuguese**).
4. Select the number of sentences to include in the summary.
5. Click the **Summarize** button to generate the summary.
6. Download the summarized text as a `.txt` file if needed.

## Results
Check out the deployed application at:
🔗 **[Live Demo](https://rp-summarize-text-nlp.streamlit.app)**

## Future Improvements
- **Integration with News APIs**: Automatically summarize news articles from external sources.
- **AI-based Abstractive Summarization**: Implement deep learning models for better summarization.
- **Multi-language Support**: Extend support for additional languages.
- **Keyword Highlighting**: Show important keywords in the output summary.

## License
This project is open-source and available under the [MIT License](LICENSE).

