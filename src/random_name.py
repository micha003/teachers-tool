import random as r
import core

# get the Name-list
def get_names(namensliste, p_anzahl_namen):
    p_anzahl_namen = int(input("Geben Sie bitte die Anzahl der Namen ein (mind. 2): "))
    core.line()

    if p_anzahl_namen >= 2:
        pass
    elif not p_anzahl_namen >= 2:
        while not p_anzahl_namen >= 2:
            p_anzahl_namen = int(input("Dies ist nicht gültig. Bitte geben Sie die Anzahl der Namen ein (mind. 2): "))
            core.line()

            if p_anzahl_namen >= 2:
                break
            else:
                continue


    # get the Names

    for i in range(p_anzahl_namen):
        temp_name = input(f"Name {i + 1}: ")
        namensliste.append(temp_name)

    core.line()
    print(namensliste)
    core.line()

    return namensliste, p_anzahl_namen

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

def randomizing_groups(namensliste, p_anzahl_namen):
    groups_or_mem = int(input("Anzahl Gruppen [1] oder Anzahl Gruppenmitglieder [2] ?: "))
    core.line()

    if groups_or_mem == 1 or groups_or_mem == 2:
        pass
    else:
        while not groups_or_mem == 1 or not groups_or_mem == 2:
            groups_or_mem = int(input("Dies ist nicht gültig! Anzahl Gruppen [1] oder Anzahl Gruppenmitglieder [2] ?: "))
            core.line()

            if groups_or_mem == 1 or groups_or_mem == 2:
                break

    if groups_or_mem == 1:
        anzahl_gruppen = int(input("Wie viele Gruppen sollen eingeteilt werden? (mind. 2): "))
        core.line()

        if anzahl_gruppen <= 1:
            while not anzahl_gruppen >= 2:
                anzahl_gruppen = int(input("Dies ist nicht zulässig. Bitte geben sie die Anzahl der Gruppen ein (mind. 2): "))
                core.line()

                if anzahl_gruppen <= 1:
                    continue
                else:
                    break
        else:
            pass

        group_members = p_anzahl_namen / anzahl_gruppen
        group_members = round(group_members)

    elif groups_or_mem == 2:
        group_members = int(input("Wie viele Leute pro Gruppe? (mind. 2): "))
        core.line()

        if group_members <= 1:
            while not group_members >= 2:
                group_members = int(input("Dies ist nicht zulässig. Bitte geben sie die Anzahl der Gruppen ein (mind. 2): "))
                core.line()

                if group_members <= 1:
                    continue
                else:
                    break
        else:
            pass

        anzahl_gruppen = p_anzahl_namen / group_members
        anzahl_gruppen = round(anzahl_gruppen)

    groups = []

    for i in range(anzahl_gruppen):
       for a in range(group_members):
           temp_name = r.choice(namensliste)


           groups.append(temp_name)

       print(f"Gruppe {i + 1}: {groups}")
       del groups[:]

    core.line()

def main_func(namensliste):
    again = 1
    anzahl_namen = 0

    get_names(namensliste, anzahl_namen)

    while again == 1 or again == 0:
        if again == 0:
            get_names(namensliste, anzahl_namen)

        groups_decide = int(input("Geben Sie 1 ein, wenn direkt Gruppen eingeteilt werden sollen. Sonst wählen sie 0."
                                  "\n >>> "))
        core.line()

        if groups_decide == 0 or groups_decide == 1:
            pass
        else:
            while not groups_decide == 0 or not groups_decide == 1:
                groups_decide = int(
                    input("Geben Sie 1 ein, wenn direkt Gruppen eingeteilt werden sollen. Sonst wählen sie 0. \n"
                          ">>>"))
                core.line()

                if groups_decide == 0 or groups_decide == 1:
                    break
                else:
                    continue

        if groups_decide == 0:

            randomizing(namensliste)

        elif groups_decide == 1:
            randomizing_groups(namensliste, anzahl_namen)

        again = int(input(
            'Geben Sie bitte 1 ein, wenn neue Gruppen eingeteilt werden sollen bzw. ein zufälliger Name ausgewählt werden soll. \n'
            'Geben Sie bitte 2 ein, wenn sie keinen weiteren Namen auswählen möchten \n'
            'Geben Sie bitte 0 ein, wenn sie eine neue Namensliste angeben möchten: \n'
            'Eingabe: '))
        core.line()

        if again == 0 or again == 1 or again == 2:
            pass
        else:
            print("Dies ist nicht zulässig!")
            core.line()

            while 0 > again > 2:
                again = int(input("Geben Sie bitte 1 ein, wenn Sie neue Namen auswählen wollen. \n"
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
    anzahl = 0
    main_func(list)

    #dies ist ein kommentar
