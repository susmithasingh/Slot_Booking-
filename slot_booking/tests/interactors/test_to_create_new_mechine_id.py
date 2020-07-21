import pytest
from unittest.mock import create_autospec
from slot_booking.interactors.presenters.add_washing_mechine_presenter_interface import AddNewWashingMechinePresenterInterface
from slot_booking.interactors.storages.add_washing_mechine_storage_interface import AddNewWashingMechineStorageInterface

from slot_booking.exceptions.exceptions import InvalidWashingMechineId
from slot_booking.interactors.add_washing_mechine_interactor import \
    AddNewWashingMechineInteractor

class Invalid(Exception):
    pass

def test_to_check_mechine_id_with_invalid_mechine_id_raise_error_exception():

    # arrange
    washing_mechine_id = 0

    presenter = create_autospec(AddNewWashingMechinePresenterInterface)
    storage = create_autospec(AddNewWashingMechineStorageInterface)
    storage.validate_new_mechine_id.side_effect = InvalidWashingMechineId
    presenter.raise_invalid_Washing_mechine_id_exception.side_effect = Invalid

    interactors = AddNewWashingMechineInteractor(
        storage=storage

    )

    # act
    with pytest.raises(Invalid) as err:

        interactors.create_new_washing_mechine_wrapper(washing_mechine_id=washing_mechine_id, presenter=presenter)

    # assert
    storage.validate_new_mechine_id.assert_called_once_with(washing_mechine_id=washing_mechine_id)
    presenter.raise_invalid_Washing_mechine_id_exception.assert_called_with()

def test_to_create_new_mechine_with_valid_mechine_id():

    # arrange
    washing_mechine_id = 1

    presenter = create_autospec(AddNewWashingMechinePresenterInterface)
    storage = create_autospec(AddNewWashingMechineStorageInterface)
    storage.validate_new_mechine_id.return_value = True
    storage.create_new_washing_mechine.return_value = washing_mechine_id

    interactors = AddNewWashingMechineInteractor(
        storage=storage

    )

    # act
    mechine_id = interactors.create_new_washing_mechine(washing_mechine_id=washing_mechine_id)

    assert mechine_id == washing_mechine_id