import os
from PIL import Image
import shutil

def convert_webp_to_jpeg(downloads_path):
    # Create a new folder for converted images
    converted_folder = os.path.join(downloads_path, 'Converted_Images')
    os.makedirs(converted_folder, exist_ok=True)
    
    # Get all WebP files in the Downloads folder
    webp_files = [f for f in os.listdir(downloads_path) if f.lower().endswith('.webp')]
    
    # Sort files to ensure consistent numbering
    webp_files.sort()
    
    # Convert and rename images
    for idx, filename in enumerate(webp_files, 1):
        try:
            # Open the WebP image
            with Image.open(os.path.join(downloads_path, filename)) as img:
                # Convert to RGB if image has transparency
                if img.mode in ('RGBA', 'LA'):
                    background = Image.new('RGB', img.size, (255, 255, 255))
                    background.paste(img, mask=img.split()[-1])
                    img = background
                
                # Create new filename
                new_filename = f"{idx:03d}.jpg"
                new_filepath = os.path.join(converted_folder, new_filename)
                
                # Save as JPEG
                img.save(new_filepath, 'JPEG')
                
                # Optional: Remove original file
                os.remove(os.path.join(downloads_path, filename))
                
                print(f"Converted {filename} to {new_filename}")
        
        except Exception as e:
            print(f"Error processing {filename}: {e}")
    
    print(f"Conversion complete. {len(webp_files)} images processed.")

def main():
    # Use the standard Windows Downloads path
    downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads')
    
    # Run the conversion
    convert_webp_to_jpeg(downloads_path)

if __name__ == "__main__":
    main()