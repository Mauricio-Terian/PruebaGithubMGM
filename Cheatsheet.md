# Cheatsheet(Hoja de Ayuda) - Git y Linux 

## Comandos básicos de Linux

```bash
ls
# Lista todos los archivos

cd "**nombre_carpeta**"
# Entra a una carpeta específica

cd **""..**""
# Regresa a la carpeta anterior

pwd
# Muestra la ruta del directorio actual

clear
# Limpia la terminal

mkdir **""nombre_carpeta**""
# Crea una nueva carpeta

touch **""archivo.txt""**
# Crea un archivo vacío

rm **""archivo.txt"**
# Elimina un archivo
```

## Comandos git

```bash
git --version
# Muestra la versión instalada de Git

git init
# Inicializa un repositorio Git en la carpeta actual

git status
# Muestra el estado del repositorio y cambios

git add .
# Agrega todos los archivos al área de preparación

git commit -m "mensaje"
# Guarda cambios con un mensaje

git branch -M main
# Renombra la rama principal a main

git remote add origin URL
# Conecta el repositorio local con GitHub

git remote -v
# Muestra los repositorios remotos conectados

git push -u origin master
# Sube el proyecto a GitHub por primera vez

git pull
# Descarga cambios del repositorio remoto

git clone URL
# Clona un repositorio desde GitHub
```
