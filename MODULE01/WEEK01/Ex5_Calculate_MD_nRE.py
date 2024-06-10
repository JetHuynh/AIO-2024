"""## 5. Viết function thực hiện Mean Difference of n^th Root Error"""
# calculate MD_nRE
def Calculate_MD_nRE( y,y_hat,n,p):
    result = ((y ** (1 / n)) - (y_hat ** (1 / n))) ** p
    print(f'MD_nRE: {result}')
    return

# RunExample
Calculate_MD_nRE(100, 99.5, 2, 1)
Calculate_MD_nRE(50, 49.5, 2, 1)
Calculate_MD_nRE(20, 19.5, 2, 1)
Calculate_MD_nRE(0.6, 0.1, 2, 1)
