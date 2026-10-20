  import random


def oyin():
    maxfiy_son = random.randint(1, 100)
    urinishlar = 0
    maksimum = 7

    print("=== SON TOPISH O'YINI ===")
    print(f"Men 1 dan 100 gacha son o'yladim. Sizda {maksimum} ta urinish bor.\n")

    while urinishlar < maksimum:
        try:
            taxmin = int(input(f"{urinishlar + 1}-urinish. Sonni kiriting: "))
        except ValueError:
            print("Iltimos, faqat son kiriting!\n")
            continue

        urinishlar += 1

        if taxmin < maxfiy_son:
            print("Kattaroq son ayting ⬆️\n")
        elif taxmin > maxfiy_son:
            print("Kichikroq son ayting ⬇️\n")
        else:
            print(f"🎉 Tabriklayman! {urinishlar} ta urinishda topdingiz!")
            return

    print(f"😔 Urinishlar tugadi. Maxfiy son: {maxfiy_son}")


def main():
    while True:
        oyin()
        yana = input("\nYana o'ynaymizmi? (ha/yo'q): ").strip().lower()
        if yana != "ha":
            print("Xayr! Yana ko'rishguncha 👋")
            break
        print()


if __name__ == "__main__":
    main()
