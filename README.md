# Scrape-YouTube
## Getting Started

The below steps will get you a copy of this repository up and running on your local machine for testing purposes.

### Clone the Repository
```
git clone https://github.com/mahipalsingh26/Scrape-YouTube.git
```

### Installation
1. Install additional:
```
pip install FastAPI
pip install uvicon
pip install youtube-dl
pip install yt-dlp
pip install youtube-search-python
```

### Configure
Open `config.ini` file and Make the changes defaults if required.
```
[SETTINGS]
download_folder =output
logfile_name=track.log
log_folder=logScrape
download_limit=5
```
### Run
```
python scarpeYouTube.py
```

### Send Request 
It will create a folder and start downloading video in background (async task).
```
http://127.0.0.1:8000/download-video?name=Tech Burner
```
Import the "youTubeScrape.postman_collection.json" file in postman to find more request options.
