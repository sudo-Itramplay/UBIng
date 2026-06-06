Transició d'una aplicació única ([[Arquitectura Multicapa|monòlit]]) a un ecosistema de serveis independents.

**Monòlit:** tot el backend en **un únic procés, aplicació i desplegament**.
- ✅ Simplicitat, debugging senzill, un sol deploy. Ideal per a prototips i equips petits.
- ❌ **Escalabilitat limitada** (cal escalar tot el sistema), **acoblament elevat** (un canvi → recompilar tot), **tolerància a fallades limitada** (un bug tomba tot).

**[[Microserveis]]:** dividir el sistema en serveis autònoms i independents.

> **Quan NO microserveis:** sistemes petits, equips reduïts, baixa necessitat d'escalabilitat. **Quan SÍ:** sistemes grans i complexos, escalat individual, equips grans en paral·lel, _bounded contexts_ clars.

Relacionat: [[Microserveis]] · [[Arquitectura Multicapa]] · [[Docker i Kubernetes]]

#assignatura/SD #tipus/teoria
