#%%
import logging, os
from youtubesearchpython import *
from youtubesearchpython import ChannelsSearch
from fastapi import BackgroundTasks, FastAPI
from configparser import ConfigParser
import uvicorn
import TaskState

app = FastAPI()

config_object = ConfigParser()
config_object.read("config.ini")
CONFIG = config_object["SETTINGS"]

folder=CONFIG["download_folder"]
LOGFOLDER=CONFIG["log_folder"]
LOGFILENAME=CONFIG["logfile_name"]
limit=CONFIG["download_limit"]

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



state = TaskState.TaskState()

@app.post('/download-video')
async def main_56(background_tasks: BackgroundTasks,id: str = "",name: str = "", limit: int = int(limit),folder:str =folder):
    try:
        if id !="" and name!="":
            name=""
        ydl_opts = {'outtmpl': f'{folder}/%(title)s.%(ext)s','max_downloads':limit}
        if id!="":
            playlist = Playlist(playlist_from_channel_id(id))
        background_tasks.add_task(state.getResult,id,name,limit,ydl_opts,folder)
        return {'status':"Task Added Sucessfully!","message":f"Video downloading in {folder}","channel":f"{id} {name}"}

    except Exception as e:
        return {'status':"Task failed!",'error': f'Something went wrong! Check Channel Name or Id',"channel":f"{id} {name}"}

# @app.get("/get_status")
# def status():
#     return state.get_state()

if __name__ == '__main__':
    uvicorn.run(app)
#%%