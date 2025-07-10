# project/business_logic/feature_engineering.py

import pandas as pd

class FeatureEngineeringTransformer:
    """
    Transformador para la creación de nuevas características (features).
    """
    def create_features(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Genera nuevas variables para el modelo de predicción.

        Args:
            df (pd.DataFrame): El DataFrame limpio.

        Returns:
            pd.DataFrame: El DataFrame con las nuevas características.
        """
        print("🚀 Iniciando la ingeniería de características...")
        
        # TODO: Ordena el DataFrame por 'customer_id' y 'transaction_date'.
        # Esto es crucial para que los cálculos de ventana (móviles) funcionen correctamente.
        df = 

        # 1. Total de transacciones por cliente.
        # TODO: Crea la columna 'transactions_count'. Debe contener el número total de transacciones
        # realizadas por cada cliente.
        df['transactions_count'] = 
        
        # 2. Promedio móvil del monto (absoluto) de las últimas 3 transacciones por cliente.
        # TODO: Crea la columna 'amount_abs_moving_avg_3t'. Debe ser el promedio móvil
        # de las últimas 3 transacciones de 'amount_abs' para cada cliente.
        df['amount_abs_moving_avg_3t'] = 

        # 3. Suma total de dinero movido (absoluto) por el cliente.
        # TODO: Crea la columna 'total_amount_moved'. Debe contener la suma de todos los
        # montos en 'amount_abs' para cada cliente.
        df['total_amount_moved'] = 
        
        # 4. Día de la semana y mes de la transacción.
        # TODO: Extrae el día de la semana y el mes de 'transaction_date'.
        df['day_of_week'] =  # Lunes=0, Domingo=6
        df['month_of_transaction'] = 
        
        print("✅ Ingeniería de características completada.")
        return df
