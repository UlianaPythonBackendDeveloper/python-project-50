import os

import pytest

from gendiff import generate_diff

TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), 'test_data')


def get_test_data_path(file_name):
    return os.path.join(TEST_DATA_DIR, file_name)


@pytest.mark.parametrize(
    'file1, file2',
    [
        ('file1.json', 'file2.json'),
        ('file1.yml', 'file2.yml'),
        ('file1.yaml', 'file2.yml'),
    ],
)
def test_flat_files_stylish(file1, file2):
    path1 = get_test_data_path(file1)
    path2 = get_test_data_path(file2)
    expected_path = get_test_data_path('expected_stylish.txt')

    result = generate_diff(path1, path2)
    with open(expected_path) as expected_file:
        expected = expected_file.read().rstrip('\n')

    assert result == expected
