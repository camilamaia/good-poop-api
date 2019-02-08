import pytest
from django.db.utils import IntegrityError
from goodpoop.api.tests.factories import AccountFactory


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
