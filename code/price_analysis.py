#%%
from data_preparation import dat 

#%%
(
    dat
    .query('ang_VONLAND == "AT"') # query equals filter in Pandas
    .filter(["ang_st_transportmittelcode", "ang_stp_gesamtpreis"]) # select the columns Type and Price
    .groupby("ang_st_transportmittelcode")
    .agg("mean")
    .reset_index() 
    .set_axis(["Type", "averagePrice"], axis = 1, inplace = False)
)

