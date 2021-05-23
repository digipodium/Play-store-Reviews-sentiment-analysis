import streamlit as st
import pandas as pd

from analyze import Analyse

st.title('Play Store Reviews Sentiments Analysis')
st.image('1.png')


def viewDataset(path):
    st.write('Dataset Used in Project')
    analysis = Analyse(path)
    dataframe = analysis.getDataframe()

    with st.spinner("Loading Data..."):
        st.dataframe(dataframe)

        st.markdown('---')
        cols = st.beta_columns(4)
        cols[0].markdown("### No. of Rows :")
        cols[1].markdown(f"# {dataframe.shape[0]}")
        cols[2].markdown("### No. of Columns :")
        cols[3].markdown(f"# {dataframe.shape[1]}")
        st.markdown('---')

        st.header('Summary')
        st.dataframe(dataframe.describe())
        st.markdown('---')

        types = {'object': 'Categorical',
                 'int64': 'Numerical', 'float64': 'Numerical'}
        types = list(map(lambda t: types[str(t)], dataframe.dtypes))
        st.header('Dataset Columns')
        for col, t in zip(dataframe.columns, types):
            st.markdown(f"### {col}")
            cols = st.beta_columns(4)
            cols[0].markdown('#### Unique Values :')
            cols[1].markdown(f"# {dataframe[col].unique().size}")
            cols[2].markdown('#### Type :')
            cols[3].markdown(f"## {t}")


sidebar = st.sidebar
sidebar.header('Choose Your Option')
options = ('View Dataset', 'Analysis of Apps','Analysis of User Reviews','About')
choice = sidebar.selectbox(options= options, label= "Choose Action")

if choice == 'View Dataset':
    with st.spinner("Loading Data..."):
        st.header('Raw datasets')
        st.header('Apps Dataset')
        viewDataset(path='datasets/apps.csv')
        st.header('User Reviews Dataset')
        viewDataset(path='datasets/user_reviews.csv')
elif choice == 'Analysis of Apps':
    with st.spinner("Loading Analysis..."):
        
        st.header('Exploring app categories')
        st.write('''With more than 1 billion active users in 190 countries around the world, Google Play continues to be an important distribution platform to build a global audience. For businesses to get their apps in front of users, it's important to make them more quickly and easily discoverable on Google Play. To improve the overall search experience, Google has introduced the concept of grouping apps into categories.
                
                This brings us to the following questions:
                Which category has the highest share of (active) apps in the market?
                Is any specific category dominating the market?
                Which categories have the fewest number of apps?
                        ''')

        st.write('We will see that there are 33 unique app categories present in our dataset. Family and Game apps have the highest market prevalence. Interestingly, Tools, Business and Medical apps are also at the top.')
        st.subheader('No. of apps in each category')
        st.image('images/playstore1.png')
        
        st.header('Distribution of app ratings')
        st.write('''After having witnessed the market share for each category of apps, let's see how all these apps perform on an average. App ratings (on a scale of 1 to 5) impact the discoverability, conversion of apps as well as the company's overall brand image. Ratings are a key performance indicator of an app.

From our research, we found that the average volume of ratings across all app categories is 4.17. The histogram plot is skewed to the right indicating that the majority of the apps are highly rated with only a few exceptions in the low-rated apps.
        ''')
        st.subheader('No. of apps(y) vs rating(x)')
        st.image('images/playstore2.png')

        st.header('Size and price of an app')
        st.write('''Let's now examine app size and app price. For size, if the mobile app is too large, it may be difficult and/or expensive for users to download. Lengthy download times could turn users off before they even experience your mobile app. Plus, each user's device has a finite amount of disk space. For price, some users expect their apps to be free or inexpensive. These problems compound if the developing world is part of your target market; especially due to internet speeds, earning power and exchange rates.

How can we effectively come up with strategies to size and price our app?

Does the size of an app affect its rating?
Do users really care about system-heavy apps or do they prefer light-weighted apps?
Does the price of an app affect its rating?
Do users always prefer free apps over paid apps?
We find that the majority of top rated apps (rating over 4) range from 2 MB to 20 MB. We also find that the vast majority of apps price themselves under \$10.
        ''')

        st.subheader('Ratings(y) vs app size(x)')
        st.image('images/playstore3.png')
        st.subheader('Ratings(y) vs app price(x)')
        st.image('images/playstore4.png')

        st.header('Relation between app category and app price')
        st.write('''So now comes the hard part. How are companies and developers supposed to make ends meet? What monetization strategies can companies use to maximize profit? The costs of apps are largely based on features, complexity, and platform.

There are many factors to consider when selecting the right pricing strategy for your mobile app. It is important to consider the willingness of your customer to pay for your app. A wrong price could break the deal before the download even happens. Potential customers could be turned off by what they perceive to be a shocking cost, or they might delete an app they’ve downloaded after receiving too many ads or simply not getting their money's worth.

Different categories demand different price ranges. Some apps that are simple and used daily, like the calculator app, should probably be kept free. However, it would make sense to charge for a highly-specialized medical app that diagnoses diabetic patients. Below, we see that Medical and Family apps are the most expensive. Some medical apps extend even up to \$80! All game apps are reasonably priced below \$20.
        ''')
        st.subheader('Apps Priceing trend across categories')
        st.image('images/playstore5.png')

        st.header('Filter out "junk" apps')
        st.write('''It looks like a bunch of the really expensive apps are "junk" apps. That is, apps that don't really have a purpose. Some app developer may create an app called I Am Rich Premium or most expensive app (H) just for a joke or to test their app development skills. Some developers even do this with malicious intent and try to make money by hoping people accidentally click purchase on their app in the store.

Let's filter out these junk apps and re-do our visualization. The distribution of apps under \$20 becomes clearer.
        ''')
        st.subheader('Apps Priceing trend across categories after filtering for junk apps')
        st.image('images/playstore6.png')

        st.header('Popularity of paid apps vs free apps')
        st.write('''For apps in the Play Store today, there are five types of pricing strategies: free, freemium, paid, paymium, and subscription. Let's focus on free and paid apps only. Some characteristics of free apps are:

Free to download.
Main source of income often comes from advertisements.
Often created by companies that have other products and the app serves as an extension of those products.
Can serve as a tool for customer retention, communication, and customer service.
Some characteristics of paid apps are:

Users are asked to pay once for the app to download and use it.
The user can't really get a feel for the app before buying it.
Are paid apps are installed as much as free apps? It turns out that paid apps have a relatively lower number of installs than free apps, though the difference is not as stark as I would have expected!
        ''')
        st.subheader('Number of downloads of free vs paid apps')
        st.image('images/playstore7.png')
        st.image('images/playstore8.png')
        st.subheader('Correalation matix of apps.csv')
        st.image('images/playstore9.png')
        st.image('images/playstore10.png')
