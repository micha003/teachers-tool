# importing functions
import random_name as av_calc
import core
import random_name as r_name
import point_grade_calc as pg_calc
import average_calculator as av_calc

#Hauptschleife
if __name__ == "__main__":
    print(f"Das Teacher-Tool {core.version}! Type 0 for help -- Michael Vorogushyn 2022")
    core.line()
    while True:
        action = int(input(">>> "))
        core.line()

        if action == 0:
            print("Help:")
            print("Type 1 for average_calculator \n"
                  "Type 2 for random_names \n"
                  "Type 3 for point-grade-calculator")
            core.line()

        elif action == 1:
            modi_choose = input("Wähle den Modi aus: [einzel] oder [listen]: ")
            core.line()

            if modi_choose.startswith("e") or modi_choose.startswith("E"):
                av_calc.einzelmodus()
                core.line()
                continue
            elif modi_choose.startswith("l") or modi_choose.startswith("L"):
                av_calc.listmodus()
                core.line()
                continue
        elif action == 2:
            namensliste = list()
            r_name.main_func(namensliste)
            core.line()
        elif action == 3:
            pg_calc.main_func()
            continue
        else:
            continue