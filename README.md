Here’s an upgraded version of your `README.md` with:

* ✅ **Badges**
* 🖼️ **Image preview**
* ⚙️ **CI/CD placeholder**
* 💡 **Optional enhancements for contributors**

---

````markdown
# 🗂️ File Organizer

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/status-active-brightgreen)

A clean and simple Python script that organizes your messy folders by sorting files into categorized subfolders. Perfect for your `Downloads`, `Desktop`, or project folders!


## 📌 Features

- 📁 Automatically creates folders: `Images`, `Videos`, `Documents`, `Music`, `Code`, `Archives`, `Executables`, etc.
- 🧠 Smart mapping of file extensions to categories
- ⚙️ Easy customization for specific needs
- 💻 Lightweight and dependency-free

---

## 🚀 How to Use

### 1. Clone the Repository

```bash
git clone https://github.com/nikhildhanda04/file-organizer.git
cd file-organizer
````

### 2. Run the Script

```bash
python organizer.py
```

### 3. Input Folder Path

You'll be prompted to enter the folder path to organize. The script does the rest.

---

## 🧠 How It Works

The script uses a dictionary (`EXTENSIONS`) to map file types to folder names:

```python
EXTENSIONS = {
    "Images": ['.png', '.jpg', '.jpeg', '.gif'],
    "Documents": ['.pdf', '.docx', '.txt'],
    "Videos": ['.mp4', '.mkv'],
    ...
}
```

You can edit this mapping in `organizer.py` to suit your needs.

---

## ⚙️ Requirements

* Python 3.x
  No additional libraries needed — built with standard Python libraries only.

---

## 🤝 Contributing

Pull requests and stars are always welcome! 🌟
If you'd like to improve the script or add features, feel free to:

```bash
git checkout -b your-feature-branch
```

---

## 🧪 Future Enhancements (Ideas)

* [ ] GUI version using Tkinter or PyQt
* [ ] Real-time folder monitoring
* [ ] Scheduling with cron or Task Scheduler
* [ ] CLI flags for silent mode or custom mapping



## 👤 Author

Made with ❤️ by [Nikhil Dhanda](https://github.com/nikhildhanda04)


