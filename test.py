import numpy as np
import pandas as pd

market_comp = pd.read_excel('./assets/Case.xlsx', sheet_name='Market - Companies')
portfolio_comp = pd.read_excel('./assets/Case.xlsx', sheet_name='Portfolio - Companies')
portfolio_loans = pd.read_excel('./assets/Case.xlsx', sheet_name='Portfolio - Loans')

# pd.DataFrame.sort_values(market_comp, by='emissions[tCO2/year]', ascending=True)
merged = pd.DataFrame.merge(portfolio_comp, portfolio_loans, left_on='loan_id', right_on='id')
del merged['company_id']
del merged['loan_id']
del merged['id']
merged = pd.DataFrame.merge(merged, market_comp, left_on='company_name', right_on='name')
print(merged)
print(merged.columns)

pd.DataFrame.to_excel(merged, './assets/Portfolio.xlsx')