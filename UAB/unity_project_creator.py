# -*- coding: utf-8 -*-
import os
import requests
import subprocess
import json
from PyQt5 import QtWidgets, uic, QFileDialog
from config import UNSPLASH_ACCESS_KEY, FREESOUND_ACCESS_KEY, HUGGINGFACE_ACCESS_KEY, UNITY_EDITOR_PATH

class UnityProjectCreator(QtWidgets.QMainWindow):
    def __init__(self):
        super(UnityProjectCreator, self).__init__()
        uic.loadUi('interface/interface.ui', self)
        self.create_project_button.clicked.connect(self.create_project)
        self.browse_button.clicked.connect(self.browse_directory)

    def browse_directory(self):
        directory = QFileDialog.getExistingDirectory(self, "Select Directory")
        self.project_path.setText(directory)

    def create_project(self):
        project_name = self.project_name.text()
        project_path = self.project_path.text()
        description = self.description.toPlainText()

        if not project_name or not project_path or not description:
            self.status.setText("Please fill in all fields.")
            return

        # Create Unity project
        self.status.setText("Creating Unity project...")
        subprocess.call([UNITY_EDITOR_PATH, "-createProject", os.path.join(project_path, project_name)])

        # Setup project for mobile platform
        self.setup_mobile_platform(project_path, project_name)

        # Download assets
        self.status.setText("Downloading assets...")
        self.download_assets(project_path, project_name)

        # Initialize Git repository
        self.init_git_repo(project_path, project_name)

        # Add licensing information
        self.add_licensing_info(project_path, project_name)

        # Generate initial scenes and code
        self.status.setText("Generating initial scenes and code...")
        self.generate_initial_code_and_scenes(project_path, project_name)

        # Setup CI/CD
        self.setup_cicd(project_path, project_name)

        # Run tests
        self.run_tests(project_path, project_name)

        self.status.setText("Project created successfully!")

    def setup_mobile_platform(self, project_path, project_name):
        # Setup Unity project for mobile platform (Android/iOS)
        project_dir = os.path.join(project_path, project_name)
        # Add necessary settings for mobile platform
        # This function needs to be implemented with Unity Editor scripting

    def download_assets(self, project_path, project_name):
        # Download photo from Unsplash
        response = requests.get(f"https://api.unsplash.com/photos/random?client_id={UNSPLASH_ACCESS_KEY}")
        if response.status_code == 200:
            photo_url = response.json()['urls']['regular']
            photo_response = requests.get(photo_url)
            with open(os.path.join(project_path, project_name, 'Assets', 'photo.jpg'), 'wb') as file:
                file.write(photo_response.content)

        # Download audio from Freesound
        response = requests.get(f"https://freesound.org/apiv2/sounds/158847/download/?token={FREESOUND_ACCESS_KEY}")
        if response.status_code == 200:
            audio_url = response.json()['previews']['preview-lq-mp3']
            audio_response = requests.get(audio_url)
            with open(os.path.join(project_path, project_name, 'Assets', 'audio.mp3'), 'wb') as file:
                file.write(audio_response.content)

    def init_git_repo(self, project_path, project_name):
        # Initialize a new Git repository
        project_dir = os.path.join(project_path, project_name)
        subprocess.call(["git", "init", project_dir])
        subprocess.call(["git", "-C", project_dir, "add", "."])
        subprocess.call(["git", "-C", project_dir, "commit", "-m", "Initial commit"])

    def add_licensing_info(self, project_path, project_name):
        license_text = """
        MIT License
        Copyright (c) 2025 SHAMAN-ATTA
        Permission is hereby granted, free of charge, to any person obtaining a copy
        of this software and associated documentation files (the "Software"), to deal
        in the Software without restriction, including without limitation the rights
        to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
        copies of the Software, and to permit persons to whom the Software is
        furnished to do so, subject to the following conditions:
        The above copyright notice and this permission notice shall be included in all
        copies or substantial portions of the Software.
        THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
        IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
        FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
        AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
        LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
        OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
        SOFTWARE.
        """
        with open(os.path.join(project_path, project_name, 'LICENSE'), 'w') as file:
            file.write(license_text)

    def generate_initial_code_and_scenes(self, project_path, project_name):
        # Generate initial code and scenes
        project_dir = os.path.join(project_path, project_name)
        # This function needs to be implemented with Unity Editor scripting

    def setup_cicd(self, project_path, project_name):
        # Setup CI/CD for the project
        project_dir = os.path.join(project_path, project_name)
        # Add necessary settings for CI/CD
        # This function needs to be implemented

    def run_tests(self, project_path, project_name):
        project_dir = os.path.join(project_path, project_name)
        # Run Unity tests using Unity Test Framework
        subprocess.call([UNITY_EDITOR_PATH, "-runTests", "-projectPath", project_dir, "-testResults", os.path.join(project_dir, "TestResults.xml")])

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = UnityProjectCreator()
    window.show()
    app.exec_()