# Distrobox per a GiVD
Si estem intentant fer ús d'un sistema amb compositor wayland, en comptes de X11, pot ser que tinguem molts problemes a la hora d'instalar totees les dependències i fer que funcionin, a més d'embrutar el sistema amb llibreries extres que potser no s'estàn fent servir, per aquesta raó, en sistemes que no siguin ni ubuntu ni debian, es recomanable fer una aproximació diferent amb Distrobox
## 1. Què és Distrobox?

Distrobox és una eina que permet crear i gestionar contenidors d'altres distribucions de Linux de forma totalment integrada amb el teu sistema operatiu principal. És una espècie de màquina virtual que corre únicament el nucli del sistema a emular, proporcionant més rendiment i flexibilitat .A diferència d'una màquina virtual tradicional, un contenidor de Distrobox:

* Comparteix la teva carpeta `/home` de manera nativa. (és a dir, navegaràs en el teu ordinador inclús dins la màquina virtual)
* Té accés directe a la teva xarxa i als dispositius externs (com ara targetes gràfiques i USB).
* Executa programari a (quasi) velocitat nativa.

## 2. Flux de Treball Recomanat

Per optimitzar el desenvolupament, la metodologia més eficient és dividir les tasques entre el sistema natiu i el contenidor:

* 
**Desenvolupament i Edició (Host Natiu):** Escriu el teu codi usant Visual Studio Code  de manera nativa en el teu sistema operatiu principal. Això et permet tenir una interfície gràfica fluida i fer ús de totes les extensions (com les de C++ i CMake ) sense afegir sobrecàrregues.


* 
**Compilació i Execució (Contenidor):** Mitjançant el terminal integrat de l'editor, obre una sessió de Distrobox per executar els processos de `cmake`, compilar el codi  i obrir l'aplicació final. D'aquesta manera garantim que estem utilitzant exactament les mateixes versions de les llibreries que s'utilitzaran per a l'avaluació.



---

## 3. Instal·lació de Distrobox al Sistema Amfitrió

Necessitarem instal·lar tant el programari per gestionar els contenidors (Podman o Docker) com el propi Distrobox.

**Per a sistemes Fedora:**
En el cas de Fedora, utilitzarem `dnf`  per instal·lar els paquets:

```bash
sudo dnf install distrobox podman

```

**Per a sistemes Arch Linux:**
En lloc d'usar `apt`, utilitzarem `pacman` per instal·lar les eines necessàries:

```bash
sudo pacman -S distrobox podman

```

---

## 4. Creació i Accés als Contenidors de Desenvolupament

Procedirem a crear un entorn basat en Ubuntu o Debian per assegurar una compatibilitat idèntica als paquets sol·licitats a les pràctiques.

**Opció Principal (Ubuntu):**

```bash
distrobox create --name givd-ubuntu --image ubuntu:latest

```
- Si donés algun error, prova amb la versió ubuntu:20.4

**Opció de Respatller (Debian - Útil per si l'entorn Ubuntu donés algun conflicte):**

```bash
distrobox create --name givd-debian --image debian:latest

```

Per començar a treballar dins de l'entorn, executa la següent comanda des de qualsevol terminal (inclòs el del Visual Studio Code ):

```bash
distrobox enter givd-ubuntu

```

*(Substitueix `givd-ubuntu` per `givd-debian` si has optat per la segona via).*

---

## 5. Instal·lació de Dependències i Llibreries al Contenidor

Un cop dins del teu contenidor `givd-ubuntu`, tindràs accés al gestor de paquets `apt`. Ara aplicarem l'estructura d'instal·lació definida a la guia de l'assignatura.

Prèviament, posa al dia el teu Linux:

```bash
sudo apt update
sudo apt upgrade -y

```



Tot seguit, instal·la les eines de desenvolupament bàsiques i de compilació de C++:

```bash
sudo apt-get install build-essential gdb pkg-config cmake

```



Finalment, instal·la les llibreries de gràfics  i l'eina sol·licitada per treballar amb formats JSON. Executa:

```bash
sudo apt-get install libglfw3 libglfw3-dev libglew-dev nlohmann-json3-dev

```

(Això instal·la GLFW i GLEW tal com s'indica a les instruccions generals de la pràctica, i hi afegeix de la mateixa manera `nlohmann` al teu sistema).
