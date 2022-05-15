from PIL import Image
import numpy as np
import operator

def merger():

    array1 = np.random.choice([0,255],(19,19),p=[0.05,0.95]) #(height,width,3)
    array2 = np.random.choice([0,255],(19,19),p=[0.05,0.95]) #(height,width,3)

    array1 = np.array(array1, dtype=np.uint8)
    array2 = np.array(array2, dtype=np.uint8)

    #print("The Array1 is: ", array1)
    #print("The Array2 is: ", array2)

    img = Image.fromarray(array1).convert('L')
    img.save('random1.png')
    img = Image.fromarray(array2).convert('L')
    img.save('random2.png')

    #print("The Array1 is: ", array1)
    array1[array1 == 0] = 1
    array2[array2 == 0] = 1

    #print("The Array1 is: ", array1)
    #print("The Array2 is: ", array2)

    arraym = np.add(array1, array2)
    arraym[arraym == 254] = 255
    arraym[arraym < 3] = 0
    arraym = np.array(arraym, dtype=np.uint8)
    print("The Arraym is: ", arraym)
    #arraym = [array1[i]+array2[i] for i in range(len(array1))]

 


    #arraym[arraym < 255] = 
    #arraym[arraym == 510] = 255


    img = Image.fromarray(arraym).convert('L')
    img.save('merged.png')



#random_img('random.png', 19, 19)
merger()


