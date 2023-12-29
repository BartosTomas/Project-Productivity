from Google import Create_Service
from googleapiclient.http import MediaFileUpload
from googleapiclient.http import MediaIoBaseDownload
from quickstart import main
import os
import io

class API:
    def __init__(self):
        main()
        CLIENT_SECRET_FILE = "credentials.json"
        API_NAME = "drive"
        API_VERSION = "v3"
        SCOPES = ["https://www.googleapis.com/auth/drive"]

        self.service = Create_Service(CLIENT_SECRET_FILE, API_NAME,  API_VERSION,  SCOPES)
    
    def Create_file(self):
        file_list = self.service.files().list(q = "mimeType='text/x-python'", spaces = "drive", fields = 'nextPageToken, files(id, name)').execute() 
        if file_list["files"] != []:
            for file in file_list:
                self.Delete_file()
        file_name = "data.py"
        mime_type = "text/x-python"
        file_metadata = {
            "name" : file_name
        }
        media = MediaFileUpload("data.py", mimetype=mime_type)
        self.service.files().create(
            body = file_metadata,
            media_body = media,
            fields = "id"
        ).execute()
    
    def Delete_file(self):
        file_list = self.service.files().list(q = "mimeType='text/x-python'",
                                              spaces = "drive",
                                              fields = 'nextPageToken, files(id, name)').execute()
        items = file_list.get("files", [])
        self.service.files().delete(fileId = items[0]["id"]).execute()
    
    def Request_Data(self):
        file_list = self.service.files().list(q = "mimeType = 'text/x-python'",
                                              spaces = "drive",
                                              fields = "nextPageToken, files(id, name)").execute()
        items = file_list.get("files", [])
        file_id = items[0]["id"]
        file_name = "data.py"

        request = self.service.files().get_media(fileId = file_id)
        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fd = fh, request = request)

        done = False

        while not done:
            status, done = downloader.next_chunk()

        fh.seek(0)

        with open(os.path.join(os.getcwd(), file_name), "wb") as f:
            f.write(fh.read())
            f.close()

            
if __name__ == "__main__":
   API().Request_Data()
