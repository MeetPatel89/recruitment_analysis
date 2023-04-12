import pandas as pd
import numpy as np
import datetime 
import config 

# get module variables
ROOT_DIR = config.ROOT_DIR

student_grades = pd.read_csv(rf"{ROOT_DIR}\data\student_grades.csv")


# relative frequency table for Categorical Variable Status
print(student_grades.loc[:, ["Status"]].value_counts(normalize=True).to_frame(name="Relative Frequency").reset_index())