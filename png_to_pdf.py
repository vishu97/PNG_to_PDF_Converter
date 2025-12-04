"""
PNG to PDF Converter - Executable Version
Simply place this .exe in the folder with your page-*.png images and run it!
"""

from PIL import Image
import os
from pathlib import Path
import sys

def convert_images_to_pdf():
    """
    Convert PNG images in current directory to a single PDF file.
    """
    # Get the directory where the exe is located
    if getattr(sys, 'frozen', False):
        # Running as compiled executable
        current_dir = Path(os.path.dirname(sys.executable))
    else:
        # Running as script
        current_dir = Path(os.path.dirname(os.path.abspath(__file__)))

    print("=" * 60)
    print("PNG to PDF Converter")
    print("=" * 60)
    print(f"\nScanning folder: {current_dir}\n")

    # Find all page-*.png files and sort them numerically
    png_files = list(current_dir.glob("page-*.png"))

    if not png_files:
        print("❌ No PNG files found matching 'page-*.png' pattern!")
        print("\nMake sure your images are named:")
        print("   page-1.png, page-2.png, page-3.png, etc.")
        input("\nPress Enter to exit...")
        return

    # Sort by page number
    try:
        png_files.sort(key=lambda x: int(x.stem.split('-')[1]))
    except:
        png_files.sort()  # Fallback to alphabetical sort

    print(f"✓ Found {len(png_files)} images:")
    for img in png_files:
        print(f"  📄 {img.name}")

    print("\n🔄 Converting to PDF...")

    # Open all images and convert to RGB
    images = []
    try:
        for png_file in png_files:
            img = Image.open(png_file)
            # Convert RGBA to RGB if needed
            if img.mode == 'RGBA':
                rgb_img = Image.new('RGB', img.size, (255, 255, 255))
                rgb_img.paste(img, mask=img.split()[3])
                images.append(rgb_img)
            elif img.mode != 'RGB':
                images.append(img.convert('RGB'))
            else:
                images.append(img)

        # Save as PDF
        output_path = current_dir / "combined_pages.pdf"
        if len(images) > 0:
            images[0].save(
                output_path,
                save_all=True,
                append_images=images[1:] if len(images) > 1 else [],
                resolution=100.0,
                quality=95,
                optimize=True
            )
            print(f"\n✅ SUCCESS! PDF created: {output_path.name}")
            print(f"📊 Total pages: {len(images)}")
            print(f"📍 Location: {output_path}")
        else:
            print("\n❌ Error: No images to convert!")

    except Exception as e:
        print(f"\n❌ Error occurred: {str(e)}")

    print("\n" + "=" * 60)
    input("Press Enter to exit...")

if __name__ == "__main__":
    convert_images_to_pdf()
