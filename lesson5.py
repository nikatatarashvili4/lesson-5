# სსავარჯოშო 1


amount = float(input("ყიდვის თანხა (ლარი): "))
promocode = input("პრომო-კოდი (თუ არ გაქვთ — Enter): ")

if amount >= 200:
    discount_p = 20

elif amount >=  100:
    discount_p = 10

elif amount >= 50:
    discount_p = 5

else:
    discount_p = 0

disocunted = amount - amount *discount_p / 100

if promocode == "vip":
    disocunted -= 5
    print("🎖 VIP კოდი: დამატებით -5 ლარი: ")

print("ფასდაკლება: ", discount_p, "%")
print("გადასახდელი: ", round(disocunted, 2), "ლარი")


# სავარჯიშო 2


try:
    name = input("სტუდენტის სახელი: ") . strip()
    score = float(input("მიღებული ქულა: "))
    most_score = float(input("მაქსიმალური ქულა: "))

    if name == "":
        raise ValueError("სახელი ცარიელია")
    if most_score <= 0:
        raise ValueError("მაქსიმალური ქულა 0 ან ნაკლები უნდა არ იყოს")
    if score <0 or score > most_score:
        raise ValueError("ქულა არასწორ დიაპაზონშია")

except ValueError as e:
    print("❌", e)


else:
    percent = score / most_score * 100

    if percent >= 91:
        grade = "A"
    elif percent >= 81:
        grade = "B"
    elif percent >= 71:
        grade = "C"
    elif percent >= 61:
        grade = "D"
    elif percent >= 51:
        grade = "E"
    elif percent >= 41:
        grade = "FX"

    else:
        grade = "F"

    print(f" {name} — {percent:.1f}% — შეფასება: {grade}")

finally:
    print("შეფასების სისტემა დასრულდა")
    