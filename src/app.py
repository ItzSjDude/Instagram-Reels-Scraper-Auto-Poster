import time
import config
import helpers as Helper
import reels, poster, shorts, remover
from instagrapi import Client
import auth
from rich import print
from datetime import datetime, timedelta
import random

def run_scheduler():
    Helper.load_all_config()

    next_reels_scraper_run_at = datetime.now()
    next_poster_run_at = datetime.now()
    next_remover_run_at = datetime.now()
    next_youtube_run_at = datetime.now()

    if config.IS_ENABLED_REELS_SCRAPER == "1" or config.IS_ENABLED_AUTO_POSTER == "1" :
        # Instagram login client is here
        api = auth.login()
    shorts.main()    
    poster.main(api)
    
    remover.main()
    # shorts.main()
    
   
