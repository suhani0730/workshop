import streamlit as st
import pandas as pd
import numpy as np
st.title('my first clould app')
st.write('Here is our first attempt at using data to create a table:')
df=pd.DataFrame(np.random.randn(10,2),columns=['col1','col2'])
st.dataframe(df)