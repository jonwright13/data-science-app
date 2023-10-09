import pandas as pd

class interrogate_single_dataset:

    describe_params = {'percentiles': None, 'include': None, 'exclude': None}
    cardinality_limit = 10

    def __init__(self, df):

        self.data = df

        # Get shape of the dataframe (rows, columns)
        self.shape = df.shape

        # Get statistical info on dataframe
        self.stats = pd.DataFrame(df.describe(**self.describe_params))

        # Get lists of feature names from the dataset
        self.columns = {
            'Numerical': [col for col in df.columns if df[col].dtype in ['int64', 'float64']],
            'Object': [col for col in df.columns if df[col].dtype == 'object'],
            'Categorical': [col for col in df.columns if df[col].nunique() < self.cardinality_limit and df[col].dtype == "object"],
            'High Cardinal': [col for col in df.columns if df[col].nunique() > self.cardinality_limit and df[col].dtype == "object"],
        }

        self.table = self.column_table(df)


    def column_table(self, df, cardinality_limit=10):
    
        '''
        Method takes 2 parameters (1 required and 2 optional) and creates a visually pleasing table using the PrettyTable package
        that displays all columns, datatypes, non-null/null counts, and whether cardinality is high
        Params:
            ► df (DataFrame) | Pandas DataFrame
            ► cardinality_limit (int) | Integer representing the limit for considering a column to have high cardinality. Default = 10 items
        Return:
            ► Pandas Dataframe
        '''

        col_name = []
        data_type = []
        non_null_count = []
        missing_count = []
        uniques = []
        cardinality = []

        for column in df.columns:
            col_name.append(column)
            data_type.append(str(df[column].dtype))
            non_null_count.append(df[column].count())
            missing_count.append(df.shape[0] - df[column].count())
            uniques.append(df[column].nunique())
            cardinality.append(df[column].nunique() > self.cardinality_limit)

        return pd.DataFrame({
            "column_name": col_name,
            "column_type": data_type,
            "non_null_count": non_null_count,
            "missing_count": missing_count,
            "unique_count": uniques,
            "high_cardinality": cardinality
        })
    
    def show_uniques(self, column):
        return self.data[column].unique()
            

    