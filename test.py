
import env
import praw
import os
import ssl
from moviepy.editor import  *

ssl._create_default_https_context = ssl._create_unverified_context

from praw.models.listing.generator import ListingGenerator
# import Submission from praw



os.system('rm -rf videos')
reddit = praw.Reddit(client_id=env.CLIENT_ID,
                     client_secret=env.CLIENT_SECRET,
                     user_agent=env.USER_AGENT,
                     username=env.USERNAME,
                     password=env.PASSWORD)

subreddit = reddit.subreddit('tiktokthots')
# subreddit.top(limit=10)
posts: ListingGenerator = subreddit.hot(limit=20)
videos = []

for p in posts:
    try:
        link = p.media['reddit_video']['fallback_url']
        link = link.replace('?source=fallback', '')
        title = p.title
        title = '-'.join([tt for tt in title.split(' ') if tt != ' '])
        print(title)
        os.system(f'yt-dlp -o "videos/{title}-#shorts.mp4"  {link}')
        
        # clip1 = VideoFileClip(f'videos/{title}.mp4')
        # follow = VideoFileClip('follow.mp4')
        # result = concatenate_videoclips([clip1, follow])
        # result.write_videofile(f'videos/{title}-#shorts.mp4')
        
        # # function to merge two videos using ffmpeg
        # # os.system(f"echo file 'videos/{title}.mp4' >> current.txt")
        # # os.system("echo file 'follow.mp4' >> current.txt")
        # # os.system(f'ffmpeg -f concat -safe 0 -i current.txt -c:v copy -vsync 0  videos/{title}-#shorts.mp4')
        # # os.system(f'ffmpeg -i "concat:videos/{title}.mp4|follow.mp4" -c:v copy -c:a copy  -codec copy {title}-ready.mp4')
        # os.system(f'rm videos/{title}.mp4')
        videos.append(link)
    except Exception:
        continue


print("DONE")
import sel
sel.upload(wait=300)
