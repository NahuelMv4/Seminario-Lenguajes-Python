
# Trabajo Práctico Integrador 1ra Parte
-------------------------------------------
**Grupo 17**

Integrantes:

    Integrante 1
    XXXXX/X

    Integrante 2
    XXXXX/X

    Nahuel Saroglia Gambino
    25447/6
-------------------------------------------
**¿Que hace este proyecto?**

Este proyecto por una parte se encarga de manejar los distintos datasets que nos han proporcionado,
con manejar nos referimos a leer, editar y guardar cada uno de ellos con las modificaciones 
pedidas por el trabajo práctico. Por otro lado se encontrará con una página de streamlit donde podrá
participar de PyTrivia, un juego de preguntas y respuestas donde podrás poner a prueba tus conocimientos 
en diferentes áreas.

-------------------------------------------
**Instalación en modo desarrollo**

Para ejecutar el proyecto se debe utilizar **Python 3.11** o versiones superiores.

**Linux**

Para instalar este proyecto usted debe realizar los siguientes comandos en su consola:
```
    python3.11 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
```

**Windows**

Para instalar este proyecto usted debe realizar los siguientes comandos en su consola:
```
    python3 -m venv venv
    source ./venv/Scripts/activate
    pip install -r requirements.txt
```
-------------------------------------------
**Uso**

Para correr los proyectos de datasets:
```
    source venv/bin/activate
    cd jupyter_notebooks
    jupyter notebook
```

Le abrirá una página local host en su navegador y podrá ver y ejecutar cualquiera de los 4 procesamientos realizados
por los integrantes del grupo.

Para correr el streamlit:
```
    source venv/bin/activate
    cd streamlit
    streamlit run 01_🏠Home.py
```

Le abrirá una página local host en su navegador con la interfaz de streamlit realizada por los integrantes del
grupo.

Si quiere cerrar cualquiera de las 2 paginas, deberá ir a la terminal en la que las ejecuto y presionar
las teclas Ctrl + C. Eso cerrara la pagina que haya abierto.