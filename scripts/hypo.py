import pandas as pd
from scipy.stats import chi2_contingency,ttest_ind
def catagorical_claims(data,column):
    """
    This function uses the chi-square test to find the p-value for categorical columns.
    """
    con=pd.crosstab(data['Claimed'],data[column])
    chi,p_value,_,_=chi2_contingency(con)
    return chi,p_value,con
def numerical_claims(column1,column2):
    """
    This function calculates the p-value for numerical column using t-test
    """
    t_stat, p_value = ttest_ind(column1, column2, equal_var=False)
    return t_stat, p_value