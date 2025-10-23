Per Reescalar imatges amb [[Scikit-image]] Tenim una funció de la propia llibreria
`from skimage.transform import rescale`

i s'aplica tal que:
```python
from skimage.transform import rescale
# Create a new RGB black image 15% larger than the img_panda (in both dimensions)

# First we create a black image with the desired size

###### OPCIO1
img_panda_black = np.zeros((int(img_panda.shape[0]*1.15), int(img_panda.shape[1]*1.15), 3), dtype=np.uint8)

##### OPCIO2
# ALternatively using the skimage rescale function
img_panda_black = rescale(img_panda, 1.15)
# Set all values to 0
img_panda_black = img_panda_black * 0 

##### OPCIO3
img_panda_black[:,:] = 0

# If suing rescale, we need to convert the image to uint8


# Embed the panga image in the center of the black image

img_panda_black[img_panda_black.shape[0]//2-img_panda.shape[0]//2:img_panda_black.shape[0]//2+img_panda.shape[0]//2,

img_panda_black.shape[1]//2-img_panda.shape[1]//2:img_panda_black.shape[1]//2+img_panda.shape[1]//2] = img_panda

  

plt.imshow(img_panda_black)

plt.axis('off')
```