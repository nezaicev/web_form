import re
regex_email = r"^[-\w.]+@([A-z0-9][-A-z0-9]+\.)+[A-z]{2,4}$"
regex_phone = r"^((\+7)+([0-9]){10})$"
regex_date = r"(0?[1-9]|[12][0-9]|3[01])[.](0?[1-9]|1[012])[.]((19|20)\d\d)"
regex_date_additional = r"[0-9]{4}-(0[1-9]|1[012])-(0[1-9]|1[0-9]|2[0-9]|3[01])"


def validate_field(field):
    if field:
        if re.match(regex_date, field):
            return 'date'
        if re.match(regex_date_additional, field):
            return 'date'
        if re.match(regex_phone, field):
            return 'phone'
        if re.match(regex_email, field):
            return 'email'
        else:
            return 'text'
    else:
        return 'Type not valid (date, phone, email, text)'



