import os
import json


class IOService:

    @staticmethod
    def read_input_from_file(input_file_path):
        """
        :param input_file_path: Input file path from which we need to extract the data
        :return: List of customer objects containing the customer_data
        Format: [{"latitude": "52.986375", "user_id": 12, "name": "Christina McArdle", "longitude": "-6.043701"}]
        """

        # checking if the input file exists or not
        if not os.path.exists(input_file_path):
            print(
                "Looks like you forgot to add the customers.txt file."
                "Make sure to add the desired JSON in the customers.txt file "
                "in the root directory inside the root /Intercom folder."
            )
            exit(0)

        # checking if the input file is empty or not
        if os.stat(input_file_path).st_size == 0:
            print("Oops... Looks like your customers.txt file is empty.")
            exit(0)

        customer_list = []
        with open(input_file_path) as customer_data:
            for line in customer_data:
                try:
                    customer_list.append(json.loads(line))
                except ValueError:
                    print("Oops... Looks like your JSON Format is broken :O")
                    print("Broken line -> {} ".format(line))

        return customer_list

    @staticmethod
    def write_output_to_file(customer_list, output_file_path):
        output_file = open(output_file_path, 'w')
        for customer in customer_list:
            # Writing only the user_id and the name of the customer as mentioned in the activity doc
            try:
                customer_details = {'user_id': customer['user_id'], 'name': customer['name']}
            except KeyError:
                print('Uh Oh! Looks like the user_id key for this customer is missing')
            except ValueError:
                print('Uh Oh! Looks like the user_id value for this customer is missing')
            else:
                output_file.write(json.dumps(customer_details) + "\n")

        output_file.close()
