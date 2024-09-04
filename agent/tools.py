from typing import Union, Dict
from crewai_tools import BaseTool
import os
import requests
from youtube_transcript_api import YouTubeTranscriptApi
from utils import _get_ares_api_key, _get_ares_api_url, _get_youtube_api_key, _get_youtube_api_url

class YoutubeSearchTool(BaseTool):
    name: str = "YoutubeV3API"
    description: str = "YouTube API for Real-Time Video Caption Searching"
    
    def _run(self, query: Union[Dict, str]) -> dict:
        if type(query) == dict:
            for key in query.keys():
                if type(query[key]) == str:
                    query = query[key]
                    break
        try:
            response = requests.get(
                url=_get_youtube_api_url(),
                params={
                    "q": query,
                    "type": "video",
                    "videoCaption": "closedCaption",
                    "key": _get_youtube_api_key()
                }
            )
        except Exception as e:
            print(f"Error fetching resources from YouTube: {e}")
            return []
        
        if response.status_code != 200:
            return []
        response = response.json()
        results = []
        for item in response["items"]:
            try:
                content = YouTubeTranscriptApi.get_transcript(item['id']['videoId'])
                raw_text = [part["text"] for part in content]
                raw_text = " ".join(raw_text)
                results.append(raw_text)
            except Exception as e:
                print(f"\nError transcibing youtube video {item['id']['videoId']} | {e}")
            
        return results
    
    
class AresRealTimeSearch(BaseTool):
    name: str = "Ares"
    description: str = "API for Real-Time Internet Search"
    
    def _run(self, query: Union[Dict, str]) -> dict:
        if type(query) == dict:
            for key in query.keys():
                if type(query[key]) == str:
                    query = query[key]
                    break
        payload = { "query": [query] }
        headers = {
            "x-api-key": _get_ares_api_key(),
            "content-type": "application/json"
        }
        response = requests.post(_get_ares_api_url(), json=payload, headers=headers)
        if response.status_code != 200:
            return {}
        response = response.json()
        return response["data"]