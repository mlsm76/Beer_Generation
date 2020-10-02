kg_cols = ['Base Malt Amount','SpecialtyMalt1Amount','SpecialtyMalt2Amount','SpecialtyMalt1Amount']
gram_cols = ['hop1amount','hop2amount','hop3amount','hop4amount','hop5amount']
celcius_cols= ['LowTemp','HighTemp']
adj_cols = ['Adjunct1Num','Adjunct2Num','Adjunct3Num','Adjunct4Num','Adjunct5Num']
conversion_cols = kg_cols + gram_cols + celcius_cols + adj_cols


def adjunct_convert(columns_list): 
        for column in columns_list:
            if column in adj_cols:
                number_column = beer_df[column]
                unit_column = column[:-3]+'{}'.format('Unit')
                for i in range(len(number_column)):
                    if beer_df[unit_column][i] == adjdict.keys:
                        beer_df[number_column][i] = beer_df[number_column][i] * adjdict.value
                        return beer_df[unit_column][i]

def temperature_convert(columns_list):
    for column in columns_list:
        if column
def pounds_kilo_convert(columns_list):
def grams_oz_convert(columns_list):