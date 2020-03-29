# Kata rest TDD 1 - MISO 4101 202010

Semana 9, actividad virtual 41: Kata REST en parejas

## Integrantes

|Nombre                      |Email                      |
|----------------------------|---------------------------|
|Juan Sebastian Alvarez Eraso|js.alvareze@uniandes.edu.co|
|Luis Felipe Pantoja Cerquera|l.pantojac@uniandes.edu.co |

## Descripción

Las Katas son prácticas de código que nos ayudan a mejorar. Estas prácticas usan los TDD (test unitarios) y los principios SOLID y se utilizan para mejorar nuestra programación, mejorar nuestros tiempos y aprender métodos nuevos.

**Nota:** Tomado de [https://geekytheory.com/antes-de-desarrollar-katas-tdd-y-solid](https://geekytheory.com/antes-de-desarrollar-katas-tdd-y-solid)

## Requisitos

Instalar los siguientes programas:

```bash
sudo apt install python3
sudo apt install python-pip
sudo apt install python3-dev
sudo apt install libpq-dev

pip install virtualenv
```

## Ejecutar el proyecto por primera vez

Descargar el proyecto:

```bash
git clone https://github.com/juanalvarez123/kata-rest-TDD1.git
```

Ir a la carpeta del proyecto e instalar el ambiente virtual:

```bash
cd kata-rest-TDD1
virtualenv -p python3 env
```

Esto creará la carpeta **env** en la raíz del proyecto. Luego:

```bash
# Activar el ambiente virtual
source env/bin/activate

# Instalar los paquetes del proyecto
pip install -r requirements.txt

# Ejecutar las migraciones pendientes
python manage.py migrate

# Correrlo !
python manage.py runserver
```

## ¿Cómo ejecutar el proyecto las siguientes veces?

```bash
cd kata-rest-TDD1
source env/bin/activate
python manage.py runserver
```
