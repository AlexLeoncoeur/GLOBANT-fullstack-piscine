# Usa una imagen base de Python
FROM python:3.10

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos requeridos
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de tu aplicación
COPY . .

# Expone el puerto que usa tu aplicación
EXPOSE 8000

# Comando por defecto para ejecutar la aplicación
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
