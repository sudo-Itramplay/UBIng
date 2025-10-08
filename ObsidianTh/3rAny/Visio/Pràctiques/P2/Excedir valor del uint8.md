Editant Imatges amb [[Scikit-image]] Pot sorgir el error

**Imatge més Brillant (Multiplicació):** S'intenta fer la imatge el doble de brillant (`cat*2`).

>[!Warning] **Problema:**
> Si `cat` és `uint8`, `cat*2` pot resultar en **desbordament/wrapping** on 255∗2=510 pot esdevenir un valor baix (e.g., 254 o 255 segons l'entorn/biblioteca).

>[!tip] Solució
>Per visualitzar correctament una imatge 'més brillant' s'ha de forçar els límits de visualització amb `vmin=0, vmax=255` (tal com es fa al codi) per a veure l'efecte.


```
ax = axs[1,0]
ax.imshow(cat*2, vmin=0, vmax=255) 



# NOTA: Amb dtype uint8, l'operació *2 pot patir wrapping. L'efecte real depèn de la implementació.
```