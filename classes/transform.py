import pandas as pd
from datetime import datetime

class Transform:
    def __init__(self, df):
        self.df = df
    def transform_value_and_add_audit_column(self):
        # Convertir la columna 'valor' de string a float y formatear con dos decimales
        self.df['valor'] = self.df['valor'].astype(float).round(2)
        # Añadir columna de auditoría con la fecha y hora actual para cada registro
        self.df['fecha_auditoria'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return self.df