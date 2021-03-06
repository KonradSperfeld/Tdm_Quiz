import json
import logging
import os


logger = logging.getLogger(__name__)


def get_config(config_path):
    if os.path.isfile(config_path):
        try:
            with open(config_path, "r") as fp:
                config_dict = json.load(fp)
                config_dict["config_path"] = config_path
                return config_dict
        except:
            logger.warning("Could not get config from the exiting file. Is it a corrupt json-file?")
    elif os.path.isdir(config_path):
        raise IOError(f"The path: {config_path} must not be a directory!")
    else:
        return {"config_path":config_path}


def set_config(config_dict, allow_new=False):
    if allow_new:
        assert os.path.isdir(
            os.path.dirname(config_dict["config_path"])
        ), f"Incorrect config_path, parent dir does not exist: {config_dict}"
    else:
        assert os.path.isfile(
            config_dict["config_path"]
        ), f"No config in path: {config_dict}, make a new config is not allowed in this option"
    with open(config_dict["config_path"], "w") as fp:
        json.dump(config_dict, fp, indent=2)
    return 0
