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
        
    def write_email(self, job, name, post, company_name, company_type, links, company_email):
        prompt_email = PromptTemplate.from_template(
            """
            ### JOB DESCRIPTION
            {job}
            
            ### INSTRUCTIONS
            You are {name}, a {post} at {company_name}, an {company_type}.
            
            Your task is to write a professional and compelling cold email to potential clients based on the job description provided. Follow these steps:
            
            1. **Introduction**: Start the email with a personalized greeting, addressing the potential client by name (use "Dear Hiring Manager"). Give a short introduction of yourself and {company_name}, including your role and the company's expertise.
            
            2. **Highlighting Company Expertise**: Explain how the capabilities of {company_name} can help the client. Make sure to mention the strengths and services offered by {company_name} and how they align with the client's needs and provided job description. This could include relevant projects, industry knowledge, or specific solutions provided by the company.
            
            3. **Portfolio Links**: Provide a selection of links to {company_name}'s portfolio that showcases successful projects or capabilities. Mention these links and explain why they are relevant to the client. You can include the following portfolio links: {links}. Structure the output in a well-formatted and structures for better visibility and readability. Use bullet points or numbers for shocasing the projects relevent to the job description.
            
            5. **Call to Action**: Conclude the email with a strong, clear call to action. Invite the client to reach out to you for further discussion or to learn more about how {company_name} can assist them. Offer a clear next step for them to take (e.g., scheduling a call, replying to the email).
            
            6 professional sign-off . **Sign-Off**: End the email with a(e.g., "Best regards," "Sincerely") followed by your name and contact information.
            
            ### Last Line should be:
            ```
            Best regards, \n
            {name}\n
            {company_name}\n
            {company_email}
            ```

            ### EMAIL Output(No Preamble):
            """
        )
        
        chain_write_email = prompt_email | self.llm
        email = chain_write_email.invoke(input={"job": str(job), "name": name, "post": post, "company_name": company_name, "company_type": company_type, "links": links, "company_email": company_email})
        return email.content