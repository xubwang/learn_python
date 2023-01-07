import pandas as pd
# import os

################################
## adidas market share report ##
################################

# read data from csv file
# os.chdir('../learn_python/data')
df = pd.read_csv("../learn_python/data/result_5.csv") #py file locates in learn_python folder

# drop rows where column 'focus_group' is na
df = df.dropna(axis=0,subset='FOCUS_GROUP')

# add subtotals
# pivot focus_group to column
df_piv = df.pivot_table(index=['COUNTRY','PRODUCT_GENDER_CLUSTER','MAIN_CATEGORY_CLUSTER']
                      , columns='FOCUS_GROUP'
                      , values='GMV_BEFORE_RETURN'
                      , aggfunc='sum')
df_piv = df_piv.reset_index()

# subtotal for gender+category - remove country
df_sub_1 = df_piv.groupby(['PRODUCT_GENDER_CLUSTER','MAIN_CATEGORY_CLUSTER'], as_index=False).sum()
df_sub_1['COUNTRY'] = 'TOT'
df_final = pd.concat([df_piv,df_sub_1])

# subtotal for country+gender - remove category
df_sub_2 = df_final.groupby(['COUNTRY','PRODUCT_GENDER_CLUSTER'], as_index=False).sum()
df_sub_2['MAIN_CATEGORY_CLUSTER'] = 'Subtotal'
df_final = pd.concat([df_final,df_sub_2])

# subtotal for country+category - remove gender
df_sub_3 = df_final.groupby(['COUNTRY','MAIN_CATEGORY_CLUSTER'], as_index=False).sum()
df_sub_3['PRODUCT_GENDER_CLUSTER'] = 'Subtotal'
df_final = pd.concat([df_final,df_sub_3])

# in case brand/peer has no sales at all, set zero
for value in ['Brand','Peer']:
    try:
        df_final[value].sum()
    except KeyError:
        df_final[value] = 0

# calculate market share
df_final['Market_Share'] = df_final['Brand'] / (df_final['Brand'] + df_final['Peer'])
df_mkt_share = df_final.drop(columns=['Brand','Peer'])
df_mkt_share = df_mkt_share.pivot_table(index = ['PRODUCT_GENDER_CLUSTER','MAIN_CATEGORY_CLUSTER']
                                        , columns = 'COUNTRY'
                                        , values = 'Market_Share'
                                        , aggfunc = 'sum')

# reindex columns & rows
# Countries to be considered
country_list = ['DE', 'CH', 'PL', 'NL', 'IT', 'BE', 'FR', 'ES', 'AT', 'SE', 'DK', 'FI',
                'NO', 'CZ', 'GB', 'SK', 'HR', 'SI', 'IE', 'LT', 'RO','HU', 'LV', 'EE']
# for index sequence
gender_sequence = ['WOMEN', 'MEN AND UNISEX', 'KIDS', 'Overall']
category_sequence = ['Subtotal', 'APP', 'FTW', 'ACC']
country_sequence = ['TOT'] + country_list
df_mkt_share = df_mkt_share.reindex(country_sequence, axis='columns', fill_value=0)
df_mkt_share = df_mkt_share.reindex(gender_sequence, level='PRODUCT_GENDER_CLUSTER', fill_value=0)
df_mkt_share = df_mkt_share.reindex(category_sequence, level='MAIN_CATEGORY_CLUSTER', fill_value=0)

# export to csv & store into result_dict
df_mkt_share.to_csv(f'../learn_python/deliverables/adidas_market_share.csv', index=True)