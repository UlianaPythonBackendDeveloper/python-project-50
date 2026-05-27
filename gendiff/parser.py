import json


def parse(stream, extension):
    if extension == '.json':
        return json.load(stream)
    raise ValueError(f'Unsupported format: {extension}')
