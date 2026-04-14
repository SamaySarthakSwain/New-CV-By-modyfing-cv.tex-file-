import requests
import sys

# Read preamble and cv.tex
with open("original_cv.tex", "r", encoding="utf-8") as f:
    lines = f.readlines()
    preamble = "".join(lines[:135]) # up to \begin{document} + \pagestyle{empty}

with open("cv.tex", "r", encoding="utf-8") as f:
    cv_body = f.read()

full_tex = preamble + "\n" + cv_body + "\n\\end{document}\n"

with open("cv_fixed.tex", "w", encoding="utf-8") as f:
    f.write(full_tex)

# Now compile using texlive.net
files = {
    'file': ('cv.tex', full_tex.encode('utf-8')),
}

print("Sending fixed tex to latex.ytmp.site...")
try:
    response = requests.post("https://latex.ytmp.site/compile", files=files)
    
    if response.status_code == 200:
        if response.headers.get('Content-Type') == 'application/pdf':
            with open("cv.pdf", "wb") as f:
                f.write(response.content)
            print("Successfully compiled and saved as cv.pdf")
        else:
            print("Error: Did not return a PDF.")
            with open("compile_error.log", "wb") as f:
                f.write(response.content)
            print("Output saved to compile_error.log")
    else:
        print(f"Request failed with status {response.status_code}")
        print(response.text)
except Exception as e:
    print(f"An error occurred: {e}")
