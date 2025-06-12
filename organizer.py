import os
import shutil

FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".py", ".js", ".html", ".css", ".cpp", ".java", ".c", ".ipynb"],
    "Executables": [".exe", ".msi", ".bat"],
    "Others": []
}

def get_category(extension):
    for category, extensions in FILE_CATEGORIES.items():
        if extension.lower() in extensions:
            return category
    return "Others"

def organize_folder(folder_path):
    if not os.path.exists(folder_path):
        print("❌ The folder does not exist.")
        return

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isdir(file_path):
            continue

        file_ext = os.path.splitext(filename)[1]
        category = get_category(file_ext)
        category_folder = os.path.join(folder_path, category)

        if not os.path.exists(category_folder):
            os.makedirs(category_folder)

        try:
            shutil.move(file_path, os.path.join(category_folder, filename))
            print(f"✅ Moved: {filename} ➝ {category}")
        except Exception as e:
            print(f"❌ Error moving {filename}: {e}")

if __name__ == "__main__":
    folder = input("📁 Enter the full folder path to organize: ").strip()
    organize_folder(folder)

