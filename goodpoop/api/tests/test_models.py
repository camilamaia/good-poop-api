import pytest
from django.db.utils import IntegrityError
from goodpoop.api.tests.factories import (
    AccountFactory,
    CheckInFactory,
    RestroomFactory,
    ReviewFactory,
)


class TestAccount:
    class TestEmailField:
        def test_must_be_unique(self, db):
            with pytest.raises(IntegrityError) as excinfo:
                AccountFactory(email="ab").save()
                AccountFactory(email="ab").save()

        def test_cant_be_null(self, db):
            with pytest.raises(IntegrityError) as excinfo:
                AccountFactory(email=None).save()

    class TestPasswordField:
        def test_cant_be_null(self, db):
            with pytest.raises(IntegrityError) as excinfo:
                AccountFactory(password=None).save()

    class TestNameField:
        def test_cant_be_null(self, db):
            with pytest.raises(IntegrityError) as excinfo:
                AccountFactory(name=None).save()


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


class TestCheckIn:
    class TestRestroomField:
        def test_cant_be_null(self, db):
            with pytest.raises(IntegrityError) as excinfo:
                CheckInFactory(restroom=None).save()

    class TestAccountField:
        def test_cant_be_null(self, db):
            with pytest.raises(IntegrityError) as excinfo:
                CheckInFactory(account=None).save()


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
