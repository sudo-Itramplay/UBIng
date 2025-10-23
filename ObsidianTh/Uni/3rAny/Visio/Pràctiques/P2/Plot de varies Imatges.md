
donada una imatge d'un panda: panda.jpg

## Carreguem Imatge i 2grayscale
``` python
#Your solution

img_panda = io.imread('images_notebook/panda.jpg')

# Print dimension

print(img_panda.shape)

# Print data type

print(img_panda.dtype)

  

plt.imshow(img_panda)

# Remove axis (optional)

plt.axis('off')


### Note

from skimage.color import rgb2gray

  
  
# To display in RGB:

## plt.imshow(img_panda)

# To display in grayscale:

img_gray = rgb2gray(img_panda)

plt.imshow(img_gray, cmap='gray')
```


## Fem el Plot
```
  

from skimage.util import img_as_ubyte

  

img_gray = rgb2gray(img_panda)

# Save the image

io.imsave('panda_gray.jpg', img_as_ubyte(img_gray))

  

# Show in a 1x2 grid the RGB and the grayscale image

fig, axes = plt.subplots(1, 2, figsize=(10, 5))

  

for ax in axes:

ax.get_xaxis().set_visible(False)

ax.get_yaxis().set_visible(False)

# Or ax.axis('off')

  

axes[0].imshow(img_panda)

axes[1].imshow(img_gray, cmap='gray')

```