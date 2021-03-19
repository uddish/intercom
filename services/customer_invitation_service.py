from math import sin, cos, radians, acos
from constants import INTERCOM_DUBLIN_LATITUDE, INTERCOM_DUBLIN_LONGITUDE, RADIUS_OF_EARTH, \
    MINIMUM_ALLOWED_DISTANCE_FOR_INVITATION


class CustomerInvitationService:

    @staticmethod
    def get_matching_customers(customer_list: list):
        """
        :param customer_list: List of customer objects on which we need to check the distance
        :return: List of customers sorted by their user_id
        """
        customers_to_be_invited = []

        for customer in customer_list:
            # Converting the latitude and longitude into a float value so that it can be converted into radians later
            try:
                customer_latitude, customer_longitude = float(customer['latitude']), float(customer['longitude'])
            except KeyError:
                print("Uh Oh! Looks like your customer did not have a latitude or longitude field/key")
                print(customer)
            except ValueError:
                print("Uh Oh! Looks like your customer did not have a latitude or longitude value")
                print(customer)
            else:
                customer_distance = CustomerInvitationService.calculate_distance_from_destination(
                    customer_latitude, customer_longitude
                )
                # Checking if the customer is within the allowed distance from the destination.
                # Also checking if a duplicate entry exists in the output list.
                if CustomerInvitationService.should_invite_customer(customer_distance) \
                        and customer not in customers_to_be_invited:
                    customers_to_be_invited.append(customer)

        customers_sorted_by_id = sorted(customers_to_be_invited, key=lambda item: item['user_id'])
        return customers_sorted_by_id

    @staticmethod
    def calculate_distance_from_destination(
            customer_latitude: float,
            customer_longitude: float,
            destination_latitude: float = INTERCOM_DUBLIN_LATITUDE,
            destination_longitude: float = INTERCOM_DUBLIN_LONGITUDE
    ):
        """
        :param customer_latitude: latitude of the customer for which we want to check if he/she should be invited
        :param customer_longitude: longitude of the customer for which we want to check if he/she should be invited
        :param destination_latitude: latitude of the destination from where we want to calculate the distance
        :param destination_longitude: longitude of the destination from where we want to calculate the distance
        :return: distance between the customer and the destination in kilometers
        """
        customer_latitude_in_radians = radians(customer_latitude)
        customer_longitude_in_radians = radians(customer_longitude)

        destination_latitude_in_radians = radians(destination_latitude)
        destination_longitude_in_radians = radians(destination_longitude)

        latitude_difference = destination_longitude_in_radians - customer_longitude_in_radians

        central_angle = acos(
            sin(destination_latitude_in_radians) * sin(customer_latitude_in_radians) +
            (cos(destination_latitude_in_radians) * cos(customer_latitude_in_radians) * cos(latitude_difference))
        )

        distance = RADIUS_OF_EARTH * central_angle
        return distance

    @staticmethod
    def should_invite_customer(distance_from_destination: float):
        """
        :param distance_from_destination:
        :return: True/False depending on if the particular user lies within the defined minimum distance
        """
        return distance_from_destination < MINIMUM_ALLOWED_DISTANCE_FOR_INVITATION
