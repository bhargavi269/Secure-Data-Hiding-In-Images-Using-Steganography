import cv2
import os

def hide_message(image_path, message, password):
    """
    Hides a secret message within an image.

    Args:
        image_path (str): Path to the image file.
        message (str): Secret message to hide.
        password (str): Password for decryption.

    Returns:
        None
    """
    try:
        img = cv2.imread(image_path)
        if img is None:
            raise FileNotFoundError("Image file not found.")

        d = {chr(i): i for i in range(255)}
        m = 0
        n = 0
        z = 0

        for i in range(len(message)):
            img[n, m, z] = d[message[i]]
            n = (n + 1) % img.shape[0]
            m = (m + 1) % img.shape[1]
            z = (z + 1) % 3

        cv2.imwrite("encryptedimage.jpg", img)
        os.system("start encryptedImage.jpg")  # Use 'start' to open the image on Windows

    except FileNotFoundError as e:
        print(f"Error: {e}")

def main():
    image_path = "my pic.jpg"
    message = input("Enter secret message: ")
    password = input("Enter a passcode: ")

    hide_message(image_path, message, password)
    print("Image encrypted successfully!")

if __name__ == "__main__":
    main()
