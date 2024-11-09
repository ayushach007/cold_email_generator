import os
from langchain_groq import ChatGroq
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException

class Chains:
    def __init__(self):
        self.llm = ChatGroq(api_key=os.environ['GROQ_API_KEY'],model='llama-3.1-70b-versatile',streaming=True,max_retries=2)
        
    def extract_job_description(self, cleaned_text):
        prompt_extract = PromptTemplate.from_template(
            """
            ### SCRAPED TEXT FROM WEBSITE
            {page_data}
            
            ### INSTRUCTIONS
            The text above is a job description from a company's job posting. 
            Please extract the relevant information and return it in JSON format with the following fields:
            - role: The job title or position.
            - experience: The required experience for the job.
            - skills: The skills required for the job.
            - description: A brief description of the job.

            Ensure the JSON is valid and contains no additional text.

            ### VALID JSON (NO PREAMBLE):
            """
        )

        chain_extract_data = prompt_extract | self.llm
        result = chain_extract_data.invoke(input={"page_data": cleaned_text})
        try:
            json_parser = JsonOutputParser()
            descriptions = json_parser.parse(result.content)
            return descriptions if isinstance(descriptions, list) else [descriptions]
        except OutputParserException:
            raise OutputParserException("Context too big. Unable to parse jobs.")
        
    def write_email(self, job, links):
        prompt_email = PromptTemplate.from_template(
            """
            ### JOB DESCRIPTION
            {job}
            
            ### INSTRUCTIONS
            You are Sujal, a Business Development Manager at Data Vanguard, an AI, Data Science, and Data Engineering Consulting company. 
            Your task is to write a compelling cold email to potential clients regarding the job description mentioned above. 
            Highlight the capabilities of Data Vanguard and explain how these capabilities can benefit the client's business.
            Include the most relevant links from the portfolio to showcase Data Vanguard's expertise and successful projects {link_list}.
            Ensure the email is professional, concise, and persuasive.
            
            ### EMAIL (NO PREAMBLE):
            """
        )
        
        chain_write_email = prompt_email | self.llm
        email = chain_write_email.invoke(input={"job": str(job), "link_list": links})
        return email.content