# Reading Playstore Apps Excel File

Read the `playstore.xlsx` excel file and store it in a DataFrame.

When reading in the file, only use the columns `'App', 'Rating', 'Installs', 'Rating', 'Genres', 'Last_Updated'`

`playstore.xlsx` already has a numeric index.

Make sure `Last_Updated` is in datetime format, try do this while reading the file into the DataFrame.

`df` should only contain the top 25 observations by highest `Rating`, 5 being the highest rating. 

This files originated as a CSV from Kaggle and has been altered for this course, https://www.kaggle.com/lava18/google-play-store-apps
