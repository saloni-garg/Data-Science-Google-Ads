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
<ul>
<li><p>The first step is to come up with a list of words that users might use to express their desire in buying low-cost sofas.</p></li>
<li><p>Now that we have brainstormed the words that work well with the brief that we received, it is now time to combine them with the product names to generate meaningful search keywords. We want to combine every word with every product once before, and once after, as seen in the example above.</p></li>
<li><p>Now we want to convert this list of lists into a DataFrame so we can easily manipulate it and manage the final output.</p></li>
<li><p>Before we can upload this table of keywords, we will need to give the columns meaningful names. If we inspect the DataFrame we just created above, we can see that the columns are currently named <code>0</code> and <code>1</code>. <code>Ad Group</code> (example: "sofas") and <code>Keyword</code> (example: "sofas buy") are much more appropriate names.</p></li>
<li><p>Now we need to add some additional information to our DataFrame. 
We need a new column called <code>Campaign</code> for the campaign name. We want campaign names to be descriptive of our group of keywords and products, so let's call this campaign 'SEM_Sofas'.</p></li>
<li><p>To upload our campaign, we need to save it as a CSV file. Then we will be able to import it to AdWords editor or BingAds editor. There is also the option of pasting the data into the editor if we want, but having easy access to the saved data is great so let's save to a CSV file!</p></li>
