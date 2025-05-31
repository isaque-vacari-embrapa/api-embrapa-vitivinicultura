import re


def transform_value(value):
    try:
        value = value.replace(",", ".")
        value = int(round(float(value)))
        return value if value >= 0 else 0
    except ValueError:
        return 0


def transform_scrap_value(value):
    if value:
        value = value.strip()
        if value == "-":
            value = "0"
        if value == "*":
            value = "0"

        aux_value = value.replace(".", "")
        if is_float(aux_value):
            value = transform_value(aux_value)
    return value


def is_float(string):
    if re.match(r"^[-+]?[0-9]*\.?[0-9]+$", string):
        return True
    else:
        return False
