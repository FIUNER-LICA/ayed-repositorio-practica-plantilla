# Algoritmos y Estructuras de datos (TADs) reutilizables

## Algoritmos reutilizables
Descripción breve
- Carpeta destinada a alojar implementaciones de algoritmos que puedan reutilizarse en distintos proyectos (ordenación, búsqueda, grafos, estructuras auxiliares, etc.).
- Cada algoritmo debe ser independiente, probado y documentado.

Estructura recomendada
- /algoritmos/
    - /\<algoritmo-name\>/
        - implementation.py  ← archivo(s) con la implementación
        - tests/*            ← pruebas unitarias

Convenciones
- Nombres de carpetas: kebab-case (por ejemplo, binary-search).
- Archivos fuente: seguir convención del lenguaje (snake_case, PascalCase, etc.).
- README de cada algoritmo debe incluir:
    - Propósito y comportamiento
    - Complejidad temporal y espacial
    - Interfaz pública (firma de funciones/clases)
    - Ejemplo de uso
    - Referencias (si aplica)

Notas
- Mantener las implementaciones lo más puras y pequeñas posible.
- Evitar dependencias innecesarias; si se usan, documentarlas.

## Estructuras de datos (TADs) reutilizables

Descripción breve
- Carpeta destinada a alojar implementaciones de Tipos Abstractos de Datos (colas, pilas, listas enlazadas, árboles, tablas hash, heaps, conjuntos, grafos, etc.).
- Cada TAD debe ser una unidad bien definida: implementación, pruebas y documentación de su interfaz y propiedades.

Estructura recomendada
- /estructuras/
    - /\<tad-name\>/               ← kebab-case (por ejemplo, linked-list, hash-map)
        - implementation.py     ← archivo(s) con la implementación (seguir convención del lenguaje)
        - tests/                 ← pruebas unitarias

Convenciones de diseño y nombrado
- Nombres de carpetas: kebab-case.
- Interfaces públicas: tipos de entrada/salida y excepciones posibles.
- Si se proporcionan múltiples implementaciones (p. ej. array-list vs linked-list), indicar claramente diferencias y costes.

Pruebas
- Tests unitarios independientes y reproducibles.

Notas
- Mantener la interfaz lo más pequeña y estable posible. (estable: poca probabilidad de cambio)
- Encapsular representación interna; evitar exponer referencias internas mutables.
- Evitar dependencias externas innecesarias.

Ejemplo de árbol sugerido
- tads/
    - stack/
        - implementation.py
        - tests/
    - hash-map/
        - implementation.py
        - tests/
