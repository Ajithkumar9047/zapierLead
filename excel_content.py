from config import *
current_date = datetime.now().strftime('%d/%m/%Y')
yesterday_date = (datetime.now() - timedelta(days=1)).strftime('%d/%m/%Y')
def create_excel_file(rows_query1, rows_query2):
    current_date = datetime.now().strftime('%d/%m/%Y')

    # Find the path to pyvenv.cfg and construct the Excel file path
    venv_directory = os.path.dirname(os.path.abspath(__file__))  # Path to the script itself
    excel_file_name = os.path.join(venv_directory, f"TVS_LMS_{current_date.replace('/', '_')}.xlsx")

    wb = Workbook()
    ws_combined = wb.active
    ws_combined.title = "tvs_count"
    ws_combined.merge_cells('C1:G1')
    #ws_combined['C1'].value = f"Yesterday_count-{yesterday_date}"
    ws_combined['C1'].value = f"Zapier_count-{current_date}"
    header_combined = ["form_name", "form_id", "ems_push1", "dms_push", "crm_push", "invalid", "Total"]
    ws_combined.append(header_combined)

    sky_blue_fill = PatternFill(start_color='7EC0EE', end_color='7EC0EE', fill_type='solid')
    for cell in ws_combined['2']:
        cell.fill = sky_blue_fill

    for row1 in rows_query1:
        combined_row = list(row1)
        ws_combined.append(combined_row)

    border_style = openpyxl.styles.Side(style='thin')
    border = openpyxl.styles.Border(left=border_style, right=border_style, top=border_style, bottom=border_style)

    for row in ws_combined.iter_rows():
        for cell in row:
            cell.border = border

    wb.save(excel_file_name)
    print("Excel file updated and saved:", excel_file_name)
    return excel_file_name