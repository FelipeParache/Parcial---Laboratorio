# Simulación de Batallas - Dragon Ball Z

Programa desarrollado en Python que simula batallas entre personajes de la serie Dragon Ball Z. El proyecto permite cargar datos de personajes desde un archivo CSV, realizar diversas consultas y acciones, y simular batallas entre el usuario y la máquina.

## Descripción del Proyecto

El programa permite a los usuarios interactuar con un menú para:
- Listar personajes por raza.
- Calcular promedios de poder de ataque y pelea.
- Jugar batallas entre personajes elegidos por el usuario y la máquina.
- Guardar datos en formato JSON y CSV.

## Estructura del Proyecto

- **main.py**: Archivo principal que inicia el programa y gestiona el flujo de la aplicación.
- **menu.py**: Contiene las funciones para mostrar el menú y manejar las opciones seleccionadas por el usuario.
- **funciones_numericas.py**: Incluye funciones para realizar cálculos y sanitizar datos numéricos.
- **funciones_listar.py**: Contiene funciones para listar personajes y sus atributos.
- **funciones_batalla.py**: Define la lógica para simular batallas entre personajes.
- **funciones_string.py**: Funciones para manipular cadenas de texto y generar códigos de personajes.
- **DBZ.csv**: Archivo CSV que contiene la información de los personajes de Dragon Ball Z, incluyendo atributos como poder de ataque, habilidades y raza.

## Funcionalidades

1. **Cargar Datos**: Permite cargar los datos de los personajes desde un archivo CSV.
2. **Listar Personajes**: Opción para listar personajes por raza, habilidad o atributos específicos.
3. **Simular Batallas**: Los usuarios pueden elegir un personaje para enfrentarse a un personaje elegido aleatoriamente por la máquina.
4. **Guardar en JSON**: Guarda los personajes con habilidades y razas específicas en un archivo JSON.
5. **Generar CSV**: Crea un archivo CSV con los datos actualizados de los personajes de raza Saiyan.
6. **Ordenar Personajes**: Permite ordenar la lista de personajes por diferentes atributos.
7. **Generar Códigos de Personajes**: Asigna códigos únicos a cada personaje basado en su información.

## Ejemplo de Uso

Al ejecutar el programa, se presentará un menú con varias opciones. Por ejemplo, al elegir la opción para listar personajes por raza, el programa mostrará la cantidad de personajes de cada raza disponible en el archivo CSV.
