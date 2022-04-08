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
pip3.7 install FastAPI
pip3.7 install uvicorn
pip3.7 install youtube-dl
pip3.7 install yt-dlp
pip3.7 install youtube-search-python
pip3.7 install flask
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
python3.7 scarpeYouTube.py
```

### Send Request 
It will create a folder and start downloading video in background (async task).
```
http://<server_ip/local_ip>:8000/download-video?name=Tech Burner
```
Import the "youTubeScrape.postman_collection.json" file in postman to find more request options.
