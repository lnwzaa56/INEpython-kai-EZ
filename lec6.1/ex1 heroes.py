heroes=['Ironman', 'Thor', 'Hulk', 'Spiderman']
def display_heroes():
    print(heroes)

     
def add_heroes():
    global heroes
    new_heroes = input("please input new heroes:")
    heroes.append(new_heroes)
    print(heroes)

def insert_heroes():
    heroes.insert(0)
    print(f"Enter heroes:{heroes}")

    








display_heroes() 
add_heroes()
insert_heroes()









