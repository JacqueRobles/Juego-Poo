import Juego_POO 




class Main_game:
    def menu_inicio():
        while (True):
            print("1)Ver los personajes ")
            print("2)Elegir personaje")
            # print("3)Combate ") 
            # print("4)elegir objeto ")
            
            op = int(input("Elija una opcion: "))
            if (op == 1):
                print("\tMago \tGuerrero \tAsesino")
                print(f"vida: {Mage.hp} \t{Warrior.hp} \t{Assassin.hp}")
        # name,hp,damage,strength,weapon,power,intelligence
        # name,hp,damage,strength,weapon,sword
        # name,hp,damage,strength,weapon,dagger")
            elif (op == 2):
                print("(1)Mago \n(2)Guerrero \n(3)Asesino")
                op_character = int(input("Elija un personaje: "))
                if (op_character == 1):
                    p = Mage()
                    print("¡Estas a punto de entrar en combate!, ¿quieres cambiar tu eleccion?")
                    op = input
                    menu(p)
                elif (op_character == 2):
                    p = Warrior()
                    menu(p)
                elif (op_character == 3):
                    p = Assasin()
                    menu(p)
                else: print("Elija una opcion")

            # elif (op == 3):
            #     menu(p)
            # elif (op == 4):
            #     ...