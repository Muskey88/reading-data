# Reading Playstore Apps Excel File with Multiple Sheets

Read the `playstore.xlsx` excel file and store it in a DataFrame.

You will need to use `pd.ExcelFile` for this excel file because there are multiple sheets we will be parsing.

`playstore` variable will contain the `Google_playstore` sheet in a DataFrame.

`content_id` variable will contain the `Content_ID` sheet in a DataFrame

`df` should be a combination of the two previous DataFrames, connected at the column level.

This files originated as a CSV from Kaggle and has been altered for this course, https://www.kaggle.com/lava18/google-play-store-apps
