# import json
# import os 
# import sys
# import boto3

# print("imported successfully...")

# prompt="you are a smart assistant so please let me know what is machine learning in smartest way?"

# bedrock= boto3.client(service_name="bedrock-runtime")

# payload={
#     "prompt": "[INST]"+prompt+"[/INST]",
#     "max_gen_len": 512,
#     "temperature": 0.3,
#     "top_p": 0.9

# }

# body= json.dumps(payload)
# model_id="meta.llama3-70b-instruct-v1:0"

# response= bedrock.invoke_model(
#     body= body,
#     modelId= model_id,
#     accept="application/json",
#     contentType= "application/json"
# )

# response_body= json.loads(response.get("body").read())
# response_text= response_body["generation"]
# print(response_text)


# ChatGPT's code:

# import json
# import os
# import sys
# import boto3

# print("imported successfully...")

# prompt = "you are a smart assistant so please let me know what is machine learning in the smartest way?"

# # Create the boto3 client for Bedrock runtime
# bedrock = boto3.client(service_name="bedrock-runtime")

# # Payload for the request
# payload = {
#     "prompt": "[INST]" + prompt + "[/INST]",
#     "max_gen_len": 512,
#     "temperature": 0.3,
#     "top_p": 0.9
# }

# # Convert payload to JSON string
# body = json.dumps(payload)
# model_id = "meta.llama3-70b-instruct-v1:0"

# # Try making the request
# try:
#     response = bedrock.invoke_model(
#         body=body,
#         modelId=model_id,
#         accept="application/json",
#         contentType="application/json"
#     )
#     print("Request to Bedrock successful!")
    
#     # Debug: Print the raw response to inspect
#     print("Raw response:", response)

#     # Parsing the response body
#     response_body = json.loads(response["body"])  # Extract 'body' directly as a JSON object
#     print("Parsed response body:", response_body)

#     # Extract the text generation output
#     response_text = response_body.get("generation", "No generation found")
#     print("Generated text:", response_text)

# except Exception as e:
#     print(f"Error occurred: {e}")

# ChatGPT's second updated code:

import json
import os
import sys
import boto3

print("imported successfully...")

prompt = "Explain machine learning in a clear and concise manner."

# Create the boto3 client for Bedrock runtime
bedrock = boto3.client(service_name="bedrock-runtime")

# Payload for the request
payload = {
    "prompt": "[INST]" + prompt + "[/INST]",
    "max_gen_len": 256,
    "temperature": 0.7,
    "top_p": 0.95
}

# Convert payload to JSON string
body = json.dumps(payload)
model_id = "meta.llama3-70b-instruct-v1:0"

# Try making the request
try:
    response = bedrock.invoke_model(
        body=body,
        modelId=model_id,
        accept="application/json",
        contentType="application/json"
    )
    print("Request to Bedrock successful!")
    
    # Debug: Print the raw response to inspect
    print("Raw response:", response)

    # Read the StreamingBody content
    response_stream = response['body']
    response_content = response_stream.read().decode('utf-8')  # Read and decode the response
    
    # Parse the JSON response
    response_body = json.loads(response_content)  # Convert to JSON object
    print("Parsed response body:", response_body)

    # Extract the text generation output
    response_text = response_body.get("generation", "No generation found")
    print("Generated text:", response_text)

except Exception as e:
    print(f"Error occurred: {e}")

