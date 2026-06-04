import json

import yaml

YAML_EXTENSIONS = {'.yml', '.yaml'}


def parse(stream, extension):
    if extension == '.json':
        return json.load(stream)
    if extension in YAML_EXTENSIONS:
        return yaml.safe_load(stream)
    raise ValueError(
        'Comparison is available only for json and yaml files'
    )
