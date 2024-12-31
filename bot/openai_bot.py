#%%
import os

import pandas as pd
from pandasai import Agent, SmartDataframe
from pandasai.helpers.openai_info import get_openai_callback
from pandasai.llm import OpenAI

#%%
employees_data = {
    "EmployeeID": [1, 2, 3, 4, 5],
    "Name": ["John", "Emma", "Liam", "Olivia", "William"],
    "Department": ["HR", "Sales", "IT", "Marketing", "Finance"],
}

employees_data = pd.DataFrame(employees_data)

llm = OpenAI(model = "gpt-4")

# conversational=False is supposed to display lower usage and cost
df = SmartDataframe(employees_data, config={"llm": llm, "conversational": False, "verbose":True})

with get_openai_callback() as cb:
    response = df.chat("Department wise employee count please.")

    print(response)
    print(cb)
