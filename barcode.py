import zxingcpp
from PIL import Image
import sys

def decode_barcode(image_path):
    try:
        img = Image.open(image_path)
        results = zxingcpp.read_barcodes(img)

        if not results:
            return "❌ No barcode detected in this image."

        output = []
        for result in results:
            output.append(
                f"📌 Type: {result.format.name}\n"
                f"✅ Data: {result.text}\n"
                f"📍 Position: {result.position}\n"
                "-------------------------"
            )
        return "\n".join(output)

    except FileNotFoundError:
        return f"⚠️ File not found: {image_path}"
    except Exception as e:
        return f"❌ Error: {str(e)}"


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python decode_barcode.py <image_path>")
        sys.exit(1)

    print(decode_barcode(sys.argv[1]))
