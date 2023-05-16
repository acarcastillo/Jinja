import pytest
import requests
from mymodule import CourseraData

@pytest.fixture
def coursera_data(monkeypatch):
    # Mocking the response from requests.get
    class MockResponse:
        def __init__(self, status_code, json_data):
            self.status_code = status_code
            self.json_data = json_data

        def json(self):
            return self.json_data

    def mock_get_programs(start):
        if start == '0':
            return MockResponse(200, {
                "paging": {
                    "next": "1"
                },
                "elements": [
                    {"id": 1, "name": "Program 1"},
                    {"id": 2, "name": "Program 2"}
                ]
            })
        elif start == '1':
            return MockResponse(200, {
                "paging": {},
                "elements": [
                    {"id": 3, "name": "Program 3"}
                ]
            })

    monkeypatch.setattr(requests, 'get', mock_get_programs)

    return CourseraData()

def test_get_program_list(coursera_data):
    # Calling the method under test
    result = coursera_data.get_program_list()

    # Assertions
    assert len(result) == 3
    assert result[0] == {"id": 1, "name": "Program 1"}
    assert result[1] == {"id": 2, "name": "Program 2"}
    assert result[2] == {"id": 3, "name": "Program 3"}
