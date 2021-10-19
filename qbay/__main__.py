from qbay import app
from qbay import *
from qbay.models import *
from qbay.controllers import *
"""
This file runs the server at a given port
"""

FLASK_PORT = 8081

if __name__ == "__main__":
    app.run(debug=True, port=FLASK_PORT)