import pytest
from datetime import datetime
from mymodule import format_data

@pytest.fixture
def sample_row():
    return {
        'completedAt': 1621152000000,  # May 17, 2021
        'lastActivityAt': 1621046400000,  # May 16, 2021
        'deletedAt': None,
        'enrolledAt': 1620950400000,  # May 15, 2021
        'grade': 0.85,
        'isCompleted': 'true',
        'overallProgress': 0.75,
        'membershipState': 'active',
        'contentId': 'content123',
        'externalId': 'external123',
        'approxTotalCourseHrs': 10,
        'id': 'row123',
        'contentType': 'lesson',
        'programId': 'program123'
    }

def test_format_data_completedAt(sample_row):
    formatted_row = format_data(sample_row)
    assert formatted_row['completedAt'] == '17-05-2021'

def test_format_data_lastActivityAt(sample_row):
    formatted_row = format_data(sample_row)
    assert formatted_row['lastActivityAt'] == '16-05-2021'

def test_format_data_deletedAt(sample_row):
    formatted_row = format_data(sample_row)
    assert formatted_row['deletedAt'] == 'Null'

def test_format_data_enrolledAt(sample_row):
    formatted_row = format_data(sample_row)
    assert formatted_row['enrolledAt'] == '15-05-2021'

def test_format_data_grade(sample_row):
    formatted_row = format_data(sample_row)
    assert formatted_row['grade'] == 85.0

def test_format_data_isCompleted_true(sample_row):
    formatted_row = format_data(sample_row)
    assert formatted_row['isCompleted'] is True

def test_format_data_isCompleted_false(sample_row):
    sample_row['isCompleted'] = 'false'
    formatted_row = format_data(sample_row)
    assert formatted_row['isCompleted'] is False

def test_format_data_isCompleted_none(sample_row):
    sample_row['isCompleted'] = None
    formatted_row = format_data(sample_row)
    assert formatted_row['isCompleted'] is False

def test_format_data_additional_fields(sample_row):
    formatted_row = format_data(sample_row)
    assert formatted_row['overallProgress'] == 0.75
    assert formatted_row['membershipState'] == 'active'
    assert formatted_row['contentId'] == 'content123'
    assert formatted_row['externalId'] == 'external123'
    assert formatted_row['approxTotalCourseHrs'] == 10
    assert formatted_row['id'] == 'row123'
    assert formatted_row['contentType'] == 'lesson'
    assert formatted_row['programId'] == 'program123'
