## Velocitat de Transmissió

$$
\Large
V_{TRX[bps]} = V_{TRX[bauds]} * n_{bits}

$$
>[!IMPORTANT]
>- $V_{TRX[bps]}$ és la velocitat de transmissió en bits per segon
>       
> - $V_{TRX[bauds]}$ és la velocitat de transmissió en bauds
>      
> - $n_{bits}$ és el nombre de bits

$$
\Large
V_{TRX[bps]} = V_{TRX[bauds]} * log_2{(N_{iv})}
$$
>[!IMPORTANT]      
> - $N_{iv}$ és el nombre de nivells de tensió

$$
\Large
V_{TRX[bps]} = 2 * BW * n_{bits}
$$
>[!IMPORTANT]
>- BW és l'ample de banda 
### Llei de Hartley
$$
\Large
V_{TRX[bps]} = 2 * BW * log_2{(N_{iv})}
$$

>[!WARNING]
>Aquesta llei ignora el **soroll**

### Teorema de Shannon
$$
\Large
V_{TRX [bps]} = BW * log_2{(1 + \frac{S}{N})}
$$
>[!IMPORTANT]
>- S és la potència del **senyal [W]**
>- N és la potència del **soroll [W]**
>- $SNR = \frac{S}{N}$

## Potència $\to$ dB
$$
\Large
[dB] = 10 * log_{10}{([W])}
$$
>[!IMPORTANT]
>- $[dB]$ és una variable en decibels
>- $[W]$ és una variable en Watts

## dB $\to$ Potència
$$
\Large
[W] = 10^{\frac{[dB]}{10}}
$$
## Soroll tèrmic
$$
\Large
N_T[W] = n_{T0} * BW
$$
>[!IMPORTANT]
>- $N_T[W]$ és la potència **total** de soroll
>- $n_{T0}$ és la densitat espectral del soroll

$$
\Large
N_T[W] = K_B * T * BW
$$
>[!IMPORTANT]
>- $K_B$ és la constant de Boltzmann $\approx 1,38*10^{-23} [J/K]$
>- $T$ és la temperatura **absoluta**

## Atenuació
$$
\Large
Atenuació = 10 * log_{10}{(\frac{P_{entrada}}{P_{sortida}})}dB
$$
>[!NOTE]
>Notes inferiors no s'apliquen

$$
\Large
L(dB) = 10 * log_{10}{((\frac{4 * \pi * d}{\lambda})^2)}
$$
>[!IMPORTANT]
>- d és la distància a **l'emissor**
>- $\lambda$ és la longitud d'ona 


>[!WARNING]
>És una equació per medis **no guiats**
## Amplificació
$$
\Large
Amplificació = 10 * log_{10}{(\frac{P_{sortida}}{P_{entrada}})}dB
$$

## Potència rebuda (Friis)
$$
\Large
P_{RX} = G_{RX} * G_{TX} * P_{TX} * (\frac{\lambda}{4 * \pi * d})^2 * \eta
$$
>[!IMPORTANT]
>- $P_[RX]$ és potència **rebuda**
>- $P_[TX]$ és la potència **transmesa**
>- $G_{TX}$ és el **guany** de l'antena transmissora
>- $G_{RX}$ és el guany de l'antena receptora
>- $\eta$ és l'eficiència total (0 - 1)

## Verificació d'una trama
$$
\Large
Q(x) = \frac{M(x) * 2^n + R(x)}{G(x)}
$$
>[!IMPORTANT]
>- $M(x)$ és un nombre de $k$ **bits**
>- $G(x)$ és un nombre de $n + 1$ bits anomenat **divisor / generador**
>- $R(x)$ és un nombre de $n < k$ bits anomenat **residu**
>- $Q(x)$ és el **quocient**

>[!WARNING]
>Sense errors, residu = 0.
>Amb errors, residu $\neq$ 0


