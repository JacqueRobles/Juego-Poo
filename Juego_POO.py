from random import randint

class Champ():
    def __init__(self,name,strength,intelligence,defense,hp): ##atributos##
        self.name = name
        self.strength = strength
        self.intelligence = intelligence
        self.defense = defense
        self.hp = hp

    def its_alive(self):
        return self.hp>0

    def death(self):
        self.vida=0
        print(self.nombre,"Ha muerto")

    def attack(self,e):
        damage = self.damage(e)
        e.hp = e.hp - damage
        print(self.name, "ha realizado",damage,"puntos de vida a", e.name)
        if e.its_alive:
            print("Vida restante de", e.name, "es:", e.hp)
        else:
            e.death
    def set_name(self):
        self.name = int(input("Ingresa tu nombre: "))

    def get_name(self):
        return self.name
    def get_hp(self):
        return self.hp
    def get_strength(self):
        return self.strength
    def get_intelligence(self):
        return self.intelligence
    def get_defense(self):
        return self.defense


class Mage(Champ):  ##subclases con herencia## 
    def init(self,name,hp,strength,defense,intelligence,wand):
        super().__init__(self,name,hp,strength,defense,intelligence)
        self.wand = wand
        hp = 90   
        strength = 10
        defense = 10
        intelligence = 30

    def choose_weapon(self):
        option = int(input("Baston de la ventisca: Daño+ Defensa++ |Último prisma:Daño+++ Vida-"))
        if option == 1:
            self.wand = 1.4
            self.defense += 10
        elif option == 2:
            self.wand = 3
            hp-= 5 

    def damage(self):
        return self.intelligence*self.wand - e.defense
    
    def special_damage(self):
        return (self.intelligence+5)*self.wand - e.defense

    def special_attack(self,e):
        damage = self.damage(e)*1.5
        self.hp -= 5
        e.hp = e.hp - damage
        print(self.name, "ha realizado",damage,"puntos de vida a", e.name)
        if e.its_alive:
            print("Vida restante de", e.name, "es:", e.hp)
        else:
            e.death

class Warrior(Champ):
    def __init__(self,name,hp,strength,defense,intelligence,sword):
        super().__init__(self,name,hp,strength,defense,intelligence)
        self.sword = sword
        hp = 140  
        strength = 15
        defense = 25
        intelligence = 10

    def choose_weapon(self):
        option = int(input("Diente Abrazador: Daño+ Vida++ |Titanicus: Daño++ Vida+"))
        if option == 1:
            self.sword = 1.3
            self.hp+=30
        elif option == 2:
            self.sword = 2
            hp+= 10 
            
    def damage(self):
        return self.strength*self.sword - e.defense

    def special_damage(self):
        return 


class Assassin(Champ):
    def __init__(self,name,hp,strength,defense,intelligence,dagger):
        super().__init__(self,name,hp,strength,defense,intelligence)
        self.dagger = dagger      
        hp = 100  
        strength = 25
        defense = 10
        intelligence = 15

    def change_weapon(self):
        option = int(input("Sangre Roja, Daño++ Inteligencia+ |Claro de Luna: Daño+ Defensa++"))
        if option == 1:
            self.dagger = 1.4
            self.intelligence += 5 
        elif option == 2:
            self.dagger = 2.2
            self.defense += 10

    def damage(self):
        return self.strength*self.dagger - e.defense


class Enemy(Champ):
    def __init__(self,name,hp,strength,defense,intelligence):
        super().__init__(name,hp,strength,defense,intelligence)
        
        n = randint(1,5)
        if n == 1:
            name = "Goblin"
        elif n == 2:
            name = "Ogro"
        elif n == 3:
            name = "Fantasma"
        elif n == 4:
            name = "Kobold"
        elif n == 5:
            name = "Jabali Salvaje"

        hp = randint(80,200)
        strength = randint(80,150)
        defense = randint(80,120)
        intelligence = randint(80,150)

e = Enemy('o',5,2,1,1)
p = Champ('b',5,2,1,1)

def menu(p):
    while True:
        print("1) Elegir un personaje")
        print("2) Estadisticas")
        
        try:
            n = int(input("Elige un Numero: "))

            if n == 1:
                choose_class(p)
            if n == 2:
                menu_stats(p)
            else:
                print("Que estas Esperando?")

        except NameError:
            print("Elige un Numero")
        except SyntaxError:
            print("Elige un Numero")

def choose_class(self):
    print("Elige tu clase:")
    print("1)Mago: Daño+++/Vida+/Defensa+")
    print("2)Guerrero: Daño+/Vida+++/Defensa++")
    print("3)Asesino: Daño++/Vida++/Defensa+")
    print("*****************")
    c = input()
    if c == 1:
        print("MAGO")
        p = Mage('a',90,10,10,30,1)
    elif c == 2:
        p = Warrior('b',140,15,25,10,1)
    elif c == 3:
        p = Assassin('c',100,25,10,15) 

def menu_stats(self):
    print("Estadísticas del jugador")
    print("*****************")
    print("Nombre:",self.get_name)
    print("Hp:",self.hp)
    print("Fuerza:",self.get_fuerza)
    print("Inteligencia",self.get_intelligence)
    print("Defensa:",self.get_defense)
    input("Presione Enter para continuar.")

def menu_fight(p):
    turn = 0
    while p.its_alive() and e.its_alive():
        print("\nTurno:", turn)
        print("1) Atacar")
        print("2) Curarse")
        print("3)Ataque especial")
        n = int(input("Introduce un número: "))
        if n == 1:
            p.attack(e)
            e.attack(p)
            turn = turn + 1
        if n == 2:
            # Al azar de 0 a 5 agrega HP.
            p.hp += randint(10,20)
            # Si la salud del jugador es mayor, entonces el HP del jugador será igual a 100.
            if p.hp > 100:
                p.hp = 100
            print(f"Tu HP {p.hp}")
            e.attack(p)
            turn = turn + 1
        if n == 3:
            p.special_attack(e)
            e.attack(p)
            turn = turn + 1

        else:
            print("¿Qué estamos esperando?")
        if p.hp < 0:
            print("Tú perdiste")
        if e.hp < 0:
            print("Tú perdiste")
        print("******************")

    ## input(
    ## mostrar menu (p)
    
    # Llamar al menu.
menu(p)
