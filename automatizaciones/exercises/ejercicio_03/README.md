# 3️⃣ Automatización de backups

### Problema

Automatizar el backup de una base de datos.

El script debe:

1. Ejecutar backup de PostgreSQL
2. Comprimir el archivo
3. Guardarlo con timestamp
4. Eliminar backups antiguos (más de 10 días)

### Pistas

Usar:

```python
subprocess
gzip
datetime
```

---