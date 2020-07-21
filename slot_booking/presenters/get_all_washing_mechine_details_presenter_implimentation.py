from slot_booking.interactors.presenters.get_washing_mechine_details_presenter_interface import \
    GetWashingMachineDetailsPresenterInterface

from slot_booking.models import WashingMechine


class GetWashingMachineDetailsPresenterImplementation(GetWashingMachineDetailsPresenterInterface):

    def get_all_washing_machines_details_response(self):

        list_of_machine_details = WashingMechine.objects.all()
        all_machine_details = []
        for data in list_of_machine_details:
            all_washing_machine_details = {}
            all_washing_machine_details["washing_machine_id"] = data.washing_machine_id
            all_washing_machine_details["is_active"] = data.is_active
            all_machine_details.append(all_washing_machine_details)
        return all_machine_details
