Rajos secundaris del [[Ray Tracing]] que simulen com la llum travessa objectes (vidre, aigua), desviant-se segons el medi.

- **Índex de Refracció (IOR, $\mu$):** densitat òptica (Aire ≈ 1.0, Aigua = 1.33, Vidre = 1.66, Diamant = 2.42).
- **Llei de Snell:** $\frac{\sin\theta_t}{\sin\theta_i} = \frac{\mu_i}{\mu_t}$. El vector de transmissió es calcula amb `glm::refract`.
- **Reflexió Total Interna:** d'un medi dens a un de menys dens amb angle elevat, el raig no pot sortir i es reflecteix 100% (terme de l'arrel negatiu) → només es fa `glm::reflect`.
- **Orientació de la [[Normal]]:** si $\vec{i}\cdot\vec{n}>0$ som a l'interior → girar la normal.
- **Atenuació $K_t$ (RGB):** quins colors deixa passar; sovint $1 - K_s$.

**Simplificacions de pràctica:** rajos d'ombra sense refracció, ombres no tenyides, sense objectes niats.

Relacionat: [[Reflexions]] · [[Equació de Color]] · [[Ombres]] · [[Normal]]

#assignatura/Grafics #tipus/teoria
