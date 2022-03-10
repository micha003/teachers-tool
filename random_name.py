import random as r
import core

# get the Name-list
def get_names(namensliste):
    anzahl_namen = int(input("Geben Sie bitte die Anzahl der Namen ein (mind. 2): "))
    core.line()

    if anzahl_namen <= 1:
        while not anzahl_namen >= 2:
            anzahl_namen = int(input("Dies ist nicht zulässig. Bitte geben sie die Anzahl der Namen ein (mind. 2): "))
            core.line()

            if anzahl_namen <= 1:
                continue
            else:
                break
    else:
        pass

    # get the Names

    for i in range(anzahl_namen):
        temp_name = input(f"Name {i + 1}: ")
        namensliste.append(temp_name)

    core.line()
    print(namensliste)
    core.line()
    return namensliste

def randomizing(namensliste):
    chosen_name = r.choice(namensliste)
    print(chosen_name)

    core.line()

    del_name = input("Soll der Name aus der Liste gelöscht werden? (j/n): ")

    if del_name.startswith("j") or del_name.startswith("J"):
        index = 0
        for d in namensliste:
            if d == chosen_name:
                del namensliste[index]
                print(namensliste)
                core.line()
                break
            else:
                index += 1
    else:
        core.line()
        pass

def main_func(namensliste):
    again = 1
    get_names(namensliste)

    while again == 1 or again == 0:
        if again == 0:
            get_names(namensliste)

        randomizing(namensliste)

        again = int(input("Geben Sie bitte 1 ein, wenn sie einen anderen Namen auswählen möchten. \n"
                        "Geben Sie bitte 2 ein, wenn sie keinen weiteren Namen auswählen möchten \n"
                        "Geben Sie bitte 0 ein, wenn sie eine neue Namensliste angeben möchten: \n"
                        "Eingabe: "))
        core.line()

        if again == 0 or again == 1 or again == 2:
            pass
        else:
            print("Dies ist nicht zulässig!")
            core.line()

            while not again < 0 and not again > 2:
                again = int(input("Geben Sie bitte 1 ein, wenn sie einen anderen Namen auswählen möchten. \n"
                                  "Geben Sie bitte 2 ein, wenn sie keinen weiteren Namen auswählen möchten \n"
                                  "Geben Sie bitte 0 ein, wenn sie eine neue Namensliste angeben möchten: \n"
                                  "Eingabe: "))
                core.line()

                if not again < 0 and not again > 2:
                    print("Dies ist nicht zulässig!")
                    core.line()
                    continue
                elif again < 0 and not again > 2:
                    break

        if again == 1:
            continue
        elif again == 2:
            break
        elif again == 0:
            continue
        else:
            print("BUG --Bye!")
            exit(-56)

if __name__ == "__main__":
    list = []
    main_func(list)