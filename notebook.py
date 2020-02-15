# -*- coding: utf-8 -*-
"""notebook.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10RA9JXSN1cGUI6FU_f693EK4H93ZzCu2

## **1. The brief**
<p>Imagine working for a digital marketing agency, and the agency is approached by a massive online retailer of furniture. They want to test our skills at creating large campaigns for all of their website. We are tasked with creating a prototype set of keywords for search campaigns for their sofas section. The client says that they want us to generate keywords for the following products: </p>
<ul>
<li>sofas</li>
<li>convertible sofas</li>
<li>love seats</li>
<li>recliners</li>
<li>sofa beds</li>
</ul>
<p><strong>The brief</strong>: The client is generally a low-cost retailer, offering many promotions and discounts. We will need to focus on such keywords. We will also need to move away from luxury keywords and topics, as we are targeting price-sensitive customers. Because we are going to be tight on budget, it would be good to focus on a tightly targeted set of keywords and make sure they are all set to exact and phrase match.</p>
<p>Based on the brief above we will first need to generate a list of words, that together with the products given above would make for good keywords. Here are some examples:</p>
<ul>
<li>Products: sofas, recliners</li>
<li>Words: buy, prices</li>
</ul>
<p>The resulting keywords: 'buy sofas', 'sofas buy', 'buy recliners', 'recliners buy',
          'prices sofas', 'sofas prices', 'prices recliners', 'recliners prices'.</p>
<p>As a final result, we want to have a DataFrame that looks like this: </p>
<table>
<thead>
<tr>
<th>Campaign</th>
<th>Ad Group</th>
<th>Keyword</th>
<th>Criterion Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>Campaign1</td>
<td>AdGroup_1</td>
<td>keyword 1a</td>
<td>Exact</td>
</tr>
<tr>
<td>Campaign1</td>
<td>AdGroup_1</td>
<td>keyword 1a</td>
<td>Phrase</td>
</tr>
<tr>
<td>Campaign1</td>
<td>AdGroup_1</td>
<td>keyword 1b</td>
<td>Exact</td>
</tr>
<tr>
<td>Campaign1</td>
<td>AdGroup_1</td>
<td>keyword 1b</td>
<td>Phrase</td>
</tr>
<tr>
<td>Campaign1</td>
<td>AdGroup_2</td>
<td>keyword 2a</td>
<td>Exact</td>
</tr>
<tr>
<td>Campaign1</td>
<td>AdGroup_2</td>
<td>keyword 2a</td>
<td>Phrase</td>
</tr>
</tbody>
</table>
<p>The first step is to come up with a list of words that users might use to express their desire in buying low-cost sofas.</p>
"""

# List of words to pair with products
words = ['buy', 'price', 'discount', 'promotion', 'promo', 'shop']

# Print list of words
print(words)

"""## 2. Combine the words with the product names
<p>We will translate campaign briefs into Python data structures.</p>

<p>Now that we have brainstormed the words that work well with the brief that we received, it is now time to combine them with the product names to generate meaningful search keywords. We want to combine every word with every product once before, and once after, as seen in the example above.</p>

<p>As a quick reminder, for the product 'recliners' and the words 'buy' and 'price' for example, we would want to generate the following combinations: </p>
<p>buy recliners<br>
recliners buy<br>
price recliners<br>
recliners price<br>
...  </p>
<p>and so on for all the words and products that we have.</p>
"""

products = ['sofas', 'convertible sofas', 'love seats', 'recliners', 'sofa beds']

# Create an empty list
keywords_list = []

# Loop through products
for product in products:
    # Loop through words
    for word in words:
        # Append combinations
        keywords_list.append([product, product + ' ' + word])
        keywords_list.append([product, word + ' ' + product])
        
# Inspect keyword list
from pprint import pprint
pprint(keywords_list)

"""## 3. Convert the list of lists into a DataFrame
<p>Now we want to convert this list of lists into a DataFrame so we can easily manipulate it and manage the final output.</p>
"""

#Load library
import pandas as pd

# Create a DataFrame from list
keywords_df = pd.DataFrame.from_records(keywords_list)

# Print the keywords DataFrame to explore it
keywords_df.head()

"""## 4. Rename the columns of the DataFrame
<p>Before we can upload this table of keywords, we will need to give the columns meaningful names. If we inspect the DataFrame we just created above, we can see that the columns are currently named <code>0</code> and <code>1</code>. <code>Ad Group</code> (example: "sofas") and <code>Keyword</code> (example: "sofas buy") are much more appropriate names.</p>
"""

# Rename the columns of the DataFrame
keywords_df = keywords_df.rename(columns={0: 'Ad Group', 1: 'Keyword'})

"""## 5. Add a campaign column
<p>Now we need to add some additional information to our DataFrame. 
We need a new column called <code>Campaign</code> for the campaign name. We want campaign names to be descriptive of our group of keywords and products, so let's call this campaign 'SEM_Sofas'.</p>
"""

# Add a campaign column
keywords_df['Campaign'] = 'SEM_Sofas'

"""## 6. Create the match type column
<p>There are different keyword match types. One is exact match, which is for matching the exact term or are close variations of that exact term. Another match type is broad match, which means ads may show on searches that include misspellings, synonyms, related searches, and other relevant variations.</p>
<p>Straight from Google's AdWords <a href="https://support.google.com/google-ads/answer/2497836?hl=en">documentation</a>:</p>
<blockquote>
  <p>In general, the broader the match type, the more traffic potential that keyword will have, since your ads may be triggered more often. Conversely, a narrower match type means that your ads may show less often—but when they do, they’re likely to be more related to someone’s search.</p>
</blockquote>
<p>Since the client is tight on budget, we want to make sure all the keywords are in exact match at the beginning.</p>
"""

# Add a criterion type column
keywords_df['Criterion Type'] = 'Exact'

"""## 7. Duplicate all the keywords into 'phrase' match
<p>The great thing about exact match is that it is very specific, and we can control the process very well. The tradeoff, however, is that:  </p>
<ol>
<li>The search volume for exact match is lower than other match types</li>
<li>We can't possibly think of all the ways in which people search, and so, we are probably missing out on some high-quality keywords.</li>
</ol>
<p>So it's good to use another match called <em>phrase match</em> as a discovery mechanism to allow our ads to be triggered by keywords that include our exact match keywords, together with anything before (or after) them.</p>
<p>Later on, when we launch the campaign, we can explore with modified broad match, broad match, and negative match types, for better visibility and control of our campaigns.</p>
"""

# Make a copy of the keywords DataFrame
keywords_phrase = keywords_df.copy()

# Change criterion type match to phrase
keywords_phrase['Criterion Type']='Phrase'

# Append the DataFrames
keywords_df_final = keywords_df.append(keywords_phrase)
pprint(keywords_df_final)

"""## 8. Save and summarize!
<p>To upload our campaign, we need to save it as a CSV file. Then we will be able to import it to AdWords editor or BingAds editor. There is also the option of pasting the data into the editor if we want, but having easy access to the saved data is great so let's save to a CSV file!</p>
<p>Looking at a summary of our campaign structure is good now that we've wrapped up our keyword work. We can do that by grouping by ad group and criterion type and counting by keyword. This summary shows us that we assigned specific keywords to specific ad groups, which are each part of a campaign. In essence, we are telling Google (or Bing, etc.) that we want any of the words in each ad group to trigger one of the ads in the same ad group. Separately, we will have to create another table for ads, which is a task for another day and would look something like this:</p>
<table>
<thead>
<tr>
<th>Campaign</th>
<th>Ad Group</th>
<th>Headline 1</th>
<th>Headline 2</th>
<th>Description</th>
<th>Final URL</th>
</tr>
</thead>
<tbody>
<tr>
<td>SEM_Sofas</td>
<td>Sofas</td>
<td>Looking for Quality Sofas?</td>
<td>Explore Our Massive Collection</td>
<td>30-day Returns With Free Delivery Within the US. Start Shopping Now</td>
<td>DataCampSofas.com/sofas</td>
</tr>
<tr>
<td>SEM_Sofas</td>
<td>Sofas</td>
<td>Looking for Affordable Sofas?</td>
<td>Check Out Our Weekly Offers</td>
<td>30-day Returns With Free Delivery Within the US. Start Shopping Now</td>
<td>DataCampSofas.com/sofas</td>
</tr>
<tr>
<td>SEM_Sofas</td>
<td>Recliners</td>
<td>Looking for Quality Recliners?</td>
<td>Explore Our Massive Collection</td>
<td>30-day Returns With Free Delivery Within the US. Start Shopping Now</td>
<td>DataCampSofas.com/recliners</td>
</tr>
<tr>
<td>SEM_Sofas</td>
<td>Recliners</td>
<td>Need Affordable Recliners?</td>
<td>Check Out Our Weekly Offers</td>
<td>30-day Returns With Free Delivery Within the US. Start Shopping Now</td>
<td>DataCampSofas.com/recliners</td>
</tr>
</tbody>
</table>
<p>Together, these tables get us the sample <strong>keywords -> ads -> landing pages</strong> mapping shown in the diagram below.</p>
<p><img src="https://assets.datacamp.com/production/project_400/img/kwds_ads_lpages.png" alt="Keywords-Ads-Landing pages flow"></p>
"""

# Save the final keywords to a CSV file
keywords_df_final.to_csv("final_keywords.csv")
# View a summary of our campaign work
summary = keywords_df_final.groupby(['Ad Group', 'Criterion Type'])['Keyword'].count()
print(summary)