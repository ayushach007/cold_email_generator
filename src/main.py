import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
from utils import clean_text
from chains import Chains
from portfolio import Portfolio

def app(llm: str, portfolio: str, clean_text: str):
    """
    Function to run the Streamlit app
    
    Args:
        llm: Chains object 
        portfolio: Portfolio object
        clean_text: function to clean text
    """
    with st.container(border=True):
        # center the title using markdown
        st.markdown("<h1 style='text-align: center;'>📧 Smart Outreach Email Generator</h1>", unsafe_allow_html=True)
        
        url, name = st.columns(2)
        post, company_name = st.columns(2)
        company_type, company_email = st.columns(2)
        
        with url:
            url_input = st.text_input('**Enter the URL of the job posting**:', value="https://jobs.nike.com/job/R-43863?from=job%20search%20funnel")
        
        with name:
            name = st.text_input('**Enter your name**:', value="XYZ")
            
        with post:
            post = st.text_input('**Enter your position**:', value="XYZ")
            
        with company_name:
            company_name = st.text_input('**Enter the name of your company**:', value="XYZ")
        
        with company_type:
            company_type = st.text_input('**Enter the type of your company**:', value="XYZ")
            
        with company_email:
            company_email = st.text_input('**Enter the email of your company**:', value="xyz@gmail.com")
        
    if st.button('Submit'):
        try:
            loader = WebBaseLoader([url_input])
            data = clean_text(loader.load().pop().page_content)
            portfolio.load_portfolio()
            jobs = llm.extract_job_description(data)
            for job in jobs:
                skills = job.get('skills', [])
                links = portfolio.query_link(skills)
                email = llm.write_email(job, name, post, company_name, company_type, links, company_email)
                st.code(email, language='markdown')                 
                
        except Exception as e:
            st.info(f":warning: Error: {e}")
                
if __name__ == '__main__':
    llm = Chains()
    portfolio = Portfolio()
    clean_text = clean_text
    app(llm, portfolio, clean_text)
            