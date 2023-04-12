from .base import *
import os
from dotenv import load_dotenv

load_dotenv()

if os.getenv("PRODUCTION") == 'true':
    print("prod basladi")
    from .production import *
else:
    from .development import *
