# UAB - Unity Automated Builder

UAB is a program designed to automate the creation of Unity projects. It can create a game based on a description, download necessary assets, check files for errors, and run tests.

## Features
- Create a new Unity project
- Download photo and audio files
- Add licensing information
- Run tests on the project
- Initialize Git repository
- Generate initial code and scenes
- Setup CI/CD for automatic testing and building

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/UAB.git
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

Update the `config.py` file with your API keys and Unity editor path.

```python
# config.py
UNSPLASH_ACCESS_KEY = "Your Unsplash Access Key"
FREESOUND_ACCESS_KEY = "Your Freesound Access Key"
HUGGINGFACE_ACCESS_KEY = "Your Hugging Face Access Key"
UNITY_EDITOR_PATH = "Path to Unity Editor"
```

## Usage

Run the program:
```bash
python run_program.py
```

## License

This project is licensed under the MIT License.