from pymongo import MongoClient
from http.server import BaseHTTPRequestHandler
import json
from urllib.parse import quote_plus

username = quote_plus("amorbot")
password = quote_plus("Amor@2025bot")
MONGO_URI = f"mongodb+srv://{username}:{password}@cluster0.lrx0iil.mongodb.net/?appName=Cluster0"

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            client = MongoClient(MONGO_URI)
            db = client["amor_db"]
            doc = db["stats"].find_one({"_id": "global"})
            data = {
                "servers": doc.get("servers", 0),
                "users": doc.get("users", 0),
                "commands_used": doc.get("commands_used", 0)
            }
            client.close()
        except Exception as e:
            data = {"error": str(e)}

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())
