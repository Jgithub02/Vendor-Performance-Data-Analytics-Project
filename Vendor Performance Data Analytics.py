import pandas as pd 
import os 
from sqlalchemy import create_engine
engine = create_engine('sqlite:///:inventry.db')
for file in os.listdir(r'C:\Users\Jitendra\OneDrive\Desktop\Venders'):
    print(file)



