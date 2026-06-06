Amb volums massius de dades, **transferir-les als processadors per la xarxa** esdevé el **coll d'ampolla** dels sistemes distribuïts. Cal una nova arquitectura ([[Hadoop]], [[Spark]]).

**Requeriments:** robustesa a fallades parcials, recuperació sense pèrdua de dades, recuperació "calenta" de nodes, consistència d'execució, **escalabilitat** (en càrrega i en recursos).

> [!info] Teorema de CAP
> Un sistema distribuït només pot garantir **2 de 3**:
> - **Consistència (C):** tota lectura rep l'escriptura més recent.
> - **Disponibilitat (A):** tot node actiu retorna resposta.
> - **Tolerància a Particions (P):** funciona malgrat fallades de xarxa.
>
> Com que les fallades de xarxa són inevitables, **P és obligatòria** → cal escollir entre **CP** o **AP**.

Relacionat: [[Hadoop]] · [[Spark]] · [[Reptes dels Sistemes Distribuïts]]

#assignatura/SD #tipus/teoria
