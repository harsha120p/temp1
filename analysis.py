#import libraries
import pandas as pd
import os
import matplotlib.pyplot as plt

#TASK 1: there are 12 csv files and we need to merge those csv files in a single file=------------------------------------------

# df = pd.read_csv(r"C:\python\learning\pandas project\Pandas-data-Science-Tasks-master\Pandas-data-Science-Tasks-master\SalesAnalysis\Sales_Data\Sales_April_2019.csv")
# print(df.head())#to read just one file
data = pd.DataFrame()
files= [file for file in os.listdir(r"C:\python\learning\pandas project\Pandas-data-Science-Tasks-master\Pandas-data-Science-Tasks-master\SalesAnalysis\Sales_Data")]

for file in files:
    df = pd.read_csv("C:\python\learning\pandas project\Pandas-data-Science-Tasks-master\Pandas-data-Science-Tasks-master\SalesAnalysis\Sales_Data/"+file)
    data = pd.concat([data,df])
    
data.to_csv("data12months.csv", index= False)
# print(data.head())

new_data = pd.read_csv("C:\python\learning\data12months.csv")

#CLEANING THE DATA

#DROPS ROWS OF NAN
nan_df = new_data[new_data.isna().any(axis  =1)]
new_data = new_data.dropna(how= "all")

#REMOVING "OR" (ERROR WE GET FOR CONVERT STR TO INT) AND REMOVING IT
new_data = new_data[new_data["Order Date"].str[0:2]!="Or"]

#CONVERT COLUMSN TO CORRECT TYPE
new_data["Quantity Ordered"]  = pd.to_numeric(new_data["Quantity Ordered"])
new_data["Price Each"]= pd.to_numeric(new_data["Price Each"])
#--------------------------------------------------------------------------------------------------
#QUESTION 1: WHAT WAS THE BEST MONTH OF SALES AND HOW  MUCH MONEY WAS EARNED IN THAT  MONTH 
 
# augment column for month
new_data["month"] = new_data["Order Date"].str[0:2]
new_data["month"] = new_data["month"].astype("int64")#to convert string into integer
# # print(new_data.head())

# add a sales column
new_data["sales"]= new_data["Quantity Ordered"]*new_data["Price Each"]
# # print(new_data.head())

# to figure out best month sales
#results= new_data.groupby("month").sum()
# print(results [ "sales"])

# to make a bar graph to visualize the data
# months = range(1,13)
# plt.bar(months, results["sales"])
# plt.yticks([1000000,2000000,3000000,4000000,5000000])
# plt.show()


#=======================================================================================================
#   QUESTION 2: WHAT CITY HAD THE HGIGHEST NUMBER OF SALES

#we notice that the city in "Purchse address " are btw 2 ","

#add a city column BY USING THE .APPLY()

# def get_city(x):
#     return x.split(",")[1]

# def get_state(x):
#     return x.split(",")[2].split(" ")[1]


# new_data["city"]= new_data["Purchase Address"].apply(lambda x: get_city(x)+","+ get_state(x))
# print(new_data.head())

# temp = new_data.groupby("city").sum()
# print(temp["sales"])

# cities = [ city for city, df in new_data.groupby("city")]
# plt.bar(cities, temp["sales"])
# plt.yticks([1000000,2000000,3000000,4000000,5000000])
# plt.show()

#==========================================================================================================
#QUESTION 3: AT WHAT TIME SHOULD WE DISPLAY THE ADS TO MAXIMIZE LIKELIHOOD OF CUSTOMERS BUYING PRODUCTS

# new_data ["Order Date"]= pd.to_datetime(new_data["Order Date"])#to convert the dtype of "order date " to datetime type
# # print(new_data.head())

# new_data["hour"] = new_data["Order Date"].dt.hour
# new_data["minute"] = new_data["Order Date"].dt.minute

#print(new_data.head())

# hours = [ hour for hour, df in new_data.groupby("hour")]
# plt.plot(hours, new_data.groupby(["hour"]).count() )
# plt.grid()
# plt.show()

#=================================================================================================
#   QUESTION 4: WHAT PRODUCTS ARE OFTEN SOLD TOGETHER?

#same order id will have been bought together

# hp = new_data[new_data["Order ID"].duplicated(keep = False)]
# # print(hp.head(20))

# hp["grouped"]= hp.groupby("Order ID")["Product"].transform(lambda x: ",".join(x))
# hp = hp[["Order ID","grouped"]].drop_duplicates()

# print(hp.head(10))

#IMPORTANT GROUPING PAIRS
#to read the grouped pairs and count them, we need to import a few libraries and their tools
# from itertools import combinations 
# from collections import Counter

# count  = Counter()
# for row in hp["grouped"]:
#     row_list = row.split(",")
#     count.update(Counter(combinations(row_list,2)))#for pairs   #for combination

# for key,value in count.most_common(10):
#     print(key,value)
    

#===============================================================================
#QUESTION 5: WHAT PRODUCT SOLD THE MOST? WHY DO YOU THINK IT SOLD THE MOST

# product_grp = new_data.groupby("Product")
# quantity = product_grp.sum()["Quantity Ordered"]

# print(product_grp["Quantity Ordered"].sum())

#LEFT PLOTTING GRAPH, IF REQUIRED THEN GO BACK TO THE VIDEO 1:18:00
# products= [product in product, df in product_grp]
# plt.bar(products, quantity)
# plt.show()