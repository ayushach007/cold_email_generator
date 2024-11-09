import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
from utils import clean_text
from chains import Chains
from portfolio import Portfolio

def app(llm: str, portfolio: str, clean_text: str):
    url_input = st.text_input('Enter the URL of the job posting:', value="https://jobs.nike.com/job/R-43863?from=job%20search%20funnel")
    if st.button('Submit'):
        try:
            loader = WebBaseLoader([url_input])
            data = clean_text(loader.load().pop().page_content)
            portfolio.load_portfolio()
            jobs = llm.extract_job_description(data)
            for job in jobs:
                skills = job.get('skills', [])
                links = portfolio.query_link(skills)
                email = llm.write_email(job, links)
                st.code(email, language='markdown')
                
        except Exception as e:
            st.info(f":warning: Error: {e}")
            
if __name__ == '__main__':
    llm = Chains()
    portfolio = Portfolio()
    clean_text = clean_text
    app(llm, portfolio, clean_text)
            