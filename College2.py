__author__ = 'Rick'

def opdracht431():
    import csv
    csvbestand = 'csv-file.csv'

    try:
        f = open(csvbestand, 'r')
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            print('Baanvak: {0:35s} Snelheid: {1:3s}'.format(row["Baanvak"], row["Snelheid (km/u)"]))
    finally:
        f.close()


def opdracht432():
    import csv

    voorletters = input("Voorletter(s): ")
    achternaam  = input("Achternaam: ")
    geboortedatum = input("Geboortedatum: ")
    email = input("E-mailadres: ")

    try:
        f = open('eticket.txt', 'a', newline='')
        writer = csv.writer(f, delimiter=',')
        writer.writerow((input("Voorletter(s): "), input("Achternaam: "), input("Geboortedatum: "), input("E-mailadres: ")))
    finally:
        f.close()
opdracht432()