import pytest
from mymodule import Transform

class TestTransform:
    @pytest.fixture
    def transform(self):
        return Transform()

    def test_set_slug_with_value(self, transform):
        element = {'tag': 'value'}
        assert transform.set_slug(element, 'tag') == 'value'

    def test_set_slug_with_none(self, transform):
        element = {}
        assert transform.set_slug(element, 'tag') == 'Null'

    def test_set_difficulty_level_with_value(self, transform):
        element = {'tag': 'value'}
        assert transform.set_difficulty_level(element, 'tag') == 'value'

    def test_set_difficulty_level_with_none(self, transform):
        element = {}
        assert transform.set_difficulty_level(element, 'tag') == 'Null'

    def test_set_program_id_with_multiple_programs(self, transform):
        element = {'programs': [{'id': '1'}, {'id': '2'}, {'id': '3'}]}
        assert transform.set_program_id(element, 'programs', 'id') == '1;2;3'

    def test_set_program_id_with_single_program(self, transform):
        element = {'programs': [{'id': '1'}]}
        assert transform.set_program_id(element, 'programs', 'id') == '1'

    def test_set_sub_languages_with_multiple_languages(self, transform):
        element = {'languages': ['en', 'es', 'fr']}
        assert transform.set_sub_languages(element, 'languages') == 'en;es;fr'

    def test_set_sub_languages_with_single_language(self, transform):
        element = {'languages': ['en']}
        assert transform.set_sub_languages(element, 'languages') == 'en'

    def test_set_partners_with_multiple_partners(self, transform):
        element = {'partners': [{'name': 'Partner 1'}, {'name': 'Partner 2'}, {'name': 'Partner 3'}]}
        assert transform.set_partners(element, 'partners', 'name') == 'Partner 1;Partner 2;Partner 3'

    def test_set_partners_with_single_partner(self, transform):
        element = {'partners': [{'name': 'Partner 1'}]}
        assert transform.set_partners(element, 'partners', 'name') == 'Partner 1'

    def test_set_courses_ids(self, transform):
        element = {'extraMetadata': {'definition': {'courseIds': [{'contentId': 'course1'}, {'contentId': 'course2'}]}}}
        assert transform.set_courses_ids(element) == 'course1;course2'

    def test_set_estimated_learning_time_with_value(self, transform):
        element = {'extraMetadata': {'definition': {'estimatedLearningTime': 10}}}
        assert transform.set_estimated_learning_time(element) == '10'

    def test_set_estimated_learning_time_with_none(self, transform):
        element = {'extraMetadata': {'definition': {}}}
        assert transform.set_estimated_learning_time(element) == 'Null'

    def test_set_skills_with_value(self, transform):
        element = {'extraMetadata': {'definition': {'skills': [{'skillName': 'Skill 1'}, {'skillName': 'Skill 2'}]}}}
        assert transform.set_skills(element) == 'Skill 1;Skill 2'

    def test_set_skills_with_none(self, transform):
        element = {'extraMetadata': {'definition': {}}}
        assert transform.set_skills(element) == 'Null'
