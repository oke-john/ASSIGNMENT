print("Filing Status:")
print("0 → Single filer")
print("1 → Married filing jointly / Qualified widow(er)")
print("2 → Married filing separately")
print("3 → Head of household")

status = int(input("Enter your filing status (0–3): "))
if status < 0 or status > 3:
    print("Invalid filing status.")
    exit()

income = float(input("Enter your taxable income: "))
if income < 0:
    print("Income cannot be negative.")
    exit()

tax = 0.0

# ---- SINGLE FILER ----
if status == 0:
    if income > 372950:
        tax += (income - 372950) * 0.35
        income = 372950
    if income > 171550:
        tax += (income - 171550) * 0.33
        income = 171550
    if income > 82250:
        tax += (income - 82250) * 0.28
        income = 82250
    if income > 33950:
        tax += (income - 33950) * 0.25
        income = 33950
    if income > 8350:
        tax += (income - 8350) * 0.15
        income = 8350

    tax += income * 0.10


# ---- MARRIED FILING JOINTLY / WIDOW ----
elif status == 1:
    if income > 372950:
        tax += (income - 372950) * 0.35
        income = 372950
    if income > 208850:
        tax += (income - 208850) * 0.33
        income = 208850
    if income > 137050:
        tax += (income - 137050) * 0.28
        income = 137050
    if income > 67900:
        tax += (income - 67900) * 0.25
        income = 67900
    if income > 16700:
        tax += (income - 16700) * 0.15
        income = 16700

    tax += income * 0.10


# ---- MARRIED FILING SEPARATELY ----
elif status == 2:
    if income > 186475:
        tax += (income - 186475) * 0.35
        income = 186475
    if income > 104425:
        tax += (income - 104425) * 0.33
        income = 104425
    if income > 68525:
        tax += (income - 68525) * 0.28
        income = 68525
    if income > 33950:
        tax += (income - 33950) * 0.25
        income = 33950
    if income > 8350:
        tax += (income - 8350) * 0.15
        income = 8350

    tax += income * 0.10


# ---- HEAD OF HOUSEHOLD ----
elif status == 3:
    if income > 372950:
        tax += (income - 372950) * 0.35
        income = 372950
    if income > 190200:
        tax += (income - 190200) * 0.33
        income = 190200
    if income > 117450:
        tax += (income - 117450) * 0.28
        income = 117450
    if income > 45500:
        tax += (income - 45500) * 0.25
        income = 45500
    if income > 11950:
        tax += (income - 11950) * 0.15
        income = 11950

    tax += income * 0.10


print(f"Total tax owed: ${tax:.2f}")
