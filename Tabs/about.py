"""This modules contains data about about page"""

# Import necessary modules
import streamlit as st
from PIL import Image


def app():
    """This function creates the about page"""
    st.balloons()
    st.title('Contact Us')
    st.markdown('''### Name: Riya Pandey''')
    st.markdown('''Passionate Engineer and Rational Thinker.  Web Developer''')
    st.image('./images/icon.jpg')
    st.markdown('''### Linkedin: [Riya](https://www.linkedin.com/in/riya-pandey-6994a8201/)''')
    st.markdown('''### GitHub: [Mainak](https://github.com/ria24122002)''')
    