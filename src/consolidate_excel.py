import pandas as pd
import os

# Definir rutas
input_folder = "data"
output_file = os.path.join("output", "Consolidated_Gummy_Box.xlsx")

def consolidate_multiple_excels(input_folder, output_file):
    try:
        # Inicializar el DataFrame consolidado
        consolidated_data = pd.DataFrame()

        # Variable para controlar si ya se agregó el encabezado
        header_added = False

        # Obtener la lista de archivos Excel en la carpeta
        excel_files = [f for f in os.listdir(input_folder) if f.endswith('.xlsx')]

        if not excel_files:
            print(f"No se encontraron archivos Excel en la carpeta: {input_folder}")
            return

        for file in excel_files:
            file_path = os.path.join(input_folder, file)
            print(f"Procesando archivo: {file}...")
            
            # Leer todas las hojas del archivo actual
            excel_data = pd.ExcelFile(file_path)
            sheet_names = excel_data.sheet_names

            for sheet in sheet_names:
                print(f"  Procesando hoja: {sheet}...")
                # Leer la hoja a partir de la fila 4 (fila de encabezados)
                sheet_data = pd.read_excel(file_path, sheet_name=sheet, header=3, engine='openpyxl')
                
                # Filtrar filas con datos a partir de la columna C (columna índice 2) y desde la fila 5 en adelante
                non_empty_data = sheet_data.iloc[1:].dropna(subset=sheet_data.columns[2:], how='all')

                if not non_empty_data.empty:
                    if not header_added:
                        # Agregar el encabezado con los datos
                        consolidated_data = pd.concat([consolidated_data, non_empty_data], ignore_index=True)
                        header_added = True
                    else:
                        # Agregar solo los datos sin el encabezado
                        consolidated_data = pd.concat([consolidated_data, non_empty_data], ignore_index=True)

        # Guardar los datos consolidados en un archivo nuevo
        consolidated_data.to_excel(output_file, index=False)
        print(f"Consolidación completa. Archivo guardado en: {output_file}")
    except Exception as e:
        print(f"Error durante la consolidación: {e}")

if __name__ == "__main__":
    consolidate_multiple_excels(input_folder, output_file)
