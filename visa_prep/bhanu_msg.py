import re
phone_num=input().strip()
pattern_code=r"^\+\d{2} \d{10}$"
if re.match(pattern_code, phone_num):
    digits=phone_num.split()[1]
    if sum(int(digit) for digit in digits) > 0:
        print("Correct")
    else:
        print("Incorrect")
elif len(phone_num) == 10 and phone_num.isdigit():
    print("Correct")
else:
    print("Incorrect")
