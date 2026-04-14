import requests
import sys

tex_content = open("cv.tex", "rb").read()

import urllib.parse

print("Sending request to latexonline...")
try:
    text = open("cv.tex", 'r', encoding='utf-8').read()
    url = "https://latexonline.cc/compile?text=" + urllib.parse.quote(text) + "&command=pdflatex"
    response = requests.get(url)
    if response.status_code == 200:
        with open("cv.pdf", "wb") as f:
            f.write(response.content)
        print("Successfully compiled and saved as cv.pdf")
    else:
        print(f"Failed with status: {response.status_code}")
        print(response.text)
except Exception as e:
    print(f"Error: {e}")
