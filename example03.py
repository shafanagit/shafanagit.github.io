from datetime import datetime, timedelta

def nic_to_birthdate(nic):
    nic = nic.strip().upper()

    # Old NIC format
    if len(nic) == 10:
        year = 1900 + int(nic[:2])
        day_of_year = int(nic[2:5])

    # New NIC format
    elif len(nic) == 12:
        year = int(nic[:4])
        day_of_year = int(nic[4:7])

    else:
        return "Invalid NIC"

    gender = "Male"

    if day_of_year > 500:
        gender = "Female"
        day_of_year -= 500

    birth_date = datetime(year, 1, 1) + timedelta(days=day_of_year - 1)

    return {
        "Year": birth_date.year,
        "Month": birth_date.month,
        "Date": birth_date.day,
        "Gender": gender,
        "Birth Date": birth_date.strftime("%Y-%m-%d")
    }


# Example
nic = input("Enter NIC Number: ")
result = nic_to_birthdate(nic)

print(result)