import pytest
from django.db.utils import IntegrityError
from goodpoop.api.tests.factories import RestroomFactory


class TestRestroom:
    class TestNameField:
        def test_cant_be_null(self, db):
            with pytest.raises(IntegrityError) as excinfo:
                RestroomFactory(name=None).save()

    class TestLatitudeField:
        def test_cant_be_null(self, db):
            with pytest.raises(IntegrityError) as excinfo:
                RestroomFactory(latitude=None).save()

    class TestLongitudeField:
        def test_cant_be_null(self, db):
            with pytest.raises(IntegrityError) as excinfo:
                RestroomFactory(longitude=None).save()
