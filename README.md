# Proyecto: Experimento-2

## Descripción

El objetivo del experimento detectar si los tokens enviados por los usuarios han sido adulterados en menos de 1 segundo, garantizando que cualquier modificación en su contenido sea identificada de forma precisa. Asegurando la integridad y autenticidad de los tokens, previniendo ataques o manipulaciones no autorizadas que puedan comprometer la seguridad del sistema. ​

El punto de sensibilidad a experimentar es la integridad y autenticidad de los tokens, asegurando que cualquier alteración en su contenido sea identificada en menos de un segundo para prevenir posibles ataques o manipulaciones no autorizadas.​

## Requisitos

Antes de empezar, asegúrate de tener instalados los siguientes requisitos:

- **Python 3.x**: Si no lo tienes instalado, puedes descargarlo desde la [página oficial de Python](https://www.python.org/downloads/).

- **Entorno Virtual**: Es recomendable crear un entorno virtual para aislar las dependencias del proyecto.

  - En **Windows**:
    ```bash
    py -m venv .venv
    venv\Scripts\activate
    ```

  - En **Linux/macOS**:
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

## Instalación

### Paso 1: Clonar el repositorio

```bash
git clone https://github.com/gvillalbag94/ABCall-experimento-2.git
cd ABCall-experimento-2
```

### Paso 2: Instalar dependencias

**Instalar dependencias**: Se deben instalar las dependencias encontradas en requirements.txt.

  - En **Linux/macOS**:
    ```bash
    pip install -r requirements.txt
    ```

### Paso 3: Ejecucion de componentes

**Iniciar Api Gateway**: Este comando empezara a ejecutar el Api Gateway el cual recibira las peticiones. ¡¡Recuerde estar en la raiz del proyecto!!

```bash
cd api_gateway
flask run -p 5000
```

**Iniciar Autorizador**: Este comando empezara a ejecutar el Autorizador el cual validara la identidad y los tokens. ¡¡Recuerde estar en la raiz del proyecto!!

```bash
cd autorizador
flask run -p 5003
```

**Recomendaciones:**: 
Si tiene problemas ejecutando el experimiento consulte el siguiente video donde explica la ejecucion de los comandos y la demostracion del experimento
