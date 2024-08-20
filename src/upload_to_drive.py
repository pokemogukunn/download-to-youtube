from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2 import service_account
import os

def upload_to_drive(file_path, folder_id):
    SCOPES = ['https://www.googleapis.com/auth/drive.file']
    SERVICE_ACCOUNT_FILE = 'path/to/service_account.json'  # 実際のサービスアカウントJSONファイルのパスに置き換えてください

    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    service = build('drive', 'v3', credentials=credentials)

    file_metadata = {'name': os.path.basename(file_path), 'parents': [folder_id]}
    media = MediaFileUpload(file_path)

    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    print(f"Uploaded File ID: {file.get('id')}")

if __name__ == "__main__":
    folder_id = 'YOUR_DRIVE_FOLDER_ID'  # 実際のGoogle DriveフォルダIDに置き換えてください
    for file_name in os.listdir('data/downloads'):
        file_path = os.path.join('data/downloads', file_name)
        upload_to_drive(file_path, folder_id)
