# vis10nary
Idea brainstorming drawing to marketable MVP in minutes. The tool to create other market-ready tools.

![Project Banner](https://d112y698adiu2z.cloudfront.net/photos/production/software_photos/002/874/296/datas/gallery.jpg)

## Steps to run
1. Required softwares
   * Python 3.10
   * Docker
2. Save the captured image file to ```files``` folder
3. Run these commands
   * ```pip install -r requirements.txt```
   * ```.env``` file is commited intentionally for ease of testing, this file may be used or also can be set using ```set GOOGLE_API_KEY=<YOUR_GEMINI_API_KEY>```
   * ```python generate.py```
4. The generated code files will be generated inside the ```code``` folder
5. ```docker-compose up``` may be execeuted inside the _files_ folder to run the project
