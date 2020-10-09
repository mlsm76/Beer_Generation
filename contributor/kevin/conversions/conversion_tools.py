import scipy as sp

kg_cols = [
    "Base Malt Amount",
    "SpecialtyMalt1Amount",
    "SpecialtyMalt2Amount",
    "SpecialtyMalt1Amount",
]
gram_cols = ["hop1amount", "hop2amount", "hop3amount", "hop4amount", "hop5amount"]
temperature_cols = ["LowTemp", "HighTemp"]
adj_cols = ["Adjunct1Num", "Adjunct2Num", "Adjunct3Num", "Adjunct4Num", "Adjunct5Num"]
conversion_cols = kg_cols + gram_cols + celcius_cols + adj_cols

print(kg_cols)
print(gram_cols)
print(celcius_cols)
print(adj_cols)


def adjunct_convert(columns_list):
    for column in columns_list:
        if column in adj_cols:
            number_column = beer_df[column]
            unit_column = column[:-3] + "{}".format("Unit")
            for i in range(len(number_column)):
                if beer_df[unit_column][i] == adjdict.keys:
                    beer_df[number_column][i] = (
                        beer_df[number_column][i] * adjdict.value
                    )
                    return beer_df[unit_column][i]


def temperature_convert(columns_list):
    for column in columns_list:
        if column in temperature_cols:
            for i, j in range(len(beer_df[temperature_cols])):
                beer_df[temperature_cols][i][j] = sp.constants.convert_temperature(
                    beer_df[temperature_cols][i][j], "C", "F"
                )


def pounds_kilo_convert(columns_list):
    for column in columns_list:
        if column in kg_cols:
            for i, j, k, l in range(len(beer_df[kg_cols])):
                beer_df[kg_cols][i][j][j][k] = beer_df[kg_cols][i][j][k][l] * 2.2046


def grams_oz_convert(columns_list):
    for column in columns_list:
        if column in gram_cols:
            for i, j, k, l, m in range(len(beer_df[gram_cols])):
                beer_df[kg_cols][i][j][j][k][m] = beer_df[kg_cols][i][j][k][l][m] * 1.1