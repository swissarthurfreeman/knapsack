#Algorithme du Knapsack.
from random import *

#Classe d'objets. 
class TBanana:
    def __init__(self, volume, price):
        self.volume = volume
        self.price = price
        #Le rapport est entre prix et volume, donc le plus petit le mieux. 
        self.rapport = self.volume / self.price
    #repr sert à préciser comment afficher un TBanana.
    def __repr__(self):
        return "\n Banana : Vol : " + str(self.volume) + " Pr : " + str(self.price) + " R : " + str(self.rapport)
 
def fill_bag(bag_volume, objects):

    val_array = objects

    #On trie selon la clef rapport. (Les premiers sont les plus précieux)
    val_array.sort(key = lambda x : x.rapport)

    print(val_array)

    #Volume indique le volume du knapsack au fur et à mesure.
    volume = 0
    objects_to_take = []
    
    for k in range(0, len(val_array)):
        #Si on ne dépasse pas le volume limite en prenant l'objet.
        if volume + val_array[k].volume <= bag_volume:
            objects_to_take.append(val_array[k]) #On le prends.
            volume += val_array[k].volume #On incrémente le volume.
        else:
            #Si on a un objet qui dépasse le poids maximal, on prends une fraction.
            place_restante = bag_volume - volume
            fac = place_restante / val_array[k].volume
            object_frac = TBanana(place_restante, objects[k].price*fac)
            objects_to_take.append(object_frac)
            break #On arrête, car on a le poids maximal.

    return objects_to_take

items_list = []
#On génère 20 bananes avec des volumes et prix aléatoires entre 1 et 5.
for i in range(0, 20):
    seed() 
    items_list.append(TBanana(randint(1,5), randint(1,5)))

#On fait pour un volume maximal de 10.
items_to_take = fill_bag(10, items_list)
print(items_to_take)

