try:
    from flask_cors import CORS
    print("flask_cors imported successfully")
except ImportError:
    print("flask_cors import failed")
