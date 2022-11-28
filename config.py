import os

class Config(object):
    
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5925907225:AAEoUGKGF4fkK9hzxi65wnNtK1Gap29uz_o")
    
    API_ID = int(os.environ.get("API_ID", "3199060"))
    
    API_HASH = os.environ.get("API_HASH", "d67f6b73f3df9f90554442255c846f79")
    
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    
    MAX_FILE_SIZE = 50000000

    TG_MAX_FILE_SIZE = 2097152000

    FREE_USER_MAX_FILE_SIZE = 50000000
    
    CHUNK_SIZE = int(128)

    HTTP_PROXY = ""
    
    MAX_MESSAGE_LENGTH = 4096
    
    PROCESS_MAX_TIMEOUT = 3600
    
    OWNER_ID = int(os.environ.get("OWNER_ID", ""))

    SESSION_NAME = "UploadLinkToFileBot"
    
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://qashidevil:Ayesha.Qasim1@cluster0.yh7psjw.mongodb.net/?retryWrites=true&w=majority")

    MAX_RESULTS = "50"
