# 📊 GDP Growth Analysis: Non-Communist, Post-Communist, and Post-Soviet Countries

This project analyzes GDP growth trends for three distinct country categories across Europe:

- **Non-Communist** (blue)  
- **Post-Communist** (orange)  
- **Post-Soviet** (red)

The data provides insights into GDP performance over time for these countries.

## About the Dataset:
The full dataset can be found here: [Global Economy Indicators Dataset](https://www.kaggle.com/datasets/prasad22/global-economy-indicators).

I used Python Pandas to filter and clean the dataset, and further data manipulation was done in PostgreSQL.

## 🌍 Visualizations & Components

- **Custom map** to visualize the map of Europe, including ex-Soviet states.

Countries are color-coded:  
- Blue → Non-Communist  
- Orange → Post-Communist  
- Red → Post-Soviet  

- **Pie chart** to visualize the distribution of total GDP.  
- **Line graph** to assist in time series analysis.  
- **3 KPI cards** for each country category.

We also have the option to filter the dataset using a slicer.  
**Available time period:** 1970-2021.

**Note:** The ex-Soviet countries (Kazakhstan, Belarus) do not have data before 1990 because they were part of the Soviet Union.

## Observations and Examples
![Model](https://github.com/tibr39/gdpgrowth/blob/main/dashboardpic.png)
We can see that GDP growth (in %) was most notable in countries that were under communist rule or part of the Soviet Union. The collapse of the Soviet Union resulted in a more free economy. This rapid economic development was most noticeable where the total GDP was already at low levels before 1990. In conclusion, the collapse of the Soviet Union and its closed market caused rapid GDP growth in the Eastern Bloc countries.

Furthermore, the total sum of GDP is not distributed evenly. We can see that the Western countries' total GDP takes up **83.11%**, which is three-quarters of the aggregated GDP sum in the dataset. We can clearly see the differences between Eastern and Western Europe here and draw a line between the two blocks based solely on GDP growth.

### Example: Ukraine - Romania - Germany
![Model](https://github.com/tibr39/gdpgrowth/blob/main/ukraine_romania_germanu_ex.png)
To demonstrate the dashboard, I will use its filtering features. I selected three countries from each category: Ukraine from the ex-Soviet bloc (as it was part of the Soviet Union), Romania from the Post-Communist bloc (since it had a communist regime before 1990), and Germany, because it is considered the economic powerhouse of Europe. Germany is a special case since it was divided during the communist regime, but our year filter is set to 1990 and 2021, after the fall of the Berlin Wall, and it includes the German reunification in 1990.

We can clearly see in the line graph that the two Eastern Bloc countries' total GDPs are more unstable, with structural breaks in the series. However, Germany's total GDP doesn't show much deviation. We can clearly see when Romania joined the European Union because, after that year, it started to overtake Ukraine's total GDP.

Regarding GDP distribution, we can say the same as in the general observations: the Non-Communist countries' total GDP surpasses the other two.

Ukraine's GDP growth (in %) is the highest, which is also the result of the fact that after the collapse of the Soviet Union Ukraine witnessed a high economic growth compared to more developed economies.


## This analysis was performed using:

- **Visualization tools:** Power BI  
- **Data sources:** Kaggle  
- **Programming tools:** PyCharm  
- **Data stored in:** PostgreSQL  

