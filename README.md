# 🧪 Evaluación Técnica: Pipeline de Datos para Machine Learning

Bienvenido a la evaluación técnica. Tu misión es construir un pipeline de procesamiento de datos completo, un paso fundamental en cualquier proyecto de **Machine Learning**. El objetivo es transformar datos bancarios crudos, dispersos en varias tablas, en un único **tablón de características (feature table)** limpio y estructurado. Este tablón será el insumo principal para entrenar un modelo predictivo.

***
## 📊 Diccionario de Datos

### `customers_large.csv` — Clientes bancarios
| Campo | Tipo | Descripción |
| :--- | :--- | :--- |
| `customer_id` | string | ID único del cliente |
| `name` | string | Nombre completo |
| `dob` | date | Fecha de nacimiento |
| `gender` | string | Género (`M`, `F`) |
| `region` | string | Región geográfica |
| `risk_profile`| string | Perfil de riesgo (`Low`, `Medium`, `High`) |

### `transactions_large.csv` — Transacciones bancarias
| Campo | Tipo | Descripción |
| :--- | :--- | :--- |
| `transaction_id` | string | ID único de la transacción |
| `customer_id` | string | ID del cliente |
| `account_id` | string | ID de cuenta utilizada |
| `transaction_date`| date | Fecha de la transacción |
| `type` | string | Tipo (`Deposit`, `Withdrawal`, `Payment`, `Transfer`) |
| `amount` | float | Monto en EUR (positivo o negativo) |
| `description` | string | Texto libre sobre el movimiento |

### `accounts_large.csv` — Tipos de cuenta
| Campo | Tipo | Descripción |
| :--- | :--- | :--- |
| `account_id` | string | ID de la cuenta |
| `account_type` | string | Tipo (`Checking`, `Savings`, `Credit Card`) |
| `currency` | string | Moneda (`EUR`) |
| `interest_rate` | float | Tasa de interés aplicada |
| `active` | string | Estado de la cuenta (`Yes`, `No`) |

***
## 🔧 Workflow y Tareas de la Evaluación

Sigue estos pasos para completar y entregar tu evaluación:

1.  **Hacer un Fork y Clonar** 🍴
    * Haz un **fork** de este repositorio a tu propia cuenta de GitHub.
    * **Clona** tu fork a tu máquina local para poder trabajar en los archivos.
        ```bash
        git clone https://github.com/NoeMelo/proyecto_analitico_test_ds_bbva.git
        ```

2.  **Completar el Código** 💻
    * Tu tarea principal es rellenar la lógica faltante en los archivos del proyecto. Busca los comentarios `# TODO:` que te guiarán. A continuación se describe la funcionalidad de cada archivo que debes completar:

    * `project/main.py`: Este es el **orquestador principal**. Se encarga de ejecutar cada paso del pipeline en el orden correcto, desde la carga de datos hasta el guardado del resultado final.

    * `project/business_logic/integration.py`: Su función es **consolidar los datos**. Aquí se deben unir las tres tablas (`customers`, `accounts`, `transactions`) para crear una vista única y completa de la información.

    * `project/business_logic/cleaning.py`: Este es el paso de **calidad de datos**. Aquí debes transformar los datos para asegurar que sean consistentes y usables: manejar nulos, convertir tipos, y estandarizar valores.

    * `project/business_logic/feature_engineering.py`: Aquí es donde **crearás valor para el modelo**. A partir de los datos limpios, generarás nuevas columnas (features) con información predictiva, como agregados y cálculos sobre el comportamiento del cliente.

3.  **Entregar la Evaluación** ✅
    * Una vez que hayas completado todo el código, haz **commit** de tus cambios y súbelos (push) a tu repositorio fork.
    * La entrega final es el **enlace a tu repositorio fork**. **No es necesario crear un Pull Request.**

***
## ▶️ Verificación Local (Opcional)

Si deseas verificar que tu código funciona correctamente antes de entregarlo, puedes ejecutar el script principal desde el directorio raíz del proyecto. Para ello, necesitarás tener `pandas` instalado.

```bash
python project/main.py
