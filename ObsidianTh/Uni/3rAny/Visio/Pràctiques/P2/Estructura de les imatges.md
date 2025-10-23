Les imatges tindràn una estructura de matriu de 3 dimensions

dim 1 = Y
dim 2 = X
dim 3 = RGB

Les imatges s'emmagatzemen en un [[Numpy]] array, però es manipularàn i carregaran amb [[Scikit-image]]


Anar amb compte amb els dtype.
	Les imatges es solen treballar amb uint8
	Donat que el espectre RGB va de 0-255
	i uint8 té just aquest rang