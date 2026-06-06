### Pas 1: Definició del Raig i el Triangle

Abans de calcular res, hem de tenir clares les nostres dades d'entrada.

- **El Raig**: Es defineix com una línia paramètrica $P(t) = A + t \cdot \vec{B}$, on $A$ és l'origen i $\vec{B}$ la direcció.
    
- **El Triangle**: Definit per tres vèrtexs en l'espai 3D: $V_0, V_1, V_2$.
    

### Pas 2: Calcular el Pla del Triangle

Un triangle és, per definició, pla. Necessitem saber l'equació d'aquest pla per trobar on el raig el travessa.

1. **Calcula les arestes**: Necessites dos vectors que vagin d'un vèrtex a un altre (per exemple, de $V_0$ a $V_1$ i de $V_0$ a $V_2$).
    
2. **Calcula la Normal ($\vec{N}$)**: Fes el producte vectorial (cross product) d'aquestes dues arestes. Això et donarà un vector perpendicular a la superfície del triangle.
    
    - _Nota_: Recorda normalitzar aquest vector $\vec{N}$ (fer que tingui longitud 1).
        

### Pas 3: Intersecció Raig-Pla

Ara busquem el punt $P$ on el raig creua aquest pla infinit. L'equació per trobar la distància $t$ des de l'origen del raig fins al pla és derivada de substituir l'equació del raig en l'equació del pla.

La fórmula general per aïllar la $t$ es basa en productes escalars (dot product):

$$t = \frac{(V_0 - A) \cdot \vec{N}}{\vec{B} \cdot \vec{N}}$$

_(On $V_0$ és un punt qualsevol del pla, $A$ l'origen del raig, i $\vec{B}$ la direcció)._

**Comprovacions crítiques en aquest punt:**

- **Paral·lelisme**: Si el denominador ($\vec{B} \cdot \vec{N}$) és proper a zero, significa que el raig és paral·lel al triangle. No hi ha intersecció.
    
- **Darrere la càmera**: Si la $t$ resultant és negativa ($t < 0$), el pla està darrere l'observador. Has de descartar-ho.
    

### Pas 4: El Test d'Interior (Coordenades Baricèntriques)

Ara sabem que el raig xoca amb el pla en el punt $P$ (calculat com $A + t \cdot \vec{B}$). La pregunta és: **Aquest punt cau dins del triangle o a fora?**

Per resoldre això, convertim el punt $P$ a **Coordenades Baricèntriques** $(u, v, w)$. Aquest sistema expressa $P$ com una mitjana ponderada dels tres vèrtexs:

$$P = u \cdot V_0 + v \cdot V_1 + w \cdot V_2$$

Has d'implementar el càlcul d'aquestes coordenades $(u, v, w)$. Un cop les tinguis, la condició per confirmar que el punt és **DINS** del triangle és estricta:

1. $u \ge 0$
    
2. $v \ge 0$
    
3. $w \ge 0$
    
4. $u + v + w = 1$ (Aquesta condició és implícita si calcules $w$ com $1 - u - v$).
    

### Pas 5: Validació Final i Retorn

Si el punt ha passat el test baricèntric, has trobat una intersecció vàlida. Ara has de complir el "contracte del mètode Hit":

1. **Comprovar el rang**: La $t$ trobada ha d'estar dins l'interval $[t_{min}, t_{max}]$. Si està més lluny que una intersecció anterior, l'ignorem.
    
2. **Omplir la informació d'impacte**:
    
    - La $t$ d'impacte.
        
    - El Punt $P$ exacte.
        
    - La Normal $\vec{N}$ en el punt d'impacte.
        
    - El Material del triangle.
        
3. **Retornar CERT**.
    

---

### Resum visual de l'algorisme

1. **Calcular Normal** del triangle.
    
2. **Trobar $t$** (distància al pla).
    
    - _Si és paral·lel o $t < 0$ → Fals._
        
3. **Calcular Punt $P$** ($ray.origin + t * ray.direction$).
    
4. **Calcular $(u, v, w)$** de $P$ respecte als vèrtexs.
    
5. **Verificar** si $u, v, w \ge 0$.
    
    - _Si algun és negatiu → Fals (el punt és al pla, però fora del triangle)._
        
6. **Si tot OK → Cert** i guardar dades.