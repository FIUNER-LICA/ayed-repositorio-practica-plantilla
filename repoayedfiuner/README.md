# README

## Uso del Repositorio

Para utilizar este repositorio, es necesario seguir los siguientes pasos:

1. **Actualizar Directorios**: Asegúrate de que los directorios `algoritmos` y `estructuras` contengan los nuevos códigos fuente que deseas utilizar.

2. **Carpeta de Tests**: Verifica que la carpeta `tests` contenga los tests correspondientes para validar el funcionamiento del código.

3. **(Opcional) Generar una distribución independiente:**: Desde la raíz del proyecto, ejecuta el script `main_generar_distribucion.py` para generar la distribución deseada. Si trabajas de esta forma, deberás ejecutar este código cada vez que realizas una actualización en el código fuente para actualizar la distribución (contenido de la carpeta "dist").


### Instalación del paquete local en modo editable

La instalación de un paquete en modo editable, realiza la instalación añadiendo un hipervínculo al código original del paquete (es como un acceso directo al código fuente del paquete. De esta forma, *el modo editable permitirá editar el repositorio e inmediatamente probar su impacto en el proyecto donde se utilizan los elementos del repositorio sin necesidad de volver a instalar*).

1. Abrir el archivo deps/requirements.txt y añadir la siguiente línea (ruta relativa desde el archivo requirements.txt):
```
-e ../../repo_ayed_estudiantes_fiuner
```
(La opción `-e` instala en modo editable; si prefieres instalación normal usa `../../repo_ayed_estudiantes_fiuner`. En este caso, deberás reinstalar el paquete cada vez que realices un cambio en el código fuente del repositorio.)

NOTA: La ruta indicada para el paquete se corresponde con la plantilla de cátedra por lo que no debería ser necesario modificarla.

2. En Windows: 
- 2.a) Crear y activar un entorno virtual de instalar:
```
python -m venv .venv
.\.venv\Scripts\activate
```

- 2.b) Desde la raíz del proyecto donde añades el repositorio ejecutar (si es necesario):
```
pip install -r .\deps\requirements.txt
```

3. VSCode:

En VSCode, también puedes añadir a tu workspace el repositorio para trabajar simultáneamente en un proyecto y en el respositorio si es necesario o práctico.