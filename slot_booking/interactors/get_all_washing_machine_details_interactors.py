from slot_booking.interactors.presenters.get_washing_mechine_details_presenter_interface import GetWashingMachineDetailsPresenterInterface

class GetWashingMachineDetailsInteractor():

    def __init__(self, presenter: GetWashingMachineDetailsPresenterInterface):
        self.presenter = presenter

    def get_washing_machine_details(self):

        data = self.presenter.get_all_washing_machines_details_response()
        return {
                "all_washing_machine_details": data
        }