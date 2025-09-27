#!/usr/bin/env python3
"""
Startup script for the Healthcare Chatbot
"""

import subprocess
import sys
import time
import webbrowser
from pathlib import Path

def check_dependencies():
    """Check if required packages are installed"""
    try:
        import flask
        import flask_cors
        import requests
        print("✅ All dependencies are installed")
        return True
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        print("Please run: pip install -r requirements.txt")
        return False

def start_server():
    """Start the Flask server"""
    print("🚀 Starting Healthcare Chatbot server...")
    print("📍 Server will be available at: http://localhost:5000")
    print("🛑 Press Ctrl+C to stop the server")
    print("-" * 50)
    
    try:
        # Start the Flask app
        subprocess.run([sys.executable, "app.py"])
    except KeyboardInterrupt:
        print("\n👋 Server stopped. Goodbye!")
    except Exception as e:
        print(f"❌ Error starting server: {e}")

def main():
    """Main function"""
    print("🏥 Healthcare AI Chatbot")
    print("=" * 30)
    
    if not check_dependencies():
        return
    
    print("\nStarting server in 3 seconds...")
    time.sleep(3)
    
    start_server()

if __name__ == "__main__":
    main()
