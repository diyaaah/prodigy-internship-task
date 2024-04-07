from PIL import Image

def encrypt_image(image_path):
    # Open the image
    img = Image.open(image_path)
    width, height = img.size
    
    # Iterate through each pixel and perform encryption
    for x in range(width):
        for y in range(height):
            r, g, b = img.getpixel((x, y))
            # Swap the RGB values
            img.putpixel((x, y), (g, b, r))
    
    # Save the encrypted image
    img.save("encrypted_image.png")
    print("Image encrypted successfully!")

def decrypt_image(encrypted_image_path):
    # Open the encrypted image
    encrypted_img = Image.open(encrypted_image_path)
    width, height = encrypted_img.size
    
    # Iterate through each pixel and perform decryption
    for x in range(width):
        for y in range(height):
            r, g, b = encrypted_img.getpixel((x, y))
            # Swap the RGB values back to original
            encrypted_img.putpixel((x, y), (b, r, g))
    
    # Save the decrypted image
    encrypted_img.save("decrypted_image.png")
    print("Image decrypted successfully!")

def main():
    image_path = input("Enter the path of the image to encrypt: ")
    encrypt_image(image_path)
    
    encrypted_image_path = "encrypted_image.png"
    decrypt_image(encrypted_image_path)

if __name__ == "__main__":
    main()
