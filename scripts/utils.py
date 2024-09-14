import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
class EDA():
    def __init__(self,data):
        self.data=data
    def null(self):
        null=pd.DataFrame(self.data.isnull().sum()).reset_index().rename(columns={'index':'column_name',0:'null_count'})
        null['null_count(%)']=null['null_count'].apply(lambda x:round((x/len(self.data))*100,2))
        null=null.sort_values(by='null_count',ascending=False)
        return null
    def plot_data(self,column):
        """
        This function plots the mentioned column extracted out of the data. This function plots a 
        bar chart for catagorical columns and a histogram for numerical columns.
        Parameter:
           column: this can be a catagorical or numerical column
        Returns: 
            A bar chart for Catagorical Column and a histogram for numerical column
        """
        first = self.data[column].iloc[0]
        if isinstance(first,(np.int64,np.float64)):
            plt.hist(self.data[column],bins=100,color='steelblue', edgecolor='black')
            plt.xlabel(column)
            plt.ylabel('Frequency')
            plt.title(f'The histogram plot for {column} column')
            plt.show()
        elif isinstance(first,(object,bool)):
            d=self.data[column].value_counts()
            d.plot(kind='bar',color='steelblue', edgecolor='black', linewidth=1.5)
            plt.xlabel(column)
            plt.ylabel('Frequency')
            plt.title(f"The distribution of values in {column} column")
            plt.show()
    def scatter_postalcode(self,column):
        """
        This method plots a scatterplot using the PostalCode as parameter to group

        Parameter:
            column: This column can be any column that you want to track its relationship with respect to PostalCode 
        """
        d=self.data[['PostalCode',column]].groupby('PostalCode').sum().reset_index()
        plt.scatter(x=d['PostalCode'],y=d[column],c='red')
        plt.title(f'The scatter plot of the {column} column grouped by PostalCode')
        plt.xlabel('PostalCode')
        plt.ylabel(column)
        plt.show()
    def corr(self):
        """
        This method return a heatmap correlating PostalCode, TotalClaims and TotalPremium
        """
        d=self.data[['PostalCode','TotalClaims','TotalPremium']].groupby('PostalCode').sum().reset_index()
        d= sns.heatmap(d.corr(),annot=True,cmap='coolwarm')
        return d
    def plot_province(self,column):
        """
        This method return a barchart where the data is grouped according to the unique provinces in the dataset 
        and plots the frequency of the column entered as a parameter

        Parameter:
           column: This can be a column where you want to track its change according to Province
        Returns: 
            A bar chart
        """
        first = self.data[column].iloc[0]
        if isinstance(first,(np.int64,np.float64)):
            self.data.groupby('Province')[column].sum().plot(kind='bar', stacked=True, figsize=(12, 8))
            plt.title(f'{column} Distribution by Province', fontsize=16)
            plt.xlabel('Province', fontsize=14)
            plt.ylabel('Count', fontsize=14)
            plt.legend(title=f'{column}', bbox_to_anchor=(1.05, 1), loc='upper left')
            plt.xticks(rotation=45, fontsize=12)
            plt.yticks(fontsize=12)
            plt.show()
        elif isinstance(first,object):
            self.data.groupby('Province')[column].value_counts().unstack().plot(kind='bar', stacked=True, figsize=(12, 8))
            plt.title(f'{column} Distribution by Province', fontsize=16)
            plt.xlabel('Province', fontsize=14)
            plt.ylabel('Count', fontsize=14)
            plt.legend(title=f'{column}', bbox_to_anchor=(1.05, 1), loc='upper left')
            plt.xticks(rotation=45, fontsize=12)
            plt.yticks(fontsize=12)
            plt.show()
    def plot_group(self,column):
        """
        This method groups the TotalClaims and the TotalPremium column according to a column entered as a parameter

        Parameter:
            column: A grouper used to group the Claims and the Premium
        Returns: 
            A bar chart
        """
        dr=self.data.groupby(column)[['TotalPremium','TotalClaims']].sum().reset_index()
        dr=dr.sort_values(by='TotalPremium',ascending=False)
        dr.plot(kind='bar',stacked=True,x=column)
        plt.title(f'The distribution of Total Premium and Total Claims according to {column}')


