from Google import Create_Service
from googleapiclient.http import MediaFileUpload
import os

class API:
    def __init__(self):
        CLIENT_SECRET_FILE = "credentials.json"
        API_NAME = "drive"
        API_VERSION = "v3"
        SCOPES = ["https://www.googleapis.com/auth/drive"]

        self.service = Create_Service(CLIENT_SECRET_FILE, API_NAME,  API_VERSION,  SCOPES)
    
    def Create_file(self):
        folder_id = "19l1-Ikdn9QUEWv_c6SyXnBSjkNKHQVPV"
        file_name = "data.py"
        mime_type = "text/x-python"
        file_metadata = {
            "name" : file_name,
            "parents" : [folder_id]
        }
        media = MediaFileUpload("data.py", mimetype=mime_type)
        self.service.files().create(
            body = file_metadata,
            media_body = media,
            fields = "id"
        ).execute()
    
    def Delete_file(self):
        pass

if __name__ == "__main__":
    API()
