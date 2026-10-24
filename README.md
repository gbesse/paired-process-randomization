# paired-process-randomization

## Français

Comparer deux procédés par un test exact de randomisation appariée.

Données fictives ; aucun accès réseau ni secret requis.

```sh
python -m paired_process_randomization examples/demo.json --lang fr
python -m unittest discover -s tests -v
```

### Méthode et différence

Énumère les 2ⁿ inversions de signe des différences appariées sous une hypothèse nulle préspécifiée ; direction et traitement des égalités sont déclarés. Différent du bootstrap par blocs : ici la distribution nulle est exacte et finie.

### Limites

Au plus16 paires ; validité conditionnée à l’échangeabilité des signes et au plan de comparaison, pas une preuve causale sur mesures observationnelles.

### Validation

Tests de domaine, cas limites et interface FR/EN/ES. La CI teste Python 3.11/3.13 et exécute la wheel installée hors du checkout. JSON conserve les identifiants techniques et les données fournis. Erreur d’entrée : code de sortie 2.

## English

Compare processes with an exact paired randomization test.

Synthetic data; no network access or secret required.

```sh
python -m paired_process_randomization examples/demo.json --lang en
python -m unittest discover -s tests -v
```

### Method and difference

Enumerates2ⁿ sign flips of paired differences under a prespecified null; direction and tie handling are explicit. Unlike block bootstrap, this null distribution is exact and finite.

### Limits

At most16 pairs; validity requires sign exchangeability and the comparison design, not causal evidence from observational measurements.

### Validation

Domain tests, boundary cases and FR/EN/ES interface. CI tests Python 3.11/3.13 and runs the installed wheel outside the checkout. JSON preserves technical identifiers and supplied data. Invalid input exits with code 2.

## Español

Comparar procesos con una prueba exacta de aleatorización emparejada.

Datos sintéticos; no requiere red ni secretos.

```sh
python -m paired_process_randomization examples/demo.json --lang es
python -m unittest discover -s tests -v
```

### Método y diferencia

Enumera2ⁿ inversiones de signo de diferencias emparejadas bajo hipótesis nula prefijada; dirección y empates explícitos. A diferencia del bootstrap por bloques, la distribución nula es exacta y finita.

### Límites

Máximo16 pares; validez condicionada a intercambiabilidad de signos y diseño de comparación, no evidencia causal de medidas observacionales.

### Validación

Pruebas de dominio, casos límite e interfaz FR/EN/ES. CI prueba Python 3.11/3.13 y ejecuta la wheel instalada fuera del repositorio. JSON conserva identificadores técnicos y datos proporcionados. Entrada inválida termina con código 2.

## Sources / Fuentes

- https://www.itl.nist.gov/div898/handbook/pri/section3/pri332.htm
