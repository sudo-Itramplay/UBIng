**Per què SÍ** (avantatges):
- Enforçament de la **integritat** (tipus, claus úniques, regles de negoci).
- **Còpies de seguretat i recuperació** davant fallades.
- Representació de **relacions complexes** entre milers de dades.
- **Seguretat:** restricció d'accés amb comptes i permisos.

**Per què NO:**
- **Sobrecàrrega (overhead):** consumeix recursos per seguretat, concurrència i integritat.
- **Costos inicials** alts (maquinari, llicències, formació).
- **Casos concrets** on no compensa:
	- Aplicacions molt simples que no canvien mai.
	- Sistemes amb requeriments de **temps real** estrictes (el DBMS és massa lent).
	- Sistemes encastats (embedded) amb memòria molt limitada.
	- Aplicacions d'un sol usuari sense necessitat de concurrència.

Relacionat: [[Avantatges del DBMS]] · [[DBMS]]

#assignatura/BD #tipus/teoria
