import os
from PIL import Image
import shutil
from pathlib import Path

def get_downloads_folder():
    """Get the path to the Downloads folder"""
    return str(Path.home() / "Downloads")

def create_output_folder(downloads_path):
    """Create output folder for resized images"""
    output_folder = os.path.join(downloads_path, "Escada-studio-201-furnished-125k")
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    return output_folder

def reduce_image_size(image_path, output_path, max_size_mb=10):
    """Reduce image size while maintaining aspect ratio"""
    # Open the image
    img = Image.open(image_path)
    
    # Convert to RGB if image is in RGBA mode
    if img.mode == 'RGBA':
        img = img.convert('RGB')
    
    # Initial quality
    quality = 95
    
    while True:
        # Save image temporarily to check size
        img.save(output_path, 'JPEG', quality=quality)
        
        # Check file size
        size_mb = os.path.getsize(output_path) / (1024 * 1024)
        
        if size_mb <= max_size_mb or quality <= 5:
            break
            
        # Reduce quality for next iteration
        quality -= 5

def process_images():
    """Main function to process images"""
    # Get Downloads folder path
    downloads_path = get_downloads_folder()
    
    # Create output folder
    output_folder = create_output_folder(downloads_path)
    
    # Supported image formats
    image_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.webp')
    
    # Process each image
    for filename in os.listdir(downloads_path):
        if filename.lower().endswith(image_extensions):
            input_path = os.path.join(downloads_path, filename)
            
            # Check if file is larger than 10MB
            size_mb = os.path.getsize(input_path) / (1024 * 1024)
            
            if size_mb > 10:
                print(f"Processing {filename} ({size_mb:.2f}MB)...")
                
                # Create output path
                output_path = os.path.join(output_folder, filename)
                
                try:
                    # Reduce image size
                    reduce_image_size(input_path, output_path)
                    
                    # Delete original file after successful resize
                    os.remove(input_path)
                    print(f"Successfully processed {filename}")
                    
                except Exception as e:
                    print(f"Error processing {filename}: {str(e)}")
            else:
                print(f"Skipping {filename} ({size_mb:.2f}MB) - already under 10MB")

if __name__ == "__main__":
    process_images()