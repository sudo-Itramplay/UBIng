Per aplicar una funció a cada element d'una columna
```
df['ColumnaResultat'] = df['ColumnaOriginal'].apply(NomDeLaFunció)
# O amb una funció lambda (molt comú)
df['ColumnaResultat'] = df['ColumnaOriginal'].apply(lambda x: x * 2 + 1)

```
