import subprocess
import os
from config import UNITY_EDITOR_PATH

def run_tests(project_path, project_name):
    project_dir = os.path.join(project_path, project_name)
    # Run Unity tests using Unity Test Framework
    subprocess.call([UNITY_EDITOR_PATH, "-runTests", "-projectPath", project_dir, "-testResults", os.path.join(project_dir, "TestResults.xml")])