from django.shortcuts import render
import pytesseract
import numpy as np
from PIL import Image
import base64
pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\\tesseract.exe'
def index(request):
    if request.method=="POST":
        image=request.FILES["image"]
        image_data = base64.b64encode(image.read()).decode('utf-8')
        img = np.array(Image.open(image))
        
        text=pytesseract.image_to_string(img)
        return render(request, "core/index.html", {
            "ocr": text,
            "image":image_data})
    return render(request,"core/index.html")