
# Trabajo Practico Integrador 1ra Parte
-------------------------------------------
**Grupo 17**

Integrantes:

    Franco Dario Ramirez
    22063/9

    Felipe Di Placido
    21256/2

    Nahuel Saroglia Gambino
    25447/6
-------------------------------------------
**¿Que hace este proyecto?**

Este proyecto por una parte se encargara de manejar los distintos datasets que nos han dado,
con manejar nos referimos a leer, editarlos y guardar cada uno de ellos con las modificaciones 
pedidas por el trabajo practica. Por otro lado encontraras un streamlit con la informacion
de los 3 integrantes que participaron en la creacion de este proyecto junto con un apartado 
para poder realizar un registro que en la segunda parte del trabajo integrador sera utilizado,
este registro puede guardar tus datos en un archivos JSON para que no se pierdan.

-------------------------------------------
**Instalacion en modo desarrollo**

Para ejecutar el proyecto se debe utilizar python 3.11 o versiones superiores.

Para instalar este proyecto usted debe realizar los siguientes comandos en su consola:
```
    phyton3.11 -m venv venv
    source venv/bin/activate
    pip install -r requirementes.txt
```
-------------------------------------------
**Uso**

Para correr los proyectos de datasets:
```
    source venv/bin/activate
    cd jupyter_notebooks
    jupyter notebook
```

Le abrira una pagina local host en su navegador y podra ver y ejecutar cualquiera de los 4 procesamientos realizados
por los integrantes del grupo.

Para correr el streamlit:
```
    source venv/bin/activate
    cd streamlit
    streamlit run 01_🏠Home.py
```

Le abrira una pagina local host en su navegador con la interfaz de streamlit realizada por los integrantes del
grupo.

Si quiere cerrar cualquiera de las 2 paginas, debera ir a la terminal en la que las ejecuto y presionar
las teclas Ctrl + C. Eso cerrara la pagina que haya abierto.