# 🧪 Evaluación Técnica: Procesamiento de Datos Bancarios

Este repositorio contiene un ejercicio técnico para evaluar tus habilidades en la construcción de un pipeline de procesamiento de datos. El objetivo es completar un código preexistente para que pueda leer, integrar, limpiar y transformar un conjunto de datos bancarios.

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
        git clone [https://github.com/NoeMelo/proyecto_analitico_test_ds_bbva.git](https://github.com/NoeMelo/proyecto_analitico_test_ds_bbva.git)
        ```

2.  **Completar el Código** 💻
    * Tu tarea principal es rellenar la lógica faltante en los archivos del proyecto. Busca los comentarios `# TODO:` que te guiarán sobre qué hacer en cada sección.
    * Los archivos a modificar son:
        * `project/main.py`
        * `project/business_logic/integration.py`
        * `project/business_logic/cleaning.py`
        * `project/business_logic/feature_engineering.py`

3.  **Entregar la Evaluación** ✅
    * Una vez que hayas completado todo el código, haz **commit** de tus cambios y súbelos (push) a tu repositorio fork.
    * La entrega final es el **enlace a tu repositorio fork**. **No es necesario crear un Pull Request.**

***
## ▶️ Verificación Local (Opcional)

Si deseas verificar que tu código funciona correctamente antes de entregarlo, puedes ejecutar el script principal desde el directorio raíz del proyecto. Para ello, necesitarás tener `pandas` instalado.

```bash
python project/main.py
```
## 