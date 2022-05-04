import os #it has method os.path.exist
import sys #(sys.argv[1], sys.argv[2], sys.argv[3])
from PIL import Image

img = sys.argv[1] #grabs imgage folder[we give argument in cmd]
output_img = sys.argv[2] #grabs output folder[we give argument in cmd]

#chk if new(folder) exists or not, if not then create one

if not os.path.exists(output_img): #looping through pokedex folder
 os.makedirs(output_img)

for file in os.listdir(img):
 openimg = Image.open(f'{img}{file}')
 clnname = os.path.splitext(file)[0] #os.path.split splits the text into parts in tuple form(that is we will split name and .jpg )
 openimg.save(f'{output_img}{clnname}.png','png')
 
 print('all done')





