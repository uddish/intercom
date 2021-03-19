from services.customer_invitation_service import CustomerInvitationService
from services.input_output_service import IOService
from constants import INPUT_FILE, OUTPUT_FILE


def execute_intercom_activity():

    # Reading data from the input file
    print('******** Reading from the input file. ********')
    customer_list = IOService.read_input_from_file(INPUT_FILE)
    # Getting the list of customers that needs to be invited
    matching_customers = CustomerInvitationService.get_matching_customers(customer_list)
    # Writing the matched customers to an output file
    IOService.write_output_to_file(matching_customers, OUTPUT_FILE)
    print('******** Customers added to the output file. Please check output.txt in the root /Intercom folder ********')


if __name__ == '__main__':
    execute_intercom_activity()
