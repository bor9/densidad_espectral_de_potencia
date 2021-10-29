# Definiciones de potencia y densidad espectral de potencia de señales en tiempo continuo

En este documento se presentan los conceptos de energía, potencia y densidades espectrales de señales en tiempo continuo. Se diferencian los casos de señales determinísticas y procesos aleatorios. Se clasifican las señales en señales de energía y señales de potencia y se incluye el teorema de Wiener-Khintchine, el cual demuestra que la función de autocorrelación y la densidad espectral de potencia de señales aleatorias forman un par de transformadas de Fourier. Finalmente, se incluye la deducción de la densidad espectral de potencia de una señal modulada por amplitud de pulsos (PAM, *Pulse Amplitude Modulation*) digital.

## Contenido del repositorio

El repositorio contiene el código fuente en Latex del documento y el código Python de las figuras.

## Compilación

```
$ latex signal_power_and_psd
$ bibtex signal_power_and_psd
$ latex signal_power_and_psd
$ latex signal_power_and_psd
$ dvipdf signal_power_and_psd.dvi
```
