from PIL import Image
import numpy as np

def sanitize_path(path):
    # Remove any invisible characters
    return path.replace('\u202a', '').replace('\u202c', '')

def encrypt_image(image_path, output_path, key):
    # Open the image
    image = Image.open(image_path)
    image_array = np.array(image)

    # Apply encryption (for simplicity, we'll add the key to each pixel value)
    encrypted_array = (image_array + key) % 256

    # Create an encrypted image from the array
    encrypted_image = Image.fromarray(encrypted_array.astype('uint8'))
    encrypted_image.save(output_path)

def decrypt_image(image_path, output_path, key):
    # Open the encrypted image
    encrypted_image = Image.open(image_path)
    encrypted_array = np.array(encrypted_image)

    # Apply decryption (subtract the key from each pixel value)
    decrypted_array = (encrypted_array - key) % 256

    # Create a decrypted image from the array
    decrypted_image = Image.fromarray(decrypted_array.astype('uint8'))
    decrypted_image.save(output_path)

def main():
    # Get user input for the mode (encrypt or decrypt)
    mode = input("Would you like to encrypt or decrypt the image? (enter 'encrypt' or 'decrypt'): ").lower()
    
    # Get user input for the image paths and the key
    image_path = sanitize_path(input("Enter the path to the image: "))
    output_path = sanitize_path(input("Enter the output path for the processed image: "))
    key = int(input("Enter the encryption/decryption key (integer): "))

    # Perform encryption or decryption based on user input
    if mode == 'encrypt':
        encrypt_image(image_path, output_path, key)
        print(f"Image encrypted successfully. Saved to {output_path}")
    elif mode == 'decrypt':
        decrypt_image(image_path, output_path, key)
        print(f"Image decrypted successfully. Saved to {output_path}")
    else:
        print("Invalid mode! Please enter 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()
