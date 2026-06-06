Error gràfic freqüent en calcular [[Ombres]] (auto-intersecció): per precisió en coma flotant, el raig d'ombra colpeja el **propi objecte** d'origen, enfosquint la seva superfície.

- El raig cap a la llum és $p = p_0 + \lambda \cdot L$, amb origen al punt d'intersecció.
- **Solució:** desplaçar l'origen un epsilon en la direcció de la llum:
$$p_0 = p_0 + \epsilon \cdot L$$
- Típicament $\epsilon = 0.01$.

> Mateix problema (i solució) que el "Surface Acne" de les [[Reflexions]].

Relacionat: [[Ombres]] · [[Reflexions]] · [[Soft Shadows]]

#assignatura/Grafics #tipus/teoria
