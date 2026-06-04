def _key_changes(first_data, second_data, key):
    result = {}
    first_value = first_data.get(key)
    second_value = second_data.get(key)

    if first_value == second_value:
        result['status'] = 'equal'
        result['old_value'] = first_value
    elif isinstance(first_value, dict) and isinstance(second_value, dict):
        result['status'] = 'nested'
        result['children'] = build_diff_tree(first_value, second_value)
    elif key in first_data and key in second_data:
        result['status'] = 'updated'
        result['old_value'] = first_value
        result['new_value'] = second_value
    elif key in first_data:
        result['status'] = 'removed'
        result['old_value'] = first_value
    elif key in second_data:
        result['status'] = 'added'
        result['new_value'] = second_value
    return result


def build_diff_tree(first_data, second_data):
    keys = sorted(first_data.keys() | second_data.keys())
    diff = []
    for key in keys:
        node = {'key': key}
        node.update(_key_changes(first_data, second_data, key))
        diff.append(node)
    return diff
