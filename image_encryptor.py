from PIL import Image
import numpy as np


ENCRYPTION_KEY = 125


def encrypt_image(input_path, output_path):
    """Encrypt the image using XOR manipulation"""
    image = Image.open(input_path)
    img_array = np.array(image)

    # XOR encryption
    encrypted_array = img_array ^ ENCRYPTION_KEY

    encrypted_img = Image.fromarray(encrypted_array.astype('uint8'))
    encrypted_img.save(output_path)
    print("Image Encrypted Successfully:", output_path)


def decrypt_image(input_path, output_path):
    """Decrypt the encrypted image using XOR manipulation"""
    image = Image.open(input_path)
    img_array = np.array(image)

    # XOR decryption (same as encryption)
    decrypted_array = img_array ^ ENCRYPTION_KEY

    decrypted_img = Image.fromarray(decrypted_array.astype('uint8'))
    decrypted_img.save(output_path)
    print("Image Decrypted Successfully:", output_path)


# RUN
if __name__ == "__main__":
    print("=== Pixel Manipulation Image Encryption Tool ===")
    print("1. Encrypt Image")
    print("2. Decrypt Image")

    choice = int(input("Enter Your Choice (1/2): "))

    if choice == 1:
        inp = input("Enter Image Path to Encrypt: ")
        out = input("Save Encrypted Image As: ")
        encrypt_image(inp, out)

    elif choice == 2:
        inp = input("Enter Encrypted Image Path: ")
        out = input("Save Decrypted Image As: ")
        decrypt_image(inp, out)

    else:
        print("Invalid Choice!")
