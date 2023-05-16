import pytest
from mymodule import format_data

def test_format_data():
    # Test case 1: Valid row with contentIds
    row1 = {
        'name': 'Program 1',
        'tagline': 'Tagline 1',
        'id': '123',
        'url': 'https://www.example.com/program1',
        'contentIds': [{'contentId': 'content1'}, {'contentId': 'content2'}, {'contentId': 'content3'}]
    }
    expected1 = {
        'learningProvider': 'Coursera',
        'programName': 'Program 1',
        'tagline': 'Tagline 1',
        'id': '123',
        'url': 'https://www.example.com/program1',
        'contentIDs': 'content1;content2;content3'
    }
    assert format_data(row1) == expected1

    # Test case 2: Valid row without contentIds
    row2 = {
        'name': 'Program 2',
        'tagline': 'Tagline 2',
        'id': '456',
        'url': 'https://www.example.com/program2',
        'contentIds': []
    }
    expected2 = {
        'learningProvider': 'Coursera',
        'programName': 'Program 2',
        'tagline': 'Tagline 2',
        'id': '456',
        'url': 'https://www.example.com/program2',
        'contentIDs': ''
    }
    assert format_data(row2) == expected2

    # Test case 3: Empty row
    row3 = {}
    expected3 = {
        'learningProvider': 'Coursera',
        'programName': None,
        'tagline': None,
        'id': None,
        'url': None,
        'contentIDs': ''
    }
    assert format_data(row3) == expected3
