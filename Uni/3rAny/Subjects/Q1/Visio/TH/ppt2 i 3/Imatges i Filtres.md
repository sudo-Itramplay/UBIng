Teoria de filtres i altres

```dataviewjs
for (let group of dv.pages('"3rAny/Visio/TH"').groupBy(p => p.file.folder)) {
    
    // Assegureu-vos d'ajustar la clau de l'agrupació per evitar veure la ruta completa a la capçalera
    // Aquesta línia elimina el "3rAny/Tallers/T1/PPT3/" de la capçalera, deixant només el nom de la subcarpeta.
    dv.header(3, group.key.replace("3rAny/Visio/TH" + "/", "")); 
    
    dv.table(["Nom de la Nota", "Mida (Bytes)"],
        group.rows
            .sort(k => k.file.name, 'asc')
            .map(k => [k.file.link, k.file.size])
    );
}
```



