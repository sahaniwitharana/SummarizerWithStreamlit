import streamlit as st
import streamlit.components.v1 as components

from sumy.summarizers.kl import KLSummarizer
summarizer_kl = KLSummarizer()

#Upload files
from PyPDF2 import PdfReader
uploaded_file = st.file_uploader("Choose a File to Upload", type=["pdf", "docx", "txt"])
if uploaded_file is not None:
    reader = PdfReader(uploaded_file)
    
    test = ""
    for page in reader.pages:
        test += page.extract_text() + "\n"
        test+=page.extract_text() + "\n"
        
    #progress bar
    from time import sleep
    progress = st.progress(0)
    for i in range(100):
        progress.progress(i)
        sleep(0.1)
        
        
    from sumy.nlp.tokenizers import Tokenizer
    from sumy.parsers.plaintext import PlaintextParser

    parser = PlaintextParser.from_string(test, Tokenizer('english'))
    # Summarize using sumy KL Divergence
    summary = summarizer_kl(parser.document, 2)
    kl_summary = ""
    for sentences in summary:
        kl_summary += str(sentences)
    st.write(kl_summary)

    components.html("""<hr style="height:5px;border:none;color:#BEFBFF;background-color:#BEFBFF;" /> """)

