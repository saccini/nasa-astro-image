# 🚀 NASA Astro Image Downloader

This project downloads the Astronomy Picture of the Day (APOD) from NASA's public API.  
You can enter a date and get the image, along with metadata.


## ⚙️ How to Use

### 1. 🐍 Run with Python

```
pip install -r requirements.txt
python main.py 
```
Note: You'll be asked to enter a date in the format YYYY-MM-DD.

### 2. 🐳 Run with Docker
```
docker build -t nasa-astro-image .

docker run -it \
  -v "$(pwd)/images:/app/images" \
  -v "$(pwd)/data:/app/data" \
  nasa-astro-image
```
The -it flag enables interactive mode to prompt you for a date.

## 📦 Output

Image saved in images/
Metadata saved to data/metadata.csv

## 🗂 Project Structure

```
nasa-astro-image/
├── main.py 
├── requirements.txt 
├── Dockerfile 
├── docker-compose.yml 
├── .gitignore
├── .dockerignore
├── images/ 
├── metadata.csv 
|   └── metadata.csv  
└── README.md
```

### 📡 NASA APOD API

More info: https://api.nasa.gov