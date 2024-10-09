import sys
import os

# Get the parent directory of the current file (which is the 'test' folder)
# Then go one directory up to reach the root project directory
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Add the root directory to sys.path
sys.path.insert(0, root_dir)
