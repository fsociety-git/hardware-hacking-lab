import argparse
import binwalk

def extract_firmware(file_path, output_dir):
    modules = binwalk.scan(file_path, signature=True, quiet=True, extract=True, dd='.*', directory=output_dir)
    for module in modules:
        print(f"Extracted: {module.extracted}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Firmware Extractor")
    parser.add_argument("--file", required=True, help="Path to firmware file")
    parser.add_argument("--output", default="extracted", help="Output directory")
    args = parser.parse_args()
    extract_firmware(args.file, args.output)
