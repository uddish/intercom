import unittest
from services.input_output_service import IOService
from services.customer_invitation_service import CustomerInvitationService

test_input = "tests/test_customers.txt"
test_input_with_wrong_format = "tests/test_customers_with_wrong_format.txt"
test_input_with_empty_file = "tests/test_customers_empty.txt"
test_output = "tests/test_output.txt"


class TestInputOutputService(unittest.TestCase):

    def test_read_input_from_missing_file(self):
        with self.assertRaises(SystemExit) as sys_exit:
            IOService.read_input_from_file("random.txt")
        self.assertEqual(sys_exit.exception.code, 0)

    def test_read_input_from_incorrect_file(self):
        customer_list = IOService.read_input_from_file(test_input_with_wrong_format)
        output = [
            {"latitude": "51.92893", "user_id": 1, "name": "Alice Cahill", "longitude": "-10.27699"}
        ]
        self.assertEqual(customer_list, output)

    def test_read_input(self):
        customer_list = IOService.read_input_from_file(test_input)
        output = [
            {"latitude": "52.228056", "user_id": 18, "name": "Bob Larkin", "longitude": "-7.915833"},
            {"latitude": "54.133333", "user_id": 24, "name": "Rose Enright", "longitude": "-6.433333"},
            {"latitude": "55.033", "user_id": 19, "name": "Enid Cahill", "longitude": "-8.112"},
            {"latitude": "53.521111", "user_id": 20, "name": "Enid Enright", "longitude": "-9.831111"},
            {"latitude": "51.802", "user_id": 21, "name": "David Ahearn", "longitude": "-9.442"},
            {"latitude": "54.374208", "user_id": 22, "name": "Charlie McArdle", "longitude": "-8.371639"},
            {"latitude": "53.74452", "user_id": 29, "name": "Oliver Ahearn", "longitude": "-7.11167"},
            {"latitude": "53.761389", "user_id": 30, "name": "Nick Enright", "longitude": "-7.2875"},
            {"latitude": "54.080556", "user_id": 23, "name": "Eoin Gallagher", "longitude": "-6.361944"},
            {"latitude": "52.833502", "user_id": 25, "name": "David Behan", "longitude": "-8.522366"}
        ]
        self.assertEqual(customer_list, output)

    def test_read_input_from_empty_file(self):
        with self.assertRaises(SystemExit) as sys_exit:
            IOService.read_input_from_file(test_input_with_empty_file)
        self.assertEqual(sys_exit.exception.code, 0)

    def test_write_output_to_file(self):
        data = [
            {"latitude": "54.080556", "user_id": 23, "name": "Eoin Gallagher", "longitude": "-6.361944"},
            {"latitude": "54.133333", "user_id": 24, "name": "Rose Enright", "longitude": "-6.433333"},
        ]
        IOService.write_output_to_file(data, test_output)
        customer_data = IOService.read_input_from_file(test_output)

        output_data = [
            {"user_id": 23, "name": "Eoin Gallagher"},
            {"user_id": 24, "name": "Rose Enright"},
        ]

        self.assertEqual(customer_data, output_data)


class TestCustomerInvitationService(unittest.TestCase):

    def test_calculate_distance_from_destination(self):
        user_id_vs_distance = {
            18: 166.44809264261397,
            24: 89.03103382223692,
            19: 223.63496516413727,
            20: 237.57601503986697,
            21: 274.79780021882317,
            22: 180.15527722864547,
            29: 72.20178549699202,
            30: 82.64284999107412,
            23: 82.69492611644121,
            25: 161.36207870697515,
        }

        customer_data = IOService.read_input_from_file(test_input)
        matching_customers = CustomerInvitationService.get_matching_customers(customer_data)
        for customer in matching_customers:
            customer_lat, customer_long = float(customer['latitude']), float(customer['longitude'])
            distance = CustomerInvitationService.calculate_distance_from_destination(customer_lat, customer_long)
            # Rounding the float value since the values calculated can be a little off for different systems
            self.assertEqual(round(distance, 2), round(user_id_vs_distance[customer['user_id']], 2))

    def test_distance_formula_correctness(self):
        # Taking Intercom's London Office coordinates and calculating their distance from Intercom's Ireland office
        # Please use this link to calculate the distance between two coordinate points
        # https://www.geodatasource.com/distance-calculator
        # Please note that the distance calculated from the above website can be a little different from the distance
        # calculated by using our formula

        intercom_london_latitude = 51.571732361751074
        intercom_london_longitude = -0.07964202473350517
        distance = CustomerInvitationService.calculate_distance_from_destination(
            intercom_london_latitude, intercom_london_longitude
        )

        # Rounding the float value since the values calculated can be a little off for different systems
        self.assertEqual(round(distance, 2), round(462.2627320552066, 2))

    def test_get_matching_customers_sorted(self):
        customer_data = IOService.read_input_from_file(test_input)
        matching_customers = CustomerInvitationService.get_matching_customers(customer_data)
        sorted_matching_customers = [
            {'latitude': '54.080556', 'user_id': 23, 'name': 'Eoin Gallagher', 'longitude': '-6.361944'},
            {'latitude': '54.133333', 'user_id': 24, 'name': 'Rose Enright', 'longitude': '-6.433333'},
            {'latitude': '53.74452', 'user_id': 29, 'name': 'Oliver Ahearn', 'longitude': '-7.11167'},
            {'latitude': '53.761389', 'user_id': 30, 'name': 'Nick Enright', 'longitude': '-7.2875'}
        ]

        self.assertEqual(matching_customers, sorted_matching_customers)


if __name__ == '__main__':
    unittest.main()
