import json
import os
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

DATA_FILE = "todos.json"

def load():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE) as f:
        return json.load(f)

def save(todos):
    with open(DATA_FILE, "w") as f:
        json.dump(todos, f, indent=2)

class Handler(BaseHTTPRequestHandler):
    def log_message(self, *args):
        pass

    def send_json(self, data, status=200):
        body = json.dumps(data).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path == "/":
            with open("index.html", "rb") as f:
                content = f.read()
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(content)
        elif parsed.path == "/todos":
            self.send_json(load())
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        body = json.loads(self.rfile.read(length)) if length else {}
        todos = load()

        if self.path == "/add":
            text = body.get("task", "").strip()
            if text:
                todos.append({"id": len(todos) + 1, "task": text, "done": False})
                save(todos)
            self.send_json(todos)

        elif self.path == "/done":
            for t in todos:
                if t["id"] == body.get("id"):
                    t["done"] = not t["done"]
            save(todos)
            self.send_json(todos)

        elif self.path == "/delete":
            todos = [t for t in todos if t["id"] != body.get("id")]
            save(todos)
            self.send_json(todos)

        else:
            self.send_response(404)
            self.end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8080), Handler)
    print("Server running at http://localhost:8080")
    server.serve_forever()
