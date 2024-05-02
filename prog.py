import google.generativeai as genai
import os
import pathlib
from dotenv import load_dotenv
from PIL import Image
import pillow_avif
from pillow_heif import register_heif_opener
from pathlib import Path
from shutil import rmtree

register_heif_opener()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

"""Image to text"""
# model = genai.GenerativeModel("gemini-1.0-pro-vision-latest")

# img = Image.open("files/test1.avif")
# prompt = """Describe this image and also suggest what modifications can be made to make this image to be used in corporate events"""
# response = model.generate_content([prompt, img])
# print(response.text)


"""PDF to text"""
# from PyPDF2 import PdfReader

# model = genai.GenerativeModel(
#     "gemini-1.5-pro-latest",
#     generation_config={"response_mime_type": "application/json"},
# )
# reader = PdfReader("files/Introduction_to_Python_Programming_-_WEB.pdf")
# content = " ".join(
#     [reader.pages[page].extract_text() for page in range(len(reader.pages))]
# )
# prompt = input("Question:")
# response = model.generate_content([prompt, content])
# print(response.text)


"""Image comparison"""
import json

modelVis = genai.GenerativeModel(
    "gemini-1.0-pro-vision-latest",
)
modelText = genai.GenerativeModel(
    "gemini-1.5-pro-latest",
    generation_config={"response_mime_type": "application/json"},
)

img1 = Image.open("files/IMG_0107.HEIC")
# img2 = Image.open("files/IMG_0103.HEIC")
# img3 = Image.open("files/IMG_0104.HEIC")

prompt = """You are a professional computer programmer who is expert in React JS for frontend, Flask for backend REST API and Postgresql for database and Docker to combine all the systems and return separate code files for each of these languages. You are creating the project from scratch so add all the initialization codes.
You can make Frontend directory with package.json and other necessary project structure for running an error-free React application.
You can make Backend directory containing proper files for Flask application.
You can make docker-compose.yml file in root folder.
You are given hand drawn images of a software application. Describe the changes in these images. 
Create and return only the properly formatted code files of a fully functional project of the latest image and all getting connected through a docker-compose.yml file for web, api and database hosting while separating each file by '----'."""

responseVis = modelVis.generate_content([prompt, img1])
responseText = modelText.generate_content(
    [
        "Separate each file and return in JSON format {'<system_module>.<file_ext>':<file_content>,}",
        responseVis.text,
    ]
)
# print(responseText.text)

if len(responseText.candidates)==0:
    print("none")
else:
    content = json.loads(responseText.text)
    print(content)

    for path in Path("code/").glob("**/*"):
        if path.is_file():
            path.unlink()
        elif path.is_dir():
            rmtree(path)

    for i in content:
        os.makedirs(os.path.dirname("code/" + i), exist_ok=True)
        f = open("code/" + i, "w")
        f.write(content[i])
        f.close()
