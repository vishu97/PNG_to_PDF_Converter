# 📄 PNG to PDF Converter

A simple, standalone tool that converts multiple PNG images into a single PDF file. Perfect for combining scanned pages, screenshots, or any series of images.

## ✨ Features

- 🎯 **Automatic Detection** - Finds all `page-*.png` files in the folder
- 🔢 **Smart Sorting** - Orders pages numerically (page-1, page-2, page-3...)
- 🎨 **Transparency Handling** - Converts RGBA images to RGB with white background
- 📦 **Single File Output** - Creates `combined_pages.pdf` in the same folder
- 💻 **No Installation** - Standalone .exe requires no Python installation

## 🚀 Quick Start (Using .EXE)

### Step 1: Download
Download `PNG_to_PDF_Converter.exe` from the [Releases](../../releases) page

### Step 2: Prepare Your Images
Make sure your PNG files are named in this format:
```
page-1.png
page-2.png
page-3.png
...
```

### Step 3: Run
1. 📂 Copy the `.exe` file to the **same folder** as your images
2. 🖱️ Double-click `PNG_to_PDF_Converter.exe`
3. ✅ Wait for conversion to complete
4. 📑 Find your `combined_pages.pdf` in the same folder!

## 🛠️ How It Works

```
📁 Your Folder
├── PNG_to_PDF_Converter.exe  ← Place exe here
├── page-1.png                 ← Your images
├── page-2.png
├── page-3.png
└── ...

         ↓ (Run the exe)

📁 Your Folder
├── PNG_to_PDF_Converter.exe
├── page-1.png
├── page-2.png
├── page-3.png
├── ...
└── combined_pages.pdf         ← Output PDF created! ✨
```

### Processing Steps:
1. 🔍 **Scan** - Searches current directory for `page-*.png` files
2. 📊 **Sort** - Arranges files by page number
3. 🖼️ **Convert** - Converts RGBA/other formats to RGB
4. 📄 **Merge** - Combines all images into single PDF
5. 💾 **Save** - Creates `combined_pages.pdf` with 95% quality

---

## 🐍 For Developers (Python Script)

### Prerequisites
```bash
pip install Pillow
```

### Installation
```bash
git clone https://github.com/yourusername/png-to-pdf-converter.git
cd png-to-pdf-converter
```

### Basic Usage
```python
python png_to_pdf.py
```

### 🔧 Customization Guide

#### Change Output PDF Name
```python
# Find this line (around line 62):
output_path = current_dir / "combined_pages.pdf"

# Change to your preferred name:
output_path = current_dir / "my_document.pdf"
```

#### Change Image Pattern
```python
# Find this line (around line 26):
png_files = list(current_dir.glob("page-*.png"))

# Examples:
png_files = list(current_dir.glob("scan-*.png"))  # For scan-1.png, scan-2.png
png_files = list(current_dir.glob("img-*.png"))   # For img-1.png, img-2.png
png_files = list(current_dir.glob("*.png"))       # For any PNG file
```

#### Adjust PDF Quality
```python
# Find this section (around line 55):
images[0].save(
    output_path,
    save_all=True,
    append_images=images[1:] if len(images) > 1 else [],
    resolution=100.0,
    quality=95,  # ← Change this (1-100)
    optimize=True
)

# Examples:
quality=100  # Highest quality (larger file)
quality=85   # Good quality (smaller file)
quality=75   # Lower quality (smallest file)
```

#### Change Background Color (for transparent PNGs)
```python
# Find this line (around line 40):
rgb_img = Image.new('RGB', img.size, (255, 255, 255))

# Change RGB values:
rgb_img = Image.new('RGB', img.size, (0, 0, 0))       # Black background
rgb_img = Image.new('RGB', img.size, (240, 240, 240)) # Light gray
```

#### Process Images from Different Folder
```python
# Change this section (around line 15):
if getattr(sys, 'frozen', False):
    current_dir = Path(os.path.dirname(sys.executable))
else:
    current_dir = Path(os.path.dirname(os.path.abspath(__file__)))

# To use a specific folder:
current_dir = Path(r"C:\Users\YourName\Documents\Images")
```

### 🏗️ Building Your Own .EXE

#### Install PyInstaller
```bash
pip install pyinstaller
```

#### Create Executable (with console window)
```bash
pyinstaller --onefile --name "PNG_to_PDF_Converter" png_to_pdf.py
```

#### Create Executable (no console window)
```bash
pyinstaller --onefile --noconsole --name "PNG_to_PDF_Converter" png_to_pdf.py
```

#### 📍 Find Your .EXE
```
dist/PNG_to_PDF_Converter.exe  ← Your executable is here!
```

#### Custom Icon (Optional)
```bash
pyinstaller --onefile --icon=icon.ico --name "PNG_to_PDF_Converter" png_to_pdf.py
```

---

## 📋 Requirements

### For .EXE Users
- ✅ Windows 10/11 (64-bit)
- ✅ No additional software needed

### For Python Users
- 🐍 Python 3.7+
- 📦 Pillow library (`pip install Pillow`)

## 🤝 Contributing

Feel free to:
- 🐛 Report bugs
- 💡 Suggest features
- 🔀 Submit pull requests

## 📄 License

MIT License - feel free to use and modify!

## ❓ Troubleshooting

### "No PNG files found" Error
- ✅ Ensure files are named `page-1.png`, `page-2.png`, etc.
- ✅ Check the .exe is in the same folder as images

### PDF Quality Issues
- 🔧 Modify `quality=95` parameter in the script (see customization guide)
- 📏 Ensure source images are high resolution

### Large File Sizes
- 🗜️ Reduce quality parameter (try `quality=85`)
- 📉 Compress source images before conversion

---

Made with ❤️ for easy PDF conversion
