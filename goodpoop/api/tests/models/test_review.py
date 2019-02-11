import pytest
from django.db.utils import IntegrityError
from goodpoop.api.tests.factories import ReviewFactory


class TestReview:
    class TestRestroomField:
        def test_cant_be_null(self, db):
            with pytest.raises(IntegrityError) as excinfo:
                ReviewFactory(restroom=None).save()

    class TestCategoryField:
        def test_cant_be_null(self, db):
            with pytest.raises(IntegrityError) as excinfo:
                ReviewFactory(category=None).save()

        def test_must_be_in_the_possible_choices(self, db):
            with pytest.raises(IntegrityError) as excinfo:
                ReviewFactory(category="Non existent category").save()

    class TestIsFreeField:
        def test_cant_be_null(self, db):
            with pytest.raises(IntegrityError) as excinfo:
                ReviewFactory(is_free=None).save()
