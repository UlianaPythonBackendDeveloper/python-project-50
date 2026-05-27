import os

from gendiff import generate_diff

TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), 'test_data')


def get_test_data_path(file_name):
    return os.path.join(TEST_DATA_DIR, file_name)


def test_flat_json_stylish():
    file1 = get_test_data_path('file1.json')
    file2 = get_test_data_path('file2.json')
    expected_path = get_test_data_path('expected_stylish.txt')

    result = generate_diff(file1, file2)
    with open(expected_path) as expected_file:
        expected = expected_file.read().rstrip('\n')

    assert result == expected
