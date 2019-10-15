import sys
from pathlib import Path

source_dir = "{{cookiecutter.project_slug}}"
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / source_dir))
