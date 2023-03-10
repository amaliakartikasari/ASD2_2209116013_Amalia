import os
os.system("cls")

print("""
Nama    : Amalia Kartika Sari
NIM     : 2209116013
""")

Dataset = ["Arsel", "Avivah", "Daiva", ["Wahyu", "Wibi"]]

def fibonacci(e, x, o):
    searching1 = 0
    searching2 = 1
    fibonacci = searching1 + searching2
    while (fibonacci < o):
        searching1 = searching2
        searching2 = fibonacci
        fibonacci = searching1 + searching2
    offset = -1
    while (fibonacci > 1):
        i = min(offset + searching1, o-1)
        if (e[i] < x):
            fibonacci = searching2
            searching2 = searching1
            searching1 = fibonacci - searching2
            offset = i
        elif (e[i] > x):
            fibonacci = searching1
            searching2 = searching2 - searching1
            searching1 = fibonacci - searching2
        else:
            return i
    if (searching2 and e[o-1] == x):
        return o-1
    return -1
    
def search():
    print("Kata", x, "ditemukan pada:")
    for i in range(len(Dataset)):
        if isinstance(Dataset[i], list):
            for j in range(len(Dataset[i])):
                if Dataset[i][j] == x:
                    print(f"Array index ke-{i}, kolom ke-{j}")
        elif Dataset[i] == x:
            print(f"Array index ke-{i}")

x = "Arsel"
search()
print(50*"=")
x = "Avivah"
search()
print(50*"=")
x = "Daiva"
search()
print(50*"=")
x = "Wahyu"
search()
print(50*"=")
x = "Wibi"
search()