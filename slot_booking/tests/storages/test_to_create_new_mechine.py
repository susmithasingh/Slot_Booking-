import pytest
from unittest.mock import create_autospec

from slot_booking.interactors.storages.add_washing_mechine_storage_interface import \
    AddNewWashingMechineStorageInterface

from slot_booking.interactors.add_washing_mechine_interactor import \
    AddNewWashingMechineInteractor


def test_to_craete_new_mechinewith_valid_mechine_id():
    washing_mechine_id = 1

    storage = create_autospec(AddNewWashingMechineStorageInterface)
    storage.create_new_washing_mechine.return_value = washing_mechine_id

    interactors = AddNewWashingMechineInteractor(
        storage=storage

    )

    # act
    mechine_id = interactors.create_new_washing_mechine(washing_mechine_id=washing_mechine_id)

    assert mechine_id == washing_mechine_id