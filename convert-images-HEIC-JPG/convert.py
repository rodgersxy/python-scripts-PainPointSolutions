import os
from pathlib import Path
import pillow_heif
from PIL import Image
import concurrent.futures

def convert_heic_to_jpg(heic_path, jpg_path):
    """
    Convert a single HEIC file to JPG format.
    
    :param heic_path: Path to the input HEIC file
    :param jpg_path: Path to save the output JPG file
    """
    try:
        heif_file = pillow_heif.read_heif(heic_path)
        image = Image.frombytes(
            heif_file.mode, 
            heif_file.size, 
            heif_file.data,
            "raw",
            heif_file.mode,
            heif_file.stride,
        )
        image.save(jpg_path, "JPEG", quality=95)
        print(f"Converted: {heic_path} -> {jpg_path}")
    except Exception as e:
        print(f"Error converting {heic_path}: {str(e)}")

def process_downloads_folder():
    """
    Process all HEIC files in the Downloads folder and convert them to JPG.
    """
    downloads_path = Path.home() / "Downloads"
    output_folder = downloads_path / "Escada-2br-17.5M"
    
    output_folder.mkdir(exist_ok=True)

    heic_files = list(downloads_path.glob("*.HEIC")) + list(downloads_path.glob("*.heic"))
    
    if not heic_files:
        print("No HEIC files found in the Downloads folder.")
        return

    print(f"Found {len(heic_files)} HEIC files. Starting conversion...")

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for heic_file in heic_files:
            jpg_file = output_folder / (heic_file.stem + ".jpg")
            futures.append(executor.submit(convert_heic_to_jpg, str(heic_file), str(jpg_file)))
        
        concurrent.futures.wait(futures)

    print("Conversion complete. Check the 'Converted_JPGs' folder in your Downloads directory.")

if __name__ == "__main__":
    process_downloads_folder()