# !pip install youtube-transcript-api 
from youtube_transcript_api import YouTubeTranscriptApi

text_dicts = YouTubeTranscriptApi.get_transcript("4HTHNf40vT4", languages=["ko"]) # id of video 
transcript = ""
for t in text_dicts:
  transcript += t["text"] + " "

print(transcript)
