import requests
import time

try:
    with open("cv_fixed.tex", "r", encoding="utf-8") as f:
        latex_code = f.read()

    print("Sending to rtex...")
    res = requests.post("https://rtex.probablyaweb.site/api/v2", json={"code": latex_code})
    
    if res.status_code == 200:
        data = res.json()
        if data.get("status") == "success":
            pdf_id = data.get("id")
            print(f"Success! ID: {pdf_id}. Downloading PDF...")
            pdf_url = f"https://rtex.probablyaweb.site/api/v2/{pdf_id}/pdf"
            
            # Wait a sec for the pdf to be ready
            time.sleep(2)
            
            pdf_res = requests.get(pdf_url)
            if pdf_res.status_code == 200:
                with open("cv.pdf", "wb") as f:
                    f.write(pdf_res.content)
                print("PDF successfully saved to cv.pdf")
            else:
                print("Failed to download PDF")
        else:
            print("Compilation failed!")
            print(data)
    else:
        print(f"Request failed: {res.status_code}")
except Exception as e:
    print(e)
