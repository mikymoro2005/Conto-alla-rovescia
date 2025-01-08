import time

def conto_alla_rovescia():
    while True:
        try:
            secondi = int(input("Inserisci il numero di secondi per il conto alla rovescia: "))
            if secondi < 0:
                print("Per favore inserisci un numero positivo!")
                continue
            break
        except ValueError:
            print("Per favore inserisci un numero valido!")
    
    for i in range(secondi, -1, -1):
        print(f"\rTempo rimanente: {i} secondi", end="")
        time.sleep(1)
    
    print("\nTempo scaduto!")

while True:
    conto_alla_rovescia()
    if input("\nVuoi fare un altro conto alla rovescia? (s/n): ").lower() != 's':
        break

print("Grazie per aver usato il conto alla rovescia!")
