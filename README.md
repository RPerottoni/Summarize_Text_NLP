# Text Summarization with NLP

This project provides a simple web-based interface for summarizing text using Natural Language Processing (NLP) techniques. The application supports both **English** and **Portuguese** text and generates a summary by selecting key sentences based on keyword frequency.

Built using **spaCy** for text processing and **Streamlit** for the web interface, this tool extracts the most relevant sentences from input text to create a concise summary.

---

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Code Explanation](#code-explanation)
4. [Contributing](#contributing)
5. [License](#license)

---

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/RPerottoni/Summarize_Text_NLP.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Summarize_Text_NLP
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Download the required spaCy models for English and Portuguese:

    ```bash
    python -m spacy download en_core_web_lg
    python -m spacy download pt_core_news_lg
    ```

5. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

The app will open in your browser, where you can enter text and generate summaries.

---

## Usage

1. **Select Language**: Choose either **English** or **Portuguese** from the sidebar.
2. **Input Text**: Type or paste the text you want to summarize in the text box.
3. **Adjust Sentence Count**: Use the slider in the sidebar to select the number of sentences for the summary.
4. **Generate Summary**: Click the "Summarize" button to get the summary of the input text. The summary will be displayed below the input area.

---

## Code Explanation

### Key Functions

#### `en_summarize_text`

This function summarizes English text by extracting key sentences based on keyword frequency.

**Arguments**:
- `original_text` (str): The text to be summarized.
- `n_sentences` (int): The number of sentences to include in the summary.
- `spacy_model` (Optional[spacy.Language]): An optional pre-loaded spaCy model (default: English model).

**Returns**: A string containing the summary of the text.

**Raises**: `ValueError` if `n_sentences` is not a positive integer.

#### `pt_summarize_text`

This function summarizes Portuguese text in a similar way as `en_summarize_text` but using a Portuguese spaCy model.

**Arguments**:
- `original_text` (str): The text to be summarized.
- `n_sentences` (int): The number of sentences to include in the summary.
- `spacy_model` (Optional[spacy.Language]): An optional pre-loaded spaCy model (default: Portuguese model).

**Returns**: A string containing the summary of the text.

**Raises**: `ValueError` if `n_sentences` is not a positive integer.

#### `main`

This is the main entry point of the Streamlit app. It:
- Displays the UI for user input.
- Accepts text input from the user.
- Provides options for language selection and number of sentences in the summary.
- Displays the generated summary after processing the input text.

---

## Contributing

Contributions are welcome! If you'd like to contribute to the project, feel free to submit a pull request with improvements or new features.

1. Fork the repository
2. Create a new branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -am 'Add feature'`)
4. Push to the branch (`git push origin feature-name`)
5. Create a new pull request

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgements

- **spaCy**: Used for text processing and NLP tasks.
- **Streamlit**: Used for building the web application.

---

For more details or updates, visit the project on [Github](https://github.com/RPerottoni/Summarize_Text_NLP).
