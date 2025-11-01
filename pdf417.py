from pdf417decoder import PDF417Decoder
from PIL import Image
import sys


def read_barcode(image_path):
    try:
        print(f"Reading: {image_path}\n")

        # Load image with PIL
        image = Image.open(image_path)

        # Create decoder
        decoder = PDF417Decoder(image)

        # Decode
        count = decoder.decode()

        if count > 0:
            print(f"✅ Found {count} barcode(s)\n")
            print("=" * 80)

            # Loop through each barcode by index
            for i in range(count):
                barcode_data = decoder.barcode_data_index_to_string(i)
                print(f"\nBarcode #{i + 1}:")
                print(barcode_data)
                print("=" * 80)

            # Save to file
            with open("decoded_output.txt", "w", encoding="utf-8") as f:
                for i in range(count):
                    barcode_data = decoder.barcode_data_index_to_string(i)
                    f.write(f"Barcode #{i + 1}:\n")
                    f.write(barcode_data + "\n\n")
                    f.write("=" * 80 + "\n\n")
            print("\n💾 Saved to: decoded_output.txt")
        else:
            print("❌ No barcodes detected")

    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    image_path = "barcode.jpg"
    if len(sys.argv) > 1:
        image_path = sys.argv[1]

    read_barcode(image_path)