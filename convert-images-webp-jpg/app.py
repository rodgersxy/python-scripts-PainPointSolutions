import os
from PIL import Image
import glob

def convert_and_rename_images():
    # Define paths
    downloads_folder = os.path.expanduser("~/Downloads")
    output_folder = os.path.join(downloads_folder, "37ON-KIKAMBALA")
    
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    # Find all WebP files in Downloads folder
    webp_files = glob.glob(os.path.join(downloads_folder, "*.webp"))
    
    for index, webp_file in enumerate(webp_files, start=1):
        try:
            # Open WebP image
            with Image.open(webp_file) as img:
                # Create new filename
                new_filename = f"{index}.jpg"
                output_path = os.path.join(output_folder, new_filename)
                
                # Convert and save as JPG
                img.convert("RGB").save(output_path, "JPEG")
                print(f"Converted {os.path.basename(webp_file)} to {new_filename}")
                
        except Exception as e:
            print(f"Error converting {webp_file}: {str(e)}")
    
    print(f"\nConversion complete. {len(webp_files)} images processed.")
    print(f"Converted images are stored in: {output_folder}")

if __name__ == "__main__":
    convert_and_rename_images()