class Submarine:
    def __init__(self):
        self._oxygen_generator_rate = 0
        self._CO2_scrubber_rate = 0
        self._gamma_rate = 0
        self._epsilon_rate = 0

    def get_oxigen_generator_rate(self):
        return self._oxygen_generator_rate

    def get_CO2_scrubber_rate(self):
        return self._CO2_scrubber_rate

    def get_power_consumption(self):
        return self._gamma_rate * self._epsilon_rate

    def get_life_support_rating(self):
        return self._CO2_scrubber_rate * self._oxygen_generator_rate

    def set_rates_from_input(self, input_list):
        gamma = ''
        epsilon = ''
        for digit in range(len(input_list[0])):
            most_common = self._get_most_common(digit, input_list)
            if '0' == most_common:
                gamma += '0'
                epsilon += '1'
            else:
                epsilon += '0'
                gamma += '1'

        self._gamma_rate = int(gamma, base=2)
        self._epsilon_rate = int(epsilon, base=2)

    def _get_most_common(self, index: int, input: list) -> str:
        zeros = 0
        for number in input:
            if number[index] == '0':
                zeros += 1
        return '0' if zeros > len(input) - zeros else '1'

    def set_oxygen_generator_rating(self, input_list):
        for digit in range(len(input_list[0])):
            most_common = self._get_most_common(digit, input_list)
            input_list = list(filter(lambda x: x[digit] == most_common, input_list))
            if len(input_list) == 1:
                self._oxygen_generator_rate = int(input_list.pop(), base=2)
                break

    def set_CO2_scrubber_rating(self, input_list):
        for digit in range(len(input_list[0])):
            most_common = self._get_most_common(digit, input_list)
            input_list = list(filter(lambda x: x[digit] != most_common, input_list))
            if len(input_list) == 1:
                self._CO2_scrubber_rate = int(input_list.pop(), base=2)
                break


def process_input(filename: str, obj: Submarine):
    def file_to_list(input: str) -> list:
        return input.split('\n')

    with open(filename, 'r') as file:
        input_list = file_to_list(file.read())
        obj.set_rates_from_input(input_list)
        obj.set_CO2_scrubber_rating(input_list)
        obj.set_oxygen_generator_rating(input_list)


if __name__ == '__main__':
    submarine = Submarine()
    process_input('input.txt', submarine)
    print(f'Power Consumption: {submarine.get_power_consumption()}')
    print(f'Life support rate: {submarine.get_life_support_rating()}')
