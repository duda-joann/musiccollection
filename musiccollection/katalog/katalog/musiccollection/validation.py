from django.core.exceptions import ValidationError


class ValidateYear:
    message = ('Enter a valid value.')
    code = 'invalid'

    @staticmethod
    def compare(self, current_year, date_of_publishment):
        return current_year > date_of_publishment

