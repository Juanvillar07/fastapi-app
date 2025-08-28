# 🚀 Guía de Configuración e Inicio del Proyecto FastAPI

Este proyecto utiliza **FastAPI** como framework principal.  
A continuación se explican los pasos para clonar el repositorio, configurar el entorno virtual en una carpeta separada e instalar las dependencias necesarias.

---

## 📂 Organización de Carpetas

La idea es tener una estructura como esta:

<img width="479" height="122" alt="image" src="https://github.com/user-attachments/assets/dc79ba64-5d22-4164-b198-bd3f449b05db" />


De esta forma, el entorno virtual (`venv`) y el proyecto (`proyecto-fastapi`) estarán dentro de la misma carpeta raíz.

---

## 1. Clonar el Repositorio

Primero, crea una carpeta donde guardarás tanto el proyecto como el entorno virtual:

```bash
mkdir MiCarpetaDeTrabajo
cd MiCarpetaDeTrabajo
```

Ahora clona el repositorio dentro de esa carpeta:
```bash
git clone <URL_DEL_REPOSITORIO> proyecto-fastapi
```

## 2. Crear el Entorno Virtual
```bash
python -m venv venv
```

## 3. Activar el Entorno Virtual
Antes de instalar las dependencias, debes activar el entorno virtual.

En Windows:
```bash
.\venv\Scripts\activate
```
En macOS/Linux:
```bash
source venv/bin/activate
```
Verás que tu terminal cambia y muestra (venv) al inicio, indicando que el entorno está activo.


