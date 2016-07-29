import time

class Recipe:
    ingredients = []
    instructions = ""
    name = ""

    '''
    def print(self):
        return
    '''

recipes = []

# grilled cheese
gc = Recipe()
gc.ingredients = ['bread', 'cheese', 'butter']
gc.name = "Grilled cheese"
gc.instructions = "Melt butter in pan.  Grate cheese on bread.  Add other slice.  Flip, adding butter as needed."
recipes.append(gc)

fe = Recipe()
fe.ingredients = ['eggs', 'butter']
fe.name = "Fried egg"
fe.instructions = "Cook egg in butter over medium heat."
recipes.append(fe)



print "Welcome to omnom!"

def top_menu():
    print "\nPlease select an action:"
    print "1) Create new recipe"
    print "2) Select recipe"
    print "\n0) Exit"

    x = input("\n> ")
    return x

def new_recipe():
    pass

def select_recipe():
    print "\nPlease select a recipe:"
    i = 1
    for r in recipes:
        print str(i) +  ") " +  r.name
        i += 1
    print "\n0) Return to previous menu"
    x = input("\n> ")
    if x == 0:
        return
    elif x > len(recipes):
        print "Invalid selection! Returning to previous menu..."
    else:
        print_recipe(recipes[x - 1])


    return

def print_recipe(r):
    print r.name
    print 
    print r.ingredients
    print
    print r.instructions
    return

while True:
    action = top_menu()

    if action == 1:
        new_recipe()

    elif action == 2:
        select_recipe()
    
    elif action == 0:
        break
    else:
        print "Invalid command. Please enter another."
        continue

