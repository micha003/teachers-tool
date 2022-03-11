import core

def point_grade():
    total_points = int(input("Geben Sie die maximale Anzahl der Punkte: "))
    core.line()

    grade1 = float(total_points) * 0,96
    grade2 = float(total_points) * 0,8
    grade3 = float(total_points) * 0,6
    grade4 = float(total_points) * 0,45
    grade5 = float(total_points) * 0,16
    grade6 = float(total_points) * 0

    print(f"Note 1: {grade1} \n"
          f"Note 2: {grade2} \n"
          f"Note 3: {grade3} \n"
          f"Note 4: {grade4} \n"
          f"Note 5: {grade5} \n"
          f"Note 6: {grade6} \n")
    core.line()

def main_func():
    again = 1

    while again == 1:
        point_grade()

        again = int(input("Reset 1; Stop 0 \n"
                          "Eingabe: "))
        if not again == 1 or not again == 0:
            while not again == 1 or not again == 0:
                again = int(input("Dies ist nicht gültig. Reset 1; Stop 0 \n"
                                "Eingabe: "))
                core.line()

                if again == 1 or again == 0:
                    break
                else:
                    continue
        else:
            pass

        if again == 1:
            continue
        elif again == 0:
            break
        else:
            print("Bug!")
            exit(564)