import re

def clean_text(text):
    # Remove html tags
    text = re.sub(r'<[^>]*>', '', text)
    
    # Remove urls
    text = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', text)
    
    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text)
    
    # remove special characters
    text = re.sub(r'[^A-Za-z0-9 ]+', '', text)
    
    # remove leading and trailing spaces
    text = text.strip()
    
    # replace multiple spaces with single space
    text = re.sub(r'\s+', ' ', text)
    
    # remove extra white spaces
    text = " ".join(text.split())
    
    return text