"""
Main entry point for the application.

This script initializes and starts both backend and frontend services.
"""
import subprocess


def init_db():


if __name__ == "__main__":
    init_db()
    print("Database initialized!")

    backend_logger.info("Starting FastAPI server on 8000...")
    fastapi_process =  subprocess.Popen(["uvicorn", "BackEnd.FastAPI:app", "--host", "0.0.0.0", "--port", "8000"])


    frontend_logger.info("Starting Streamlit on port 8501...")
    streamlit_process = subprocess.Popen(["streamlit", "run", "FrontEnd/StreamlitApp.py", "--server.port=8501"])

    input("Press Enter to stop...\n")
    backend_logger.info("Shutting down servers.")
    frontend_logger.info("Terminating services...")
