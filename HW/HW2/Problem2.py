def main():
    n = input("Enter a date (mm/dd/yyyy): ")
    month = n[0:2]
    day = n[3:5]
    year = n[6:11]
    dictMonth = {
        "01":"January",
        "02":"February",
        "03": "March",
        "04": "April",
        "05": "May",
        "06": "June",
        "07": "July",
        "08": "August",
        "09": "September",
        "10": "October",
        "11": "November",
        "12": "December",
    }

    print(dictMonth.get(month), str(day)+",", str(year))


main()