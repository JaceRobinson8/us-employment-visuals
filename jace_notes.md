# Start Day 11-30-22

1. Understand the dataset more
2. Understand advanced bokeh more

### Notes on understanding dataset

Loosely my goal is to pick a hypothesis / question, use the data to support / refute the hypothesis. Try to tell an interesting story in a blog-like format, using the visuals and dataset.

So what does this dataset contain?

Crap dataset only goes to 2010... Can we find better / more recent data?

Oooohh bureau of labor statistics publishes lots of great data! https://www.bls.gov/

Lets probably focus on unemployement data? But slice it in a few ways

1. Slice of demographics, can we get enconomic brackets somehow?
2. Slice by regions / geography
3. Slice by industry

Okay great, lets start with demographics.

We can get demographic data from here https://data.bls.gov/PDQWeb/ln, there is an API but having troubles with it, so going to use this link. I am can one spreadsheet at a time. Then I can manually merge the spreadsheets for visualization in bokeh.

The basic format of the data is:

1. Value: unemployment percentage
2. Per month for last 10 years (want longer, but not super sure)
3. Different ways to slice it
   1. Sex
   2. Race/ethnicity
   3. Age
   4. Education

Employment! Ideas...

1. Something around COVID if the dataset goes to 2022? Comparing covid times to historical times
