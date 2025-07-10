# project/business_logic/cleaning.py

import pandas as pd
import numpy as np

class CleaningTransformer:
    """
    Transformador para la limpieza y preprocesamiento de datos.
    """
    def clean_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Realiza la limpieza de datos en el DataFrame integrado.

        Args:
            df (pd.DataFrame): El DataFrame para limpiar.

        Returns:
            pd.DataFrame: El DataFrame limpio y preprocesado.
        """
        print("🚀 Iniciando la limpieza de datos...")
        
        # 1. Convertir columnas de fecha a formato datetime
        df['transaction_date'] = pd.to_datetime(df['transaction_date'])
        df['dob'] = pd.to_datetime(df['dob'])
        
        # 2. Eliminar valores nulos críticos y montos iguales a 0
        df.dropna(subset=['customer_id', 'account_id', 'amount'], inplace=True)
        # Se eliminan transacciones con monto 0, pero se conservan montos negativos (ej. retiros)
        df = df[df['amount'] != 0].copy()
        
        # 3. Calcular la edad del cliente (usando la columna 'age' si existe, o 'dob')
        if 'age' not in df.columns:
            # Usamos la fecha actual de la simulación para consistencia
            current_date = pd.to_datetime('2025-07-10')
            df['age'] = ((current_date - df['dob']).dt.days / 365.25).astype(int)
        df.drop(columns=['dob'], inplace=True)

        # 4. Manejar la columna 'amount'. Para el modelo, puede ser útil el valor absoluto.
        # Creamos una nueva feature que podría ser usada por el modelo.
        df['amount_abs'] = df['amount'].abs()

        # 5. Mapear columna binaria 'active'
        df['active'] = df['active'].map({'Yes': 1, 'No': 0})
        
        # 6. Codificar variables categóricas usando one-hot encoding
        categorical_cols = [
            'gender', 'region', 'risk_profile', # de customers
            'type',                           # de transactions
            'account_type'                    # de accounts
        ]
        df = pd.get_dummies(df, columns=categorical_cols, prefix=categorical_cols, dtype=int)
        
        # 7. Eliminar columnas que no aportan al modelo
        df.drop(columns=['name', 'description', 'currency'], inplace=True, errors='ignore')
        
        print("✅ Limpieza de datos completada.")
        return df
