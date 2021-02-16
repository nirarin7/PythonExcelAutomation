

import pandas as pd
import numpy as np


def mergeData(MainDataEntry, SearchDataEntry):

  main_workbook = MainDataEntry
  search_workbook = SearchDataEntry
  # results_workbook = OutputDataEntry


  df_main = pd.read_excel(main_workbook)
  df_search = pd.read_excel(search_workbook)



  df_results = pd.merge(df_search, df_main[['Info','SCN', 'Content']], on = 'SCN', how = 'left')
  

  ## user decide the file name
  df_results.to_excel("OutputDataEntry.xlsx", index = False)