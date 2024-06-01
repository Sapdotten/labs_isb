class Luhn:
    '''
    Class for checking Luhn algorithm in sequence
    '''

    @classmethod
    def check(cls, sequence: str) -> bool:
        """
        Checks control digit by Luhn algorithm
        :param sequence: full number of card
        :return: true, if number is correct
        """
        if len(sequence) <= 1:
            raise ValueError("Sequence can't have less then 2 digits in itself")
        control_sum = 0
        for i in range(-2, -len(sequence) - 1, -1):
            summand = int(sequence[i])
            if i % 2 == 0:
                summand = summand * 2
                if summand >= 10:
                    summand = summand // 10 + summand % 10
            control_sum += summand
        control_digit = (10 - ((control_sum % 10) % 10))
        return control_digit == int(sequence[-1])
