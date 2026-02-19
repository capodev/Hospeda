# Hospeda

## Sistema para publicidad de hostales, hoteles, hosterias y sitios de alojamiento .

## para instalar los requerimientos en local del sistema he preparado un archivo requerimientos.txt

## Para ejecutarlo deben ejecutar

#### pip install -r requirements.txt

#### creamos el entorno virtual

##### python -m venv venv

#### levantamos el entorno virtual .\venv\Scripts\activate

## Como ejecutar las rutas Dinamicas

#### abriremos el sitio web Hospeda en local

#### Ejemplo localhost:5000 0 127.0.0.1:5000

### El sitio cuenta con rutas dinamicas en hotels y home

#### ejemplo para el home localhost:5000/ si ingresamos asi nos guiara a la ruta principal

#### ejemplo para el home localhost:5000/Felix Jimenez si ingresamos asi nos guiara a la ruta principal, con nuestra bienvenida en la seccion de el hero home

#### si ingresamos a localhost:5000/hotels/nombre-del-hotel nos giara a hotel especificado, tambien podemos ingresar a la seccion de hotel, directamente desde la card hotel impresas en el home y en la tag hotels.
