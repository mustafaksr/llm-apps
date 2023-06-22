import os
import vertexai
from vertexai.preview.language_models import TextGenerationModel
import time
# Vertex AI
from google.cloud import aiplatform

EXAMPLE = """<h1>Title related with query</h1>
<p>paragraph</p>
<p>paragraph</p>
"<h2>SubTitles</h2>
<p>paragraph</p>
<p>paragraph</p>
You can support with images, charts, tables etc.
<img src="url">
<p>paragraph</p>
<ul>
<li>bullet</li>
<li>bullet</li>
</ul>
<p>paragraph</p>
<h2>SubTitles</h2>
<p>paragraph</p>
<p>paragraph</p>
<ul>
<li>bullet</li>
<li>bullet</li>
</ul>
"<h2>SubTitles</h2>
<p>paragraph</p>
<p>paragraph</p>
<h2>Conclusion</h2>
<p>paragraph</p>
<p>paragraph</p>
<h2>Keywords</h2>
<ul>
<li>bullet</li>
<li>bullet</li>
</ul>
<h2>References</h2>
<ul>
<li>bullet</li>
<li>bullet</li>
</ul>
"""
context = f"""
You are bloggerbot for google blogger, you design and \ 
create blogs as HTML code for content like AI,Machine Learning, Deep Learning. \
You Must write all blogs within 10000 chars, \
show images as html image tag, \
and return text in html only body format content. \
You can't use markdown code, only you can use HTML code\
You can use images, charts, tables etc. if it is helping explain. \
You should use EXAMPLE as Template. \
You should use img tag for supportive images from webs, and add image reference for cite from webs \
You shouldn't use any text or HTML tag before blog body like "Sure, here is a blog text as HTML... or <HTML>" \
You should only return html body. \
You should add conlucion and keywords end of text. \
You can find and add supportive images as <img> tag. \
You should add  at least one image , least one diagram, least one table  to explain better. \
Bullets should be with <ul> <li> tags. \
==================================================================================================
(Don't copy examples , just use as template) \
example image tag = <img src="https://developers.google.com/static/machine-learning/gan/images/gan_diagram.svg" alt="DCGAN architecture">
EXAMPLE = {EXAMPLE}
"""

def post_process(response):
    kws = []
    try:
        try:
            if response.split("<body>")[1].split("</body>")[0]:
                response = response.split("<body>")[1].split("</body>")[0]
        except:
            response = "<h1>"+response.split("<h1>")[1]
    except:pass
    
    try:
        try:
            kws=[kw.split("</li>")[0] for kw in response.split("References")[0].split("Keywords")[1].split("<li>")[1:]]
        except:pass
        try: 
            kws = response.split("Keywords")[1].split("<p>")[1].split("</p>")[0].split(",")
        except:pass
    except:
        kws = []
    
    return response , kws

def predict_large_language_model_sample(
    project_id: str,
    model_name: str,
    temperature: float,
    max_decode_steps: int,
    top_p: float,
    top_k: int,
    content: str,
    location: str = "us-central1",
    tuned_model_name: str = "",
    ) :
    """Predict using a Large Language Model.

    Args:
        project_id (str): The ID of the project.
        model_name (str): The name of the large language model.
        temperature (float): Temperature controls the degree of randomness in token selection. Lower temperatures
                             are good for prompts that expect a true or correct response, while higher temperatures
                              can lead to more diverse or unexpected results. 
                              A temperature of 0 is deterministic: the highest probability token is always selected.
                               For most use cases, try starting with a temperature of .2.
        max_decode_steps (int): The maximum number of tokens in the generated output.
        top_p (float): Changes how tokens are selected for output. Tokens are selected from most
                        probable to least until the sum of their probabilities equals the top-p value.
        top_k (int): Changes how tokens are selected for output. A top-k of 1 means the most probable
                      token is selected, while a top-k of 3 means the next token is selected from the
                      three most probable tokens.
        content (str): The input prompt or text to generate output from.
        location (str, optional): The location of the model. Defaults to "us-central1".
        tuned_model_name (str, optional): The name of the tuned model. Defaults to "".

    Returns:
        str: The generated text output from the large language model.

    Raises:
        (Any relevant exceptions that may occur during the execution)

    Examples:
        # Example usage
        response = predict_large_language_model_sample(
            project_id="my-project",
            model_name="my-model",
            temperature=0.2,
            max_decode_steps=256,
            top_p=0.8,
            top_k=40,
            content="Generate a paragraph about dogs.",
            location="us-central1",
            tuned_model_name="tuned-model"
        )
        print(response)  # Output: Generated text from the large language model
    """
    vertexai.init(project=project_id, location=location)
    model = TextGenerationModel.from_pretrained(model_name)
    if tuned_model_name:
      model = model.get_tuned_model(tuned_model_name)
    response = model.predict(
        content,
        temperature=temperature,
        max_output_tokens=max_decode_steps,
        top_k=top_k,
        top_p=top_p,)
    # print(f"Response from Model: {response.text}")
    if response.text=='':
      return f"There is an ERROR, it can be related to non-english result prompt.{response.text}"
    else:
      return response.text