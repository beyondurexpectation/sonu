import streamlit as st
import pandas as pd
data=pd.read_excel(r"Rhimjhim.xlsx")

new_data=st.experimental_data_editor(data,num_rows="dynamic")


final_data=pd.DataFrame(new_data)
final_data["Order Qty(MT)"]=final_data["Order Qty(MT)"].astype(str).astype(int)
final_data["Dispatch Qty(MT)"]=final_data["Dispatch Qty(MT)"].astype(str).astype(int)

final_data["Pending Qty"]=(final_data["Order Qty(MT)"])-(final_data["Dispatch Qty(MT)"])
st.write(final_data)




