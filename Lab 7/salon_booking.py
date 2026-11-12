
def parse_booking(text):
    if not isinstance(text, str) or text.count(':') != 1:
        return None

    service, minutes = text.split(':')
    try:
        minutes = float(minutes)
        if not service.strip() or minutes < 0:
            return None
        return service.strip().title(), minutes
    except ValueError:
        return None


def duration_average(durations_csv):
    if not isinstance(durations_csv, str) or not durations_csv.strip():
        return 0

    try:
        values = [int(r.strip()) for r in durations_csv.split(',')]
        if not values or any(x < 0 for x in values):
            return 0
        return sum(values) // len(values)
    except ValueError:
        return 0


def payable_bill(text):
    if not isinstance(text, str) or text.count('|') != 1:
        return 0

    bill, discount = text.split('|')
    try:
        bill = float(bill)
        discount = float(discount)
        if bill < 0 or discount < 0:
            return 0
        total = bill * 1.18 - discount
        return max(total, 0)
    except ValueError:
        return 0


def main():
    print("==== Running parse_booking ====")
    user_input = input("Enter service:duration in min (e.g. haircut:45): ")
    result = parse_booking(user_input)
    print("Service and Duration:", result)

    print("\n==== Running duration_average ====")
    user_input = input("Enter durations as CSV (e.g. 30,45,60): ")
    result = duration_average(user_input)
    print("Average Duration:", result)

    print("\n==== Running payable_bill ====")
    user_input = input("Enter bill|discount (e.g. 800|100): ")
    result = payable_bill(user_input)
    print("Payable Bill:", result)

if __name__ == "__main__":
    main()
