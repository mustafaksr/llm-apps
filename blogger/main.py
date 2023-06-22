import os
import vertexai
from vertexai.preview.language_models import TextGenerationModel
from IPython.display import display
from google.cloud import aiplatform
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from IPython.display import HTML
import argparse
from dotenv import load_dotenv
from utils import *

# Load variables
load_dotenv()
# Set your credentials and blog ID
credentials_file = 'credentialsOauth2.json'  # OAuth 2.0 Client ID Credentials
API_KEY = os.environ["API_KEY"] #Blogger API apikey, Only requires when to get blog posts 
BLOG_ID = os.environ["BLOG_ID"]
PROJECT_ID = os.environ["PROJECT_ID"]

def run():
    response = predict_large_language_model_sample(PROJECT_ID, "text-bison@001", temprature , max_output_tokens, top_p, top_k, prompt, "us-central1")
    response, kws = post_process(response)
    
 
    
    # Define the required scopes
    scopes = ['https://www.googleapis.com/auth/blogger']
    
    # Perform OAuth 2.0 authorization flow
    flow = InstalledAppFlow.from_client_secrets_file(credentials_file, scopes)
    credentials = flow.run_local_server(port=9090)
    
    # Build the Blogger API client
    service = build('blogger', 'v3', credentials=credentials)
    
    # Create a new blog post json body
    post = {
        'kind': 'blogger#post',
        'blog': {'id': BLOG_ID},
        'title': response.split("<h1>")[1].split("</h1>")[0],
        'content': response,
        'labels': kws,
        'status': 'DRAFT' 
    }
    
    # Insert the blog post
    request = service.posts().insert(blogId=BLOG_ID, body=post)
    response_post = request.execute()
    HTML(response)
    # Get the newly created post's ID
    post_id = response_post['id']
    print('New blog post ID:', post_id)

if __name__=="__main__":
    # (--project_id="google project_id",  --top_p=0.1, --max_output_tokens=1024, --top_p=0.8, top_k=40, prompt="Can you create blog about Machine learning.", "us-central1")
    
    parser = argparse.ArgumentParser(description='blogger prompt arg parser')
    parser.add_argument('--prompt', help='User prompt related to blog topic.', required=True, type=str)
    parser.add_argument('--max_output_tokens', help='llm max_output_tokens', required=True, type=int)
    parser.add_argument('--temprature', help='llm temperature', required=True, type=float)
    parser.add_argument('--top_p', help='llm top_p', required=True, type=float)
    parser.add_argument('--top_k', help='llm top_k', required=True, type=int)  
    
    args = parser.parse_args()
    user_prompt = str(args.prompt)
    temprature = float(args.temprature)
    max_output_tokens = int(args.max_output_tokens)
    top_p = float(args.top_p)
    top_k = int(args.top_k)
    
    prompt = f"""user prompt : {user_prompt}, you should create blog text as html ,\
    your rules and context are ```context:{context}``` """ 
    
    run()
# python main.py --temprature=0.1 --max_output_tokens=1024 --top_p=0.8 --top_k=40 --prompt="Can you create blog about Machine learning."