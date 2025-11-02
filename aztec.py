import zxingcpp
from PIL import Image
import sys

def decode_aztec(image_path):
    try:
        img = Image.open(image_path)
        result = zxingcpp.read_barcode(img)

        if result is None:
            return "❌ No Aztec code detected in the image."

        if result.format.name != "AZTEC":
            return f"⚠️ Detected {result.format.name}, not an Aztec code."

        return f"✅ Aztec Decoded Text: {result.text}"

    except FileNotFoundError:
        return f"⚠️ File not found: {image_path}"
    except Exception as e:
        return f"❌ Error: {str(e)}"


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python aztec_reader.py <image_path>")
        sys.exit(1)

    print(decode_aztec(sys.argv[1]))
