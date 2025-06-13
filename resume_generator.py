import yaml
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential
from azure.core.exceptions import HttpResponseError

def load_yaml_config(file_path='config.yaml'):
    """Load configuration from YAML file."""
    try:
        with open(file_path, 'r') as file:
            config = yaml.safe_load(file)
            return config
    except FileNotFoundError:
        return {"error": f"Configuration file {file_path} not found."}
    except yaml.YAMLError as e:
        return {"error": f"Error parsing YAML file: {e}"}

def generate_resume(resume_input, job_description):
    """Generate a resume using the Grok API."""
    config = load_yaml_config()
    if "error" in config:
        return config["error"]
    
    token = config.get('grok', {}).get('api_key')
    if not token:
        return "Error: GitHub token not found in config.yaml."

    endpoint = "https://models.github.ai/inference"
    model = "xai/grok-3"

    try:
        client = ChatCompletionsClient(
            endpoint=endpoint,
            credential=AzureKeyCredential(token)
        )

        response = client.complete(
            messages=[
                SystemMessage(content="You are a professional resume writer. Generate a polished resume based on the provided experience and tailored to the job description."),
                UserMessage(content=f"Experience: {resume_input}\nJob Description: {job_description}")
            ],
            model=model,
            temperature=0.7,
            max_tokens=1000,
            top_p=1.0
        )

        return response.choices[0].message.content
    except HttpResponseError as e:
        return f"Error generating resume: {e.status} {e.reason} - {e.message}"
    except Exception as e:
        return f"Error generating resume: {str(e)}"