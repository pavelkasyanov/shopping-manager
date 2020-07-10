def validate_float_or_none(value):
    return validate_number_or_none(value, default_value=0.0)


def validate_number_or_none(value, default_value):
    # if value is not None:
    #     return value >= 0.0
    # else:
    #     return True
    return (value is None) or (value and value >= default_value)
