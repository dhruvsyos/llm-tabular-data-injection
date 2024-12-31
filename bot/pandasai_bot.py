#%%
import os
import pandas as pd
from pandasai import Agent

# Sample DataFrame
#%%
df = pd.read_excel("/Users/dhruvarya_peng/Downloads/test dataset.xlsx", sheet_name="Data")

# By default, unless you choose a different LLM, it will use BambooLLM.
# You can get your free API key signing up at https://pandabi.ai (you can also configure it in your .env file)
#%%
agent = Agent(df)
agent.chat('Which company has the most employees')
agent.chat('From this dataset, please calculate the attriation rate for each company? Output as dataframe')
