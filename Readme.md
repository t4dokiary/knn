# Practica 1 de recuperacion de la informacion.

## Configuración del Entorno Virtual
1. Instalación de Python, para esta ocacion se utilizo la version 3.12.1.
2. comprobamos que python se instalo correctamente con el siguiente comando:
   ```zsh
   python --version
   ```
3. comprueba la versión de pip instalada con:
   ```zsh
   pip --version
   ```
4. Si estás utilizando Python 3.12.1, procede a instalar `virtualenv` con:
   ```zsh
   pip install virtualenv
   ```
5. Comprueba que `virtualenv` se instaló correctamente con:
   ```zsh
   virtualenv --version
   ```
## Ejecución del Entorno Virtual
1. Crea un entorno virtual ejecutando:
   ```zsh
   virtualenv env
   ```
2. Activa el entorno virtual con el comando:
   ```zsh
   .\env\Scripts\activate
   ```
3. Verifica que Python y pip estén correctamente instalados en el entorno virtual:
   ```zsh
   python --version
   ```
   ```zsh
   pip --version
   ```
4. Para revisar los paquetes instalados en el entorno virtual, utiliza:
   ```zsh
   pip freeze
   ```
5. Guarda los paquetes instalados en un archivo de requisitos con:
   ```zsh
   pip freeze > requirements.txt
   ```
6. Para salir del entorno virtual, ejecuta:
   ```zsh
   .\env\Scripts\deactivate
   ```
## Instalación de Dependencias
1. Para instalar las dependencias del proyecto, utiliza:
   ```zsh
   pip install -r requirements.txt
   ```
2. Para verificar que las dependencias se instalaron correctamente, ejecuta:
   ```zsh
   pip freeze
   ```