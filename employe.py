name = []
jobtile = []
age = []
salli = []
while 1 :

    print('1 - Add a new employe \n 2 - delete employe \n 3 - searh employe \n 4 - exit  ')
    something = int(input('  :  '))

    if something == 1 :

        name.append(input('The name of empo : '))
        jobtile.append(input('The title : '))
        age.append(input('The age : '))
        salli.append(input('The salli : '))

    if something == 2 : 
        
        delempo = int(input('Enter the number of the employe : '))
        delempo -= 1

        name.pop(delempo)
        jobtile.pop(delempo)
        age.pop(delempo)
        salli.pop(delempo)

    if something == 3 : 
        print('Two way to searh for employe \n 1 - searh by the number of the employe \n 2 - searh by name of the employe')
        thesearhway = int(input(' : '))
        if thesearhway == 1 :
            X = int(input('Number of emp : '))
            X -= 1
            print( 'name of emp : ', name[X] ,'\ntitle : ' , jobtile[X] ,'\nage : ', age[X] ,'\nsali' ,  salli[X]   )
        elif thesearhway == 2 :
            nameofempoforsearh = str(input('the name of the employe : '))
            nefs = name.index(nameofempoforsearh)
            print( 'name of emp : ', name[nefs] ,'\n title : ' , jobtile[nefs] ,'\n age : ', age[nefs] ,'\n sali' ,  salli[nefs]   )
    if something == 4 :
        
        break

