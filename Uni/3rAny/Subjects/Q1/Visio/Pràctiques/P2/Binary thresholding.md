Agafar una imatge i fer que tots els valos siguin blanc (255) o negre (0)
Passar imatge a binaria
``` python
mean = np.mean(img_gray)
# Binary thresholding
img_binary = img_gray > mean
plt.imshow(img_binary, cmap='gray')

```

