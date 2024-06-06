# Image Encryption Tool

This Python script allows you to encrypt and decrypt images using pixel manipulation. The tool modifies pixel values by applying a mathematical operation based on a key, making it easy to protect the contents of your images.

## Features

- Encrypt images by shifting pixel values.
- Decrypt images by reversing the pixel value shift.
- Supports both encryption and decryption modes.
- Handles images in various formats (e.g., PNG, JPEG).

## Installation

### Prerequisites

- Python 3.x
- Pillow library

### Install Pillow

You can install the Pillow library using pip:

```bash
pip install pillow
```

## Usage

### Clone the Repository

```bash
git clone https://github.com/amitraj29/PRODIGY_CS_02.git
cd PRODIGY_CS_02
```

### Run the Script

You can run the script on any operating system with Python installed. Follow the specific instructions for your OS below.

### Windows

1. Open Command Prompt.
2. Navigate to the directory where the script is located.
3. Run the script:

```bash
python image_encryption.py
```

### macOS and Linux

1. Open Terminal.
2. Navigate to the directory where the script is located.
3. Run the script:

```bash
python3 image_encryption.py
```

### How to Use

1. **Follow the prompts**:
   - Enter 'encrypt' or 'decrypt' to choose the mode.
   - Provide the path to the input image.
   - Provide the output path where the processed image will be saved.
   - Enter an integer key for encryption/decryption.

### Example

#### Encrypting an Image

```
Would you like to encrypt or decrypt the image? (enter 'encrypt' or 'decrypt'): encrypt
Enter the path to the image: C:\Users\rajka\Downloads\Image.png
Enter the output path for the processed image: C:\Users\rajka\Downloads\EncryptedImage.png
Enter the encryption/decryption key (integer): 50
Image encrypted successfully. Saved to C:\Users\rajka\Downloads\EncryptedImage.png
```

#### Decrypting an Image

```
Would you like to encrypt or decrypt the image? (enter 'encrypt' or 'decrypt'): decrypt
Enter the path to the image: C:\Users\rajka\Downloads\EncryptedImage.png
Enter the output path for the processed image: C:\Users\rajka\Downloads\DecryptedImage.png
Enter the encryption/decryption key (integer): 50
Image decrypted successfully. Saved to C:\Users\rajka\Downloads\DecryptedImage.png
```

## Code Explanation

### `encrypt_image` Function

This function takes the image path, output path, and key as input. It reads the image, applies the encryption by adding the key to each pixel value, and saves the encrypted image.

### `decrypt_image` Function

This function takes the image path, output path, and key as input. It reads the encrypted image, applies the decryption by subtracting the key from each pixel value, and saves the decrypted image.

### `main` Function

Handles user interaction, gets the mode (encrypt or decrypt), image paths, and key from the user, and calls the appropriate function to process the image.

## Contributing

Feel free to fork this repository, make improvements, and submit pull requests. Contributions are welcome!

## Contact

For any questions or suggestions, please open an issue or contact me at amitrajkarmakar29@gmail.com.
