import zxingcpp
from PIL import Image
import sys

def decode_qr(image_path):
    try:
        img = Image.open(image_path)
        result = zxingcpp.read_barcode(img)

        if result is None:
            return "❌ No QR Code found in this image."

        if result.format.name != "QR_CODE":
            return f"⚠️ Detected {result.format.name}, not a QR Code."

        return f"✅ QR Code Data: {result.text}"

    except FileNotFoundError:
        return f"⚠️ File not found: {image_path}"
    except Exception as e:
        return f"❌ Error: {str(e)}"


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python decode_qr.py <image_path>")
        sys.exit(1)

    print(decode_qr(sys.argv[1]))
