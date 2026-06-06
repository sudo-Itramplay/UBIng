
Sempre que hi hahi un color "fondo" hem de trobar la mascara

mask = img[:,:,:3]>0

mask=np.max(mask, axis=2)


AQUESTA MASK SON ELS PIXELS QUE HEM DE COPIAR

img_model_coat[mask] = img_coat[mask]
