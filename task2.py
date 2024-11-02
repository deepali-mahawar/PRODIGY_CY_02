import cv2

def encrypt_image(image_path, key):
    """Encrypts an image using a simple XOR operation with a key.

    Args:
        image_path (str): Path to the image file.
        key (int): The encryption key.

    Returns:
        numpy.ndarray: The encrypted image.
    """

    image = cv2.imread(image_path)
    encrypted_image = image.copy()
    for y in range(encrypted_image.shape[0]):
        for x in range(encrypted_image.shape[1]):
            for channel in range(encrypted_image.shape[2]):
                encrypted_image[y, x, channel] = image[y, x, channel] ^ key

    return encrypted_image

def decrypt_image(encrypted_image, key):
    """Decrypts an image using the same XOR operation and key.

    Args:
        encrypted_image (numpy.ndarray): The encrypted image.
        key (int): The decryption key.

    Returns:
        numpy.ndarray: The decrypted image.
    """

    decrypted_image = encrypted_image.copy()
    for y in range(decrypted_image.shape[0]):
        for x in range(decrypted_image.shape[1]):
            for channel in range(decrypted_image.shape[2]):
                decrypted_image[y, x, channel] = encrypted_image[y, x, channel] ^ key

    return decrypted_image

# Example usage:
image_path = "input_image.jpg"
key = 42

encrypted_image = encrypt_image(image_path, key)
cv2.imwrite("encrypted_image.jpg", encrypted_image)

decrypted_image = decrypt_image(encrypted_image, key)
cv2.imwrite("decrypted_image.jpg", decrypted_image) 