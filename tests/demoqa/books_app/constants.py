import os

USER = os.environ.get("BOOK_APP_USER")
PASSWORD = os.environ.get("BOOK_APP_PASSWORD")
HOST = "https://demoqa.com"

CAPABILITIES = [
    {"browserName": "chrome"},
    {"browserName": "firefox",
     "acceptInsecureCerts": True,
     "moz:debuggerAddress": True},
]
