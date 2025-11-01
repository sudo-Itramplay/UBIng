

Indica on està el template a la imatge, el normalized cross-correlation
	Algo de detecció de ulls
Sum of swqared-> fast but sensitive a canvis de contrast

correlation -> Less sensitive to ilumination changes

Zero-mean correlation -> Less sensitive to mask and image values

Normalized X_correlation-> Less sensitive to mask and image variance




HOG
	No vull tant que depengui de pixels, aixó que divideixo l ull en regions (una greu) Això es farà amb un descriptor
	Així serém més tolerants a canvis de la imatge

Per a cada subregió farem el calcul de quants píxels hi ha amb angle 0, 90, 180 (exemples) no vas de 1 a 1 pq é sridicul, no hi ha casi diferència

La direcció és la derivada entre (o tangent o les dos) d'un pixel en relació als veins (crec)


SIFT

Per trobar zones distintives, és una zona de la imatge on canvia si ens movem d'adalt cap abaix i de dreta a esquerra (cantonades)
	Quant més diferents siguin, "major longitud de fletxa" 
Si $\lambda$ 1 o 2 és 0 vol dir que un dels dos cantons no pateix canvi

Si no depen de la iluminació no depen de la rotació
Com fer lo invariant escala? 
	Provar diferents mides de areas de detecció i a la que dongui maximum cornerness function