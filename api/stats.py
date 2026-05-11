from pymongo import MongoClient
from http.server import BaseHTTPRequestHandler
import json, os

MONGO_URI = "mongodb+srv://amorbot:Amor@2025bot@cluster0.lrx0iil.mongodb.net/?appName=Cluster0"

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
