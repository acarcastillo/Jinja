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

    def mock_get(*args, **kwargs):
        return MockResponse(200, {"programs": []})

    monkeypatch.setattr(requests, 'get', mock_get)
    
    return CourseraData()

def test_get_programs(coursera_data):
    # Calling the method under test
    result = coursera_data.get_programs("0")

    # Assertions
    assert requests.get.called_once_with(
        "https://api.coursera.org/api/businesses.v1/eb9rVSdASBGpRxlxirYAnQ/programs?start=0&limit=1000",
        headers={"Authorization": "Bearer <access_token>"}
    )
    assert result.status_code == 200
    assert result.json() == {"programs": []}

def test_get_programs_exception(coursera_data, monkeypatch):
    # Mocking an exception raised by requests.get
    def mock_get_exception(*args, **kwargs):
        raise requests.exceptions.RequestException()

    monkeypatch.setattr(requests, 'get', mock_get_exception)

    # Calling the method under test
    result = coursera_data.get_programs("0")

    # Assertions
    assert result is None
