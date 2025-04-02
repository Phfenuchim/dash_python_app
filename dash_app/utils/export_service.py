# dash_app/utils/export_service.py
import pandas as pd
import plotly.io as pio
import plotly.graph_objects as go
from datetime import datetime
import os

EXPORT_DIR = "exports"
os.makedirs(EXPORT_DIR, exist_ok=True)

def export_to_csv(df: pd.DataFrame, filename: str) -> str:
    path = os.path.join(EXPORT_DIR, f"{filename}.csv")
    df.to_csv(path, index=False)
    return path

def export_to_pdf(fig: go.Figure, filename: str) -> str:
    path = os.path.join(EXPORT_DIR, f"{filename}.pdf")
    pio.write_image(fig, path, format='pdf')
    return path
