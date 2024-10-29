# import boto3
# import json
# import base64
# import os

# prompt= "provide me one 4k hd image of person who is swimming in the river"

# prompt_template=[{"text":prompt, "weight":1}]

# bedrock= boto3.client(service_name= "bedrock-runtime")

# payload={
#     "text_prompts": prompt_template,
#     "cfg_scale": 10,
#     "seed": 0,
#     "steps": 50,
#     "width": 512,
#     "height": 512
# }

# body= json.dumps(payload)
# model_id="amazon.titan-image-generator-v1"

# response= bedrock.invoke_model(
#     body= body,
#     modelId= model_id,
#     accept= "application/json",
#     contentType= "application/json"

# )

# response_body= json.loads(response.get("body").read())
# print(response_body)


# artifacts= response_body.get("artifacts")[0]
# image_encoded= artifacts.get("base64").encode('utf-8')
# image_bytes= base64.b64decode(image_encoded)

# output_dir= "output"
# os.mkdirs(output_dir,exist_ok=True)
# file_name= f"{output_dir}/generated-img.png"
# with open(file_name,"wb") as f:
#     f.write(image_bytes)

#Modified code according to the Titan model

import boto3
import json, base64, io
import os
from random import randint
from PIL import Image

# Initialize the Bedrock client
bedrock_runtime_client = boto3.client("bedrock-runtime")

# Function to generate an image using the Titan Image Generator model
def titan_image(
    prompt: str,
    num_image: int = 1,  # Number of images to generate (1 to 5)
    cfg: float = 10.0,   # Classifier-free guidance scale
    seed: int = None,    # Seed for reproducibility
    modelId: str = "amazon.titan-image-generator-v1"
) -> list:
    # Set a seed if not provided
    seed = seed if seed is not None else randint(0, 214783647)
    
    # Prepare the request body
    body = json.dumps(
        {
            "taskType": "TEXT_IMAGE",  # Task type
            "textToImageParams": {
                "text": prompt  # Required prompt for image generation
            },
            "imageGenerationConfig": {
                "numberOfImages": num_image,  # Number of images (1 to 5)
                "quality": "premium",         # Image quality: standard/premium
                "height": 1024,               # Image height (valid values: 512, 768, 1024)
                "width": 1024,                # Image width (valid values: 512, 768, 1024)
                "cfgScale": cfg,              # Classifier-free guidance scale (1.0 to 10.0)
                "seed": seed                  # Seed for reproducibility
            }
        }
    )

    # Call the Titan Image Generator model
    response = bedrock_runtime_client.invoke_model(
        body=body,
        modelId=modelId,
        accept="application/json",
        contentType="application/json"
    )

    # Process the response
    response_body = json.loads(response.get("body").read())
    
    # Decode and return images from the response
    images = [
        Image.open(io.BytesIO(base64.b64decode(base64_image)))
        for base64_image in response_body.get("images")
    ]
    return images

# Example usage
if __name__ == "__main__":
    try:
        # Set the image prompt
        prompt = "provide me one 4k hd image of person who is swimming in the river"

        # Generate image(s) using the function
        generated_images = titan_image(prompt, num_image=1, cfg=10.0)

        # Save the images
        output_dir = "output"
        os.makedirs(output_dir, exist_ok=True)
        
        for i, img in enumerate(generated_images):
            file_name = f"{output_dir}/generated_image_{i+1}.png"
            img.save(file_name)
            print(f"Image saved to {file_name}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

