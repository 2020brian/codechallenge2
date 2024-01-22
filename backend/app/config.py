# backend/app/config.py

from flask_cors import CORS

class Config:
    # ... (unchanged)

# Add CORS configuration
CORS(app)
