# Blogger LLM App

This is a Python application that utilizes a large language model (LLM) to generate blog posts and publish them on Google Blogger. The application generates text using the LLM and creates a new blog post with the generated content.


## Getting Started

### 1.Prerequisites

Before running the application, make sure you have the following:

* #### Python installed on your system
* #### Required Python packages installed (vertexai, google-cloud, google-auth-oauthlib, dotenv)
* #### OAuth 2.0 Client ID credentials file (credentialsOauth2.json)
  * OAuth 2.0 Client ID credentials file (credentialsOauth2.json):
The OAuth 2.0 Client ID credentials file is a JSON file that contains the credentials required for OAuth 2.0 authorization. It includes the client ID, client secret, and other information necessary for the authentication process. In the context of the Blogger LLM App, the credentials file (credentialsOauth2.json) is used to authorize the application to access the required Google APIs, such as the Blogger API. To obtain this credentials file, you can go to the Google Cloud Console, navigate to the API & Services section, create credentials for OAuth 2.0, and download the JSON file.
  * OAuth 2.0 Consent screen:
The OAuth 2.0 Consent screen is an interface that allows you to configure the permissions and information displayed to users when they are prompted to authorize an application's access to their Google account data. It provides details about the application, such as its name, logo, and privacy policy, and requests specific permissions required for accessing certain APIs or user data. In the context of the Blogger LLM App, setting up the OAuth 2.0 Consent screen involves defining the necessary information and scopes required for the application to access the Blogger API. You can configure the Consent screen settings in the Google Cloud Console under the API & Services section.
  * Please note that the OAuth 2.0 Client ID credentials file (credentialsOauth2.json) is essential for the application to authenticate and authorize requests to the Blogger API, while the OAuth 2.0 Consent screen allows you to customize the authorization experience for users and specify the required permissions for accessing user data.

* #### Blogger API API key:
  * The Blogger API API key is a unique identifier that grants access to the Blogger API. It is used to authenticate and authorize requests made to the API. To obtain an API key, you can go to the Google Cloud Console, navigate to the API & Services section, and create credentials for the Blogger API. This key is necessary for the application to interact with the Blogger API and perform operations such as creating and updating blog posts.
* Google Cloud project ID:
  * The Google Cloud project ID is a user-defined, globally unique identifier for a project created on the Google Cloud Platform (GCP). It represents a container for your GCP resources and services. Each project has a unique project ID that is used to identify and manage the resources within that project. In the context of the Blogger LLM App, the project ID is required to authenticate and access Google Cloud services, such as Vertex AI and Google Blogger.
* #### Blogger blog ID:
  * The Blogger blog ID is a unique identifier for a blog hosted on the Blogger platform. When you create a blog on Blogger, it is assigned a specific blog ID. This ID is used to uniquely identify the blog when making API requests to the Blogger API. In the context of the Blogger LLM App, the blog ID is required to specify the target blog where the generated content will be published as a new blog post.

### 2.Installation

 Clone the repository:

```bash
git clone https://github.com/mustafaksr/llm-apps.git

```

### 3.Navigate to the project directory:
```bash
cd ~/llm-apps/blogger
```

### 4.Create env:
```bash
virtualenv blogger
```

```bash
source blogger/bin/activate
```


### 5.Install the required dependencies:
```bash
pip install --upgrade setuptools
pip install -r requirements.txt
```

### 6.Configuration:
1. Create an OAuth 2.0 Client ID credentials file named credentialsOauth2.json and place it in the project directory. This file is used for authorization.
2. Set the following environment variables within .env file:
   * API_KEY: Your Blogger API API key.
   * BLOG_ID: The ID of the Blogger blog where you want to publish the generated posts.
   * PROJECT_ID: Your Google Cloud project ID.


### 7.Usage
To run the application, use the following command:
```bash
python main.py --temprature=<temperature> --max_output_tokens=<max_output_tokens> --top_p=<top_p> --top_k=<top_k> --prompt="<prompt>"
```
Replace <temperature>, <max_output_tokens>, <top_p>, <top_k>, and <prompt> with the desired values for generating the blog post.

* temperature: Controls the randomness of token selection. Recommended starting value is 0.1.
* max_output_tokens: The maximum number of tokens in the generated output.
* top_p: Controls how tokens are selected for output. Recommended starting value is 0.8.
* top_k: Controls how tokens are selected for output. Recommended starting value is 40.
* prompt: The user prompt related to the blog topic.

For example:

```bash
python main.py --temprature=0.1 --max_output_tokens=1024 --top_p=0.8 --top_k=40 --prompt="Can you create a blog about Machine learning."

```
The application will generate the blog post content using the LLM and publish it on the specified Blogger blog as a draft.

## Additional Notes
* The utils.py file contains utility functions used by the main application script.
* The EXAMPLE variable in utils.py provides a template for the blog post content. You can modify it according to your needs.
* The post_process function in utils.py is used for post-processing the LLM response and extracting keywords from the generated content.