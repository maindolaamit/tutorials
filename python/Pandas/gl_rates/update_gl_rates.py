#!python

import sys
import pandas as pd
import cx_Oracle

ORACLE_CONNECT = "apps/apps2016@(DESCRIPTION=(SOURCE_ROUTE=OFF)(ADDRESS_LIST=(ADDRESS=(PROTOCOL=TCP)(HOST=ocioraebsdb7102.karmalab.net)(PORT=1535)))(CONNECT_DATA=(SID=ORADEV)(SRVR=DEDICATED)))"
orcl = cx_Oracle.connect(ORACLE_CONNECT)
print("Connected to Oracle: " + orcl.version)


def get_conv_rate(to_curr, conv_date):
    sql = """SELECT CONVERSION_RATE
  FROM gl_daily_rates
 WHERE TO_CURRENCY = 'USD'
   AND FROM_CURRENCY = :to_curr 
   AND CONVERSION_DATE = :conv_date
    """
    # print(f"Getting rate for Currency : {to_curr}")
    cur = orcl.cursor()
    try:
        cur.execute(sql, [to_curr.upper(), conv_date])
    except ex:
        print(ex)
    # Fetch only first row
    row = cur.fetchone()
    if row is not None:
        cur.close()
        # print(f"\t\t{row[0]}")
        return row[0]
    else:
        return 1


# excel_file = "Test.xlsx"
excel_file = sys.argv[1]
conv_date = str(sys.argv[2]).upper()

try:
    print(f"Reading excel file {excel_file} for Conversion date {conv_date} ...")
    df = pd.read_excel(excel_file, sheet_name="Sheet1")
except PermissionError:
    print(f"Please close the File {excel_file}.")

if df is not None:
    df_cumm = df.groupby('Currency', as_index=False).sum()
    # Loop for each Currency
    df_cumm['Conversion_Rate'] = df_cumm.apply(lambda x: get_conv_rate(x['Currency'], conv_date), axis=1)
    df_cumm['Converted_Amount'] = df_cumm['Amount'] * df_cumm['Conversion_Rate']
    # print(df_cumm.head())

    print("Writing to Excel file...")
    with pd.ExcelWriter(excel_file) as writer:
        df.to_excel(writer, sheet_name="Sheet1", index=False)
        df_cumm.to_excel(writer, sheet_name="Combined", index=False)

# close the connection
orcl.close()
