#%%
import logging, os
from youtubesearchpython import *
from youtubesearchpython import ChannelsSearch
from flask import Flask, request
from yt_dlp import YoutubeDL
from fastapi import FastAPI
from configparser import ConfigParser
import uvicorn

config_object = ConfigParser()
config_object.read("config.ini")
CONFIG = config_object["SETTINGS"]

#folder=CONFIG["download_folder"]
LOGFOLDER=CONFIG["log_folder"]
LOGFILENAME=CONFIG["logfile_name"]

try:
     os.makedirs(os.path.join(os.getcwd(),LOGFOLDER))
except:
     pass

logname = os.path.join(os.getcwd(),LOGFOLDER,LOGFILENAME)
logging.basicConfig(filename=logname,
                              filemode='a',
                              format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                              datefmt='%H:%M:%S',
                              level=logging.DEBUG)

logger = logging.getLogger('urbanGUI')

class TaskState:

    def __init__(self):
        self.video_url = []
        self.limit=-1
        self.isDone=False
        self.channel_id=""

    def getResult(self,channel_id,channel_name,download_limit,ydl_opts,folder):
        self.limit=download_limit
        #self.isDone
        if channel_name!='' and channel_id=='':
            channelsSearch = ChannelsSearch(channel_name,limit = 1)
            if len(channelsSearch.result()['result'])!=0:
                channel_id=channelsSearch.result()['result'][0]['id']

        self.channel_id=channel_id
        self.video_url=[]
        if channel_id!='':
            playlist = Playlist(playlist_from_channel_id(channel_id))
            for i in playlist.videos:
                if len(self.video_url)>=download_limit:
                    break
                self.video_url.append(i['link'])

            if len(self.video_url)<download_limit:
                while playlist.hasMoreVideos:
                    playlist.getNextVideos()
                    for i in playlist.videos:
                        if len(self.video_url)>=download_limit:
                            break
                        self.video_url.append(i['link'])

            try:
                for i in self.video_url:
                    with YoutubeDL(ydl_opts) as ydl:
                        ydl.download([i])
            except Exception:
                self.isDone=True
                pass
            
            #self.limit=-1
            logging.info(f'Video Downloaded for channel ID:{channel_id} Total Video: {len(self.video_url)} Destination Folder: {folder}')
                    
    # def get_state(self):
    #     if self.limit==-1:
    #         return {'status':200, "message":"Task not added"}
    #     elif self.isDone==False:
    #         return {'status':200, "message":f"Downloading! for channel ID: {self.channel_id}"}
    #     else:
    #         #self.isDone=False
    #         #self.limit==-1
    #         TaskState()
    #         return {'status':200, "message":f"Download completed for channel ID: {self.channel_id}"}