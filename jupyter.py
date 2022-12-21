        
def positive_negative(cell):
        if type(cell) != str and cell < 0 :
                return 'color: red'
        else:
                return 'color: black'
                

set_table_styles([
{"selector":"tbody tr:nth-child(odd)","props":[("background-color","white")]},
{"selector":"tr th","props":[("border","2px solid grey")]},
{"selector":"tbody tr","props":[("border","2px solid grey")]},


.style \
.applymap(lambda slice_of_df: 'background-color: lightgrey', subset=pd.IndexSlice[:, '']) \
.bar( subset=list(.values()), color=['#FFCCCB', "lightgreen"], axis=ax) 


            