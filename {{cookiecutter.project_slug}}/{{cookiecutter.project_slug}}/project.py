import logging
import logging.config
from pathlib import Path

import yaml


class Coordinator:
    def __init__(self, log_file_name="log.txt"):
        self.path_project_root = Path(__file__).resolve().parents[1]
        self.path_log = self.path_project_root / "log"
        self.path_config = self.path_project_root / "config"

        with open(self.path_config / "logging_config.yml", "r") as f:
            config = yaml.safe_load(f.read())
            log_file = self.path_log / log_file_name
            config["handlers"]["file"]["filename"] = log_file

            logging.config.dictConfig(config)
            self.logger = logging.getLogger("root")
