"""
Logging configuration module.

This module sets up logging for the backend service.
- Defines log levels
- Configures file and console logging
- Ensures all backend modules use a centralized logger

Usage:
    from utils.logger import logger
    logger.info("Logging message")
"""
import logging
import os
