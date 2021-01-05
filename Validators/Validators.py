from Errors.Errors import ValidationError


class Validators:

    @staticmethod
    def validate_column(column):
        if column > 7 or column < 1:
            raise ValidationError("The column must be an integer between 1 and 7")

    @staticmethod
    def validate_option(option):
        if not option.isnumeric():
            raise ValidationError("Option should be an integer number between 1 and 7!")
