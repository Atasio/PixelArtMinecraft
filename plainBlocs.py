import minecraft_data

mcd = minecraft_data("1.19.2")
plain_blocs = []
for b in mcd.blocks_list:
    if (b['boundingBox'] == 'block' and mcd.blockCollisionShapes['blocks'][b['name']] == 1 ):
        plain_blocs.append((b['id'], b['name']))
        
print(plain_blocs)
print(len(plain_blocs))
        
#print(mcd.blockCollisionShapes['blocks']['cobblestone'])
#Degager les blocs transparants