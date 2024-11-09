# 📧 **Smart Outreach Email Generator**

### 🚀 Overview
The **Smart Outreach Email Generator** is a powerful tool designed to simplify and personalize cold email outreach for consulting firms. By leveraging the **Groq API** with the advanced **LLaMA-3.1-70b** model, this app automatically analyzes job descriptions from provided URLs and crafts contextually relevant, professional emails. It acts as a virtual **Business Development Manager**, seamlessly integrating company-specific achievements and projects to enhance the email's impact and make it more appealing to potential clients.

### 🔑 Key Features
- **📝 Automated Job Description Extraction**: Scrapes job postings using **LangChain**, extracting key details to understand job requirements and context.
- **🔍 Personalized Email Content**: Leverages **ChromaDB** to pull relevant company projects and achievements, ensuring that the email highlights the most pertinent information related to the job description.
- **✍️ Tailored and Editable Emails**: Generates a fully customized email draft that clients can directly copy, with flexible options to personalize the content further by modifying company names, client names, or contact details.

### 🧠 Why It’s Useful
This app is a game-changer for consulting companies looking to efficiently create personalized outreach emails that resonate with potential clients. By automating the email crafting process, it saves time while ensuring that each email feels tailored, professional, and relevant to the specific job description. Whether for a single client or multiple outreach campaigns, this tool ensures maximum impact with minimal effort.

---

### 📸 **App Preview**

Get a quick look at the **Smart Outreach Email Generator** in action! Below are screenshots of the app's user interface and an example of the generated email response:

1. **App UI**  
   *A clean and intuitive interface where users can easily input details and generate personalized emails.*

   ![App UI Screenshot](images/Screenshot%202024-11-09%20210114.png)

2. **Generated Email Response**  
   *An example of a crafted cold email response that the app generates based on the input details.*

   ![Generated Email Screenshot](images/Screenshot%202024-11-09%20210156.png)


---

### 📝 **User Input Requirements**

To generate a tailored cold email, please provide the following details in the app form:

1. **name** - Your name
2. **post** - Your position in the company
3. **company_name** - The name of your company
4. **company_type** - The type of company (e.g., consulting, tech, finance)
5. **link** - The URL of the job posting
6. **company_email** - Your company email (if available)

--- 

### 🛠️ **How to Use**

To get started with the **Smart Outreach Email Generator**, follow these steps:

1. **Clone the Repository**  
   Start by cloning the project repository to your local machine:
   ```bash
   git clone https://github.com/ayushach007/cold_email_generator
   ```

2. **Install Requirements**  
   Use `pip` to install the necessary Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**  
   Create a `.env` file in the root directory of the project and add your **Groq API key**:
   ```
   GROQ_API_KEY=your-groq-api-key
   ```

4. **Run the App**  
   Start the Streamlit app by running the following command:
   ```bash
   streamlit run src/main.py
   ```

   The app should open in your default web browser, allowing you to generate cold emails by pasting job description URLs.

---

### 💬 **Contact**  
If you have any questions or need further assistance, feel free to reach out:  
- Email: [ayushach007@gmail.com](mailto:ayushach007@gmail.com)  
- GitHub: [@ayushach007](https://github.com/ayushach007)

---

### ✨ **Technologies Used**  
- **Groq API**  
- **LLaMA-3.1-70b**  
- **LangChain**  
- **ChromaDB**  
- **Streamlit**