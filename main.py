import pandas as pd

df = pd.read_csv('Global Economy Indicators.csv')

neighbors = [
    " Austria ", " Belgium ", " Bulgaria ", " Croatia ", " Cyprus ", " Czechia ", 
    " Denmark ", " Estonia ", " Finland ", " France ", " Germany ", " Greece ", 
    " Hungary ", " Ireland ", " Italy ", " Latvia ", " Lithuania ", " Luxembourg ", 
    " Malta ", " Netherlands ", " Poland ", " Portugal ", " Romania ", " Slovakia ", 
    " Slovenia ", " Spain ", " Sweden ", " Armenia ", " Azerbaijan ", " Belarus ", 
    " Georgia ", " Kazakhstan ", " Kyrgyzstan ", " Republic of Moldova ", 
    " Russian Federation ", " Tajikistan ", " Turkmenistan ", " Ukraine ", 
    " Uzbekistan ", " Albania ", " Bosnia and Herzegovina ", " Kosovo ", 
    " Montenegro ", " North Macedonia ", " Serbia "
]

print(df)

#firstly the idea was Romania's negihbors but i expanded the idea to the EU and Pos-Communist countries
df_new = df.loc[(df[' Country '].isin(neighbors))]

#replacing missing values
missing_values = df_new[' Country '].isnull().any()

if missing_values:
    print("There are missing countries in the column.")
else:
    print("There are no missing countries in the column.")








#renaming the countries
replacements = {
    ' Czechia ': ' Czech Republic ',
    ' Russian Federation ': ' Russia ',
    ' Cyprus ': ' Republic of Cyprus ',
    ' Republic of Moldova ': ' Moldova '
}


df_new.loc[:, ' Country '] = df_new[' Country '].replace(replacements)


#remove the spaces in the country names
df_new = df_new.rename(columns=lambda x: x.strip())

df_new.loc[:, 'Country'] = df_new.loc[:, 'Country'].apply(lambda x: x.strip())


df_new.to_csv('countriesecoindexes.csv', index=False)
