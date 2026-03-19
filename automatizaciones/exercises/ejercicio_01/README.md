# 1️⃣ Automatización de limpieza de archivos

### Problema

Una carpeta `/tmp/uploads` acumula archivos diariamente.

Crea un script que:

1. Elimine archivos de más de **7 días**
2. Genere un **reporte de archivos eliminados**
3. Se ejecute automáticamente cada día.

### Habilidades evaluadas

* manejo de archivos
* scripting
* automatización

### Pistas

Usar:

```python
os
pathlib
datetime
```


### Nota
- La nota en la que podemosa saber si un archivo es antiguo en python es con stat(), un ejemplo de uso es:
```python
file.stat().st_mtime
```
Esto nos devuelve el valor en segundos desde la fecha de 1970 `1719872342.34` 