elif choice == 'Analysis of User Reviews':
    with st.spinner("Loading Analysis..."):
        st.header('Sentiment analysis of user reviews')
        st.write('''Mining user review data to determine how people feel about your product, brand, or service can be done using a technique called sentiment analysis. User reviews for apps can be analyzed to identify if the mood is positive, negative or neutral about that app. For example, positive words in an app review might include words such as 'amazing', 'friendly', 'good', 'great', and 'love'. Negative words might be words like 'malware', 'hate', 'problem', 'refund', and 'incompetent'.

By plotting sentiment polarity scores of user reviews for paid and free apps, we observe that free apps receive a lot of harsh comments, as indicated by the outliers on the negative y-axis. Reviews for paid apps appear never to be extremely negative. This may indicate something about app quality, i.e., paid apps being of higher quality than free apps on average. The median polarity score for paid apps is a little higher than free apps, thereby syncing with our previous observation.

In this notebook, we analyzed over ten thousand apps from the Google Play Store. We can use our findings to inform our decisions should we ever wish to create an app ourselves.
        ''')
        st.subheader('Sentiment analysis polarity')
        st.image('images/userReviews.png')
        st.image('images/userReviews1.png')
elif choice == 'About':
    with st.spinner("Loading Analysis..."):
        st.write('''Mobile apps are everywhere. They are easy to create and can be lucrative. Because of these two factors, more and more apps are being developed. In this notebook, we will do a comprehensive analysis of the Android app market by comparing over ten thousand apps in Google Play across different categories. We'll look for insights in the data to devise strategies to drive growth and retention.

Let's take a look at the data, which consists of two files:

apps.csv: contains all the details of the applications on Google Play. There are 13 features that describe a given app.
user_reviews.csv: contains 100 reviews for each app, [most helpful first](https://www.androidpolice.com/2019/01/21/google-play-stores-redesigned-ratings-and-reviews-section-lets-you-easily-filter-by-star-rating/). The text in each review has been pre-processed and attributed with three new features: Sentiment (Positive, Negative or Neutral), Sentiment Polarity and Sentiment Subjectivity.
        ''')