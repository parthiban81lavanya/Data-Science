class Univariate():
    def quanqual(dataset):
        quan=[]
        qual=[]
        for ColumnName in dataset.columns:
               # print(ColumnName)
                if (dataset[ColumnName].dtype=='O'):
    #print("it is quantitative variable / column")   #numbers may be discrete or continous
                    qual.append(ColumnName)
                else:
                   # print("it is qualitative variable / column")      # Categorical data - nominal, or ordinal
                    quan.append(ColumnName)
        return quan,qual

#Find and Replace the ouliers
    def findOutlier():
        lesser=[]
        greater=[]
        
        for columnName in quan:
            if (descriptive_table.loc["min", columnName] < descriptive_table.loc["lesser", columnName]):
                lesser.append(columnName)
            if ((descriptive_table.loc["max", columnName]) >(descriptive_table.loc["greater", columnName])) :
                greater.append(columnName)
        print("lesser outlier column",lesser )
        print("greater outlier column",greater )
        return lesser,greater


    def univariate(dataset,quan):
        descriptive_table = pd.DataFrame(index=["mean","median","mode","min","Q1:25%","Q2:50%","Q3:75%","99%","Q4:100%","max","IQR","1.5Rule","lesser","greater",
                                     "skew","kurtosis","var","std"],columns=quan)
        for columnName in quan:
            descriptive_table.loc["mean", columnName] = dataset[columnName].mean()
            descriptive_table.loc["median", columnName] = dataset[columnName].median()
            descriptive_table.loc["mode", columnName] = dataset[columnName].mode()[0] 
            descriptive_table.loc["min", columnName] = dataset[columnName].min()
            descriptive_table.loc["max", columnName] = dataset[columnName].max()
            descriptive_table.loc["Q1:25%", columnName] = dataset.describe()[columnName]["25%"]
            descriptive_table.loc["Q2:50%", columnName] = dataset.describe()[columnName]["50%"]
            descriptive_table.loc["Q3:75%", columnName] = dataset.describe()[columnName]["75%"]
            descriptive_table.loc["99%", columnName] = np.percentile(dataset[columnName],99)
            descriptive_table.loc["Q4:100%", columnName] = dataset.describe()[columnName]["max"]
            descriptive_table.loc["IQR", columnName] = descriptive_table.loc["Q3:75%", columnName] - descriptive_table.loc["Q1:25%", columnName]
            descriptive_table.loc["1.5Rule", columnName] = descriptive_table.loc["IQR", columnName]*1.5
            descriptive_table.loc["lesser", columnName] = descriptive_table.loc["Q1:25%", columnName] - descriptive_table.loc["1.5Rule", columnName]
            descriptive_table.loc["greater", columnName] = descriptive_table.loc["Q3:75%", columnName] + descriptive_table.loc["1.5Rule", columnName]
            descriptive_table.loc["skew", columnName] = dataset[columnName].skew()
            descriptive_table.loc["kurtosis", columnName] = dataset[columnName].kurtosis()
            descriptive_table.loc["var", columnName] = dataset[columnName].var()
            descriptive_table.loc["std", columnName] = dataset[columnName].std()
    
        return descriptive_table
        
        