import streamlit as st
import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        title = soup.title.string if soup.title else "No title found"
        paragraphs = [p.get_text() for p in soup.find_all('p')]

        return title, paragraphs
    
    except Exception as e:
        return None, [f"Error: {str(e)}"]
    
def main():
    st.title("Web Scraping App")
    st.markdown("""" Enter an URL to scrape its content. This app wil  fetch the web page's title and extract text from all paragraphs.""")

    url = st.text_input("Enter the URL:")

    if st.button("Scrape") and url:
        st.markdown('### Results:')

        title, paragraphs = scrape_website(url)

        if title:
            st.markdown(f"**Title:** {title}")
        else:
            st.markdown("**Title:** No title found")

        st.markdown("**Content:**")
        for para in paragraphs:
            st.write(para)

if __name__ == "__main__":
    main()