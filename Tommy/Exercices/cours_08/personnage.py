import des

force = 0
points_de_vie = 0

def creation(f, pv):
    f = des.des_20(1) #On lance 1 de
    pv = des.des_6(2) #On lance 2 des
    return f, pv

force, points_de_vie = creation(force, points_de_vie)
print(force)
print(points_de_vie)