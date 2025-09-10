def attendence(day1, day2, day3):
    day1 = [mail.lower() for mail in day1]
    day2 = [mail.lower() for mail in day2]
    day3 = [mail.lower() for mail in day3]

    day1 = set(day1)
    day2 = set(day2)
    day3 = set(day3)

    total_unique = day1 | day2 | day3
    all_three = day1 & day2 & day3
    exactly_one = (day1 ^ day2 ^ day3)
    overlap_12 = day1 & day2
    overlap_23 = day2 & day3
    overlap_13 = day1 & day3

    print("Final Attendance Report:\n")
    print(f"Total unique attendees ({len(total_unique)}): {sorted(total_unique)}")
    print(f"Attended all three days ({len(all_three)}): {sorted(all_three)}")
    print(f"Attended exactly one day ({len(exactly_one)}): {sorted(exactly_one)}")
    print(f"Overlap between Day 1 & Day 2 ({len(overlap_12)}): {sorted(overlap_12)}")
    print(f"Overlap between Day 2 & Day 3 ({len(overlap_23)}): {sorted(overlap_23)}")
    print(f"Overlap between Day 1 & Day 3 ({len(overlap_13)}): {sorted(overlap_13)}")
attendence(
    ['a@gmail.com', 'b@gmail.com'],
    ['A@gmail.com', 'c@gmail.com'],
    ['B@gmail.com', 'C@gmail.com']
)
