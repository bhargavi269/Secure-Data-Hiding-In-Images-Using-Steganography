import cv2

def extract_message(image_path, password, original_message_length):
    """
    Extracts the hidden message from an image.

    Args:
        image_path (str): Path to the encrypted image file.
        password (str): Password for decryption.
        original_message_length (int): Length of the original message.

    Returns:
        str: Extracted message or error message.
    """
    try:
        img = cv2.imread(image_path)
        if img is None:
            raise FileNotFoundError("Image file not found.")

        c = {i: chr(i) for i in range(255)}
        message = ""
        n = 0
        m = 0
        z = 0

        pas = input("Enter passcode for Decryption: ")
        if password == pas:
            for i in range(original_message_length):
                message += c[img[n, m, z]]
                n = (n + 1) % img.shape[0]
                m = (m + 1) % img.shape[1]
                z = (z + 1) % 3
            return message
        else:
            return "YOU ARE NOT auth"

    except FileNotFoundError as e:
        print(f"Error: {e}")

def main():
    image_path = "encryptedimage.jpg"
    password = input("Enter the passcode used for encryption: ")
    original_message_length = int(input("Enter the length of the original message: "))

    extracted_message = extract_message(image_path, password, original_message_length)
    print("Image Decrypted successfully!")

if __name__ == "__main__":
    main()
