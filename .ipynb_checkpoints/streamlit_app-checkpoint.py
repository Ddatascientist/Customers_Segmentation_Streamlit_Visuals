import plotly.express as px
import streamlit as st
import pandas as pd

from func_page import (
top10_sales_bar, 
top10_selling_productline, 
wrangle, 
clustered_df, 
cluster_bargraph
)



st.title('Soyummy Customer Segmentation Dashboard')

df = wrangle('../DATA_FILES/Soyum_data.xlsx')
selected_year = st.selectbox(label='Year', 
                             options=df['Date'].dt.year.unique(), 
                             placeholder="Choose an option", 
                             index=None,)

st.header('Sales Analysis')

if selected_year != None:
  mask = df['Date'].dt.year == selected_year
  data_coy = df[mask]
  bar_2 = top10_sales_bar(data_coy)
  st.plotly_chart(bar_2)
else:
  bar_2 = top10_sales_bar(df)
  st.plotly_chart(bar_2)

if selected_year != None:
  mask = df['Date'].dt.year == selected_year
  data_coy = df[mask]
  bar_1 = top10_selling_productline(data_coy)
  st.plotly_chart(bar_1)
else:
  bar_1 = top10_selling_productline(df)
  st.plotly_chart(bar_1)
  

st.header('Customers Clusters')
cluster_visual = cluster_bargraph(clustered_df)
st.plotly_chart(cluster_visual)

cluster_dropdown = st.selectbox(label='Cluster Dropdown Menu',
                                options=clustered_df['Cluster_names_'].unique(),
                                placeholder="Choose Cluster Group",
                                index=None)
if cluster_dropdown != None:
  mask = clustered_df['Cluster_names_'] == cluster_dropdown
  df_table = clustered_df[mask]
  df_table_grp = (
      df_table
      .groupby(by='Customer_ID', as_index=False)[['Recency', 'Frequency', 'Monetary']]
      .mean()
      .sort_values(by='Recency', ascending=True)
  )
  st.dataframe(df_table_grp)
else:
  df_table_grp = (
            clustered_df
            .groupby(by='Customer_ID', as_index=False)[['Recency', 'Frequency', 'Monetary']]
            .mean()
            .sort_values(by='Recency', ascending=True)
            .head(10)
        )
  st.dataframe(df_table_grp)





