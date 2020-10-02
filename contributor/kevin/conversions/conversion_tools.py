def convert(columns): 
        for column in columns:
            if column in adj_cols:
                number_column = beer_df[column]
                unit_column = column[:-3]+'{}'.format('Unit')
                for i in range(len(number_column)):
                    if beer_df[unit_column][i] == adjdict.keys:
                        beer_df[unit_column][i] = beer_df[unit_column][i] * adjdict.value
                        return beer_df[unit_column][i]