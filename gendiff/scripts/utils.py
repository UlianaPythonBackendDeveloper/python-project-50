NONE_BOOLEAN_MAPPING = {
    True: 'true',
    False: 'false',
    None: 'null',
}


def resolve_none_and_boolean(value):
    if isinstance(value, bool) or value is None:
        return NONE_BOOLEAN_MAPPING[value]
    return value
