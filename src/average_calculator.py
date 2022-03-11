import core

def einzelmodus():
    again = 1

    while again == 1:
        anzahl_noten = int(input("Geben Sie bitte die Anzahl der erteilten Noten ein: \n"
                                ">>> "))
        core.line()

        sum = 0

        for i in range(anzahl_noten):
            temp_note = int(input(f"Note {i + 1}:"))
            core.line()

            if temp_note < 1 or temp_note > 6:
                while temp_note < 1 or temp_note > 6:
                    temp_note = int(input(f"Dies ist nicht zulässig. Note {i + 1}: "))
                    core.line()

                    if temp_note < 1 or temp_note > 6:
                        continue
                    else:
                        break
            else:
                pass

            sum += temp_note

        average = sum / anzahl_noten

        print(f"average: Ø{average}")

        again = int(input("Nochmal: 1 \n"
                          "Beenden: 0 \n"
                          ">>> "))
        core.line()

        if again == 1:
            continue
        elif again == 0:
            break
        else:
            while not again == 1 or not again == 0:
                print("Dies ist nicht gültig.\n"
                      "Nochmal: 1 \n"
                      "Beenden: 0 \n"
                      ">>> ")
                core.line()

                if again == 1 or again == 0:
                    break
                else:
                    continue

        if again == 1:
            continue
        elif again == 0:
            break

def listmodus():
    again = 1

    while again == 1:
        sum = 0
        num = 0

        for i in range(6):
            input_num = int(input(f"Anzahl Note {i + 1}: "))
            num += input_num

            core.line()

            temp_note = input_num * (i + 1)
            sum += temp_note

        average = sum / num

        average = round(average, 2)

        print(f"average: Ø{average}")
        core.line()


        again = int(input("Nochmal: 1 \n"
                          "Beenden: 0 \n"
                          ">>> "))

        if again == 1:
            continue
        elif again == 0:
            break
        else:
            while not again == 1 or not again == 0:
                print("Dies ist nicht gültig.\n"
                      "Nochmal: 1 \n"
                      "Beenden: 0 \n"
                      ">>> ")
                core.line()

                if again == 1 or again == 0:
                    break
                else:
                    continue

        if again == 1:
            continue
        elif again == 0:
            break


if __name__ == "__main__":
    listmodus()