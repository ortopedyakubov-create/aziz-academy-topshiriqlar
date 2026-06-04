# Kutubxona kitoblar soni hisobi
# Kurs: IT Dasturlash
# Mavzu: 2-mavzu: Birinchi dastur, print() va kommentlar
# Ball: 30
# Aziz Academy — AI Topshiriq

n = int(input())
print(f"Kitoblar soni:", n, sep="")
if n < 10:
    print("Kam kitob bor.")
elif 10 <= n <= 50:
    print("O'ratachi kitob bor.")
else:
    print("Ko'p kitob bor.")