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
conversion_cols = kg_cols + gram_cols + temperature_cols + adj_cols

print(kg_cols)
print(gram_cols)
print(temperature_cols)
print(adj_cols)


def adjunct_convert(df,columns_list):
    for column in columns_list:
        if column in adj_cols:
            number_column = df[column]
            unit_column = column[:-3] + "{}".format("Unit")
            for i in range(len(number_column)):
                if df[unit_column][i] == adjdict.keys:
                    df[number_column][i] = (
                        df[number_column][i] * adjdict.value
                    )
                    return df[unit_column][i]


def temperature_convert(df,columns_list):
    for column in columns_list:
        if column in temperature_cols:
            for i in range(len(df[temperature_cols])):
                df[temperature_cols][i] = sp.constants.convert_temperature(
                    df[temperature_cols][i], "C", "F"
                )


def pounds_kilo_convert(columns_list):
    for column in columns_list:
        if column in kg_cols:
            for i, j, k, l in range(len(df[kg_cols])):
                df[kg_cols][i][j][j][k] = df[kg_cols][i][j][k][l] * 2.2046


def grams_oz_convert(columns_list):
    for column in columns_list:
        if column in gram_cols:
            for i, j, k, l, m in range(len(df[gram_cols])):
                df[kg_cols][i][j][j][k][m] = df[kg_cols][i][j][k][l][m] * 1.1