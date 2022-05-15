from PIL import Image
from Merge import merger
import numpy as np
import operator


#def random_img(output, width, height):
    #yes = [0,255]
#    array = np.random.choice([0,255],(height,width,3),p=[0.1,0.9]) #(height,width,3)

    #array = np.array(array, dtype=np.uint8)
    #array = np.array(dtype=np.uint8)
#    print(array)

#    img = Image.fromarray(array).convert('1')
#    img.save(output)


#random_img('random.png', 10, 10)




def random_img(output, width, height):
    #yes = [0,255]
    #make array with dots
    array = np.random.choice([0,255],(height,width),p=[0.05,0.95]) #(height,width,3)

    #then we cut out donut array



    array = np.array(array, dtype=np.uint8)
    #array = np.array(dtype=np.uint8)
    print(array)

    img = Image.fromarray(array).convert('L')
    img.save(output)

    random_img('random.png', 19, 19)

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


