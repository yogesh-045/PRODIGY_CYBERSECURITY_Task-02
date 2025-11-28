# PRODIGY_CYBERSECURITY_Task-02
# Pixel Manipulation Image Encryption Tool


This project is a simple **image encryption & decryption tool** based on **pixel manipulation**.  
It applies a reversible **XOR operation** on every pixel to secure the image.


## 🔥 Features
- Encrypt any image using pixel XOR manipulation  
- Decrypt encrypted image back to original  
- Reversible & lossless encryption  
- Works for PNG/JPG images  
- Simple Python script, beginner-friendly  


## 🛠 Technologies Used
- Python
- NumPy
- Pillow (PIL)


## 📌 How It Works
Each pixel value is XORed with a numeric key:
EncryptedPixel = OriginalPixel XOR KEY
DecryptedPixel = EncryptedPixel XOR KEY


Using the same KEY, the image can be decrypted perfectly.


## ▶️ How to Run

### Install Required Libraries
pip install pillow numpy

### Run Script
python image_encryptor.py


### Choose:
1 → Encrypt  
2 → Decrypt  


## 📁 Output Files
- `encrypted.png`
- `decrypted.png`


## ✨ Example
Before → Encrypt → Decrypt (restores original image)



