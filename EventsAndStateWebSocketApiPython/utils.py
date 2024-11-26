# utils.py
"""
Utility functions for cross-platform compatibility
"""
import os
import platform

def clear_screen():
    """Clear the console screen in a cross-platform way"""
    if platform.system().lower() == "windows":
        os.system('cls')
    else:
        os.system('clear')
