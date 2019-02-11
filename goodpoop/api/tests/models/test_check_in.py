import pytest
from django.db.utils import IntegrityError
from goodpoop.api.tests.factories import CheckInFactory


class TestCheckIn:
    class TestRestroomField:
        def test_cant_be_null(self, db):
            with pytest.raises(IntegrityError) as excinfo:
                CheckInFactory(restroom=None).save()

    class TestAccountField:
        def test_cant_be_null(self, db):
            with pytest.raises(IntegrityError) as excinfo:
                CheckInFactory(account=None).save()
