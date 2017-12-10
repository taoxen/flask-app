# Run a test server.
from app import app

app.run(host='192.168.0.204', port=5000, debug=True)
