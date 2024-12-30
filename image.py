from PIL import Image

def swap_pixels(image):
    pixels = list(image.getdata())
    width, height = image.size
    swapped_pixels = []

    for i in range(0, len(pixels), 2):
        if i + 1 < len(pixels):
            swapped_pixels.extend([pixels[i + 1], pixels[i]])
        else:
            swapped_pixels.append(pixels[i])

    new_image = Image.new(image.mode, (width, height))
    new_image.putdata(swapped_pixels)
    return new_image

def apply_math_operation(image, operation):
    pixels = list(image.getdata())
    width, height = image.size

    modified_pixels = [
        tuple(operation(channel) for channel in pixel)
        for pixel in pixels
    ]

    new_image = Image.new(image.mode, (width, height))
    new_image.putdata(modified_pixels)
    return new_image

def main():
    print("Welcome to the Image Encryption Tool!")
    image_path = input("Enter the path to the image: ").strip()

    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"Error loading image: {e}")
        return

    while True:
        print("\nChoose an operation:")
        print("1. Swap adjacent pixels")
        print("2. Apply a mathematical operation to each pixel")
        print("3. Quit")
        choice = input("Your choice: ").strip()

        if choice == '1':
            image = swap_pixels(image)
            print("Swapped adjacent pixels.")
        elif choice == '2':
            print("Available operations: add, subtract, multiply, divide")
            operation = input("Enter the operation (e.g., 'add 50'): ").strip()

            try:
                op, value = operation.split()
                value = int(value)

                if op == 'add':
                    func = lambda x: min(x + value, 255)
                elif op == 'subtract':
                    func = lambda x: max(x - value, 0)
                elif op == 'multiply':
                    func = lambda x: min(x * value, 255)
                elif op == 'divide':
                    func = lambda x: max(x // value, 0) if value != 0 else x
                else:
                    print("Invalid operation.")
                    continue

                image = apply_math_operation(image, func)
                print(f"Applied {op} operation with value {value}.")
            except Exception as e:
                print(f"Error applying operation: {e}")
        elif choice == '3':
            save_path = input("Enter the path to save the modified image: ").strip()
            try:
                image.save(save_path)
                print(f"Image saved to {save_path}.")
            except Exception as e:
                print(f"Error saving image: {e}")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
