import minecraft_data

def get_blocs_names():
    mcd = minecraft_data("1.19.2")
    plain_blocs = []
    for b in mcd.blocks_list:
        if (b['boundingBox'] == 'block' and mcd.blockCollisionShapes['blocks'][b['name']] == 1 ):
        #    plain_blocs.append((b['id'], b['name'])) # ID and Name
            plain_blocs.append(b['name']) # name only
    return plain_blocs;
        

if __name__ == "__main__":
    print(get_blocs_names())


        
#print(mcd.blockCollisionShapes['blocks']['cobblestone'])
#Degager les blocs transparants