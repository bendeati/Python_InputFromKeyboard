#adatok bekérése billentyűzetről

print("Kérem a nevét!")
nev = input()
print("A bekért adat típusa: ", type(nev))
print("Üdvözlöm ", nev, "!")

szulEv = input("Kérem a születési évét: ")
print("A bekért adat típusa", type(szulEv))
print("A beírt érték:", szulEv)

gyerekSzam = int(input("Kérem a gyerekeinek számát: "))
print("A bekért adat típusa", type(gyerekSzam))
print("A beírt érték:", gyerekSzam)