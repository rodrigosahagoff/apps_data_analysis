#!/usr/bin/env python
# coding: utf-8
## Project: Data Analyse based on Apps Data

English:
This project runs over large datasets about apps from the Google Play and App Store.

The overgoal is to extract data and analyze informations that will help  developers to understand what type of apps are likely to attract more users.

Portuguese:
Esse projeto explora datasets sobre aplicativos do Google Play e da App Store.

O objetivo principal é extrair dados e analisar informações que ajudarão desenvolvedores a entender que tipo de aplicativos tem mais chances de atrair usuários.

## Documentation
English:
In case of any clarification needed, we can find the documentation about the data here: [Google Play](https://www.kaggle.com/lava18/google-play-store-apps) and here [App Store](https://www.kaggle.com/ramamet4/app-store-apple-data-set-10k-apps)

Portuguese:
Em caso de esclarecimentos, podemos encontrar a documentação dos dados aqui: [Google Play](https://www.kaggle.com/lava18/google-play-store-apps) e aqui [App Store](https://www.kaggle.com/ramamet4/app-store-apple-data-set-10k-apps)

# In[2]:


from csv import reader

opened_file_google = open('googleplaystore.csv')
read_file_google = reader(opened_file_google)
apps_data_google = list(read_file_google)
google_header = apps_data_google[0]
google = apps_data_google[1:]

opened_file_apple = open('AppleStore.csv')
read_file_apple = reader(opened_file_apple)
apps_data_apple = list(read_file_apple)
apple_header = apps_data_apple[0]
apple = apps_data_apple[1:]

#This function allows us to extract little "slices" or frameworks from the data we are looking at
def explore_data(dataset, start, end, rows_and_columns = False):  
    
    dataset_slice = dataset[start:end]
    
    for row in dataset_slice:
        print(row)
        print('\n')
        
    if rows_and_columns:
        print('Number of rows:', len(dataset))
        print('Number of columns:', len(dataset[0])) #if we have the length of the first row, we do have the number of columns


# In[3]:


print('Google first rows', '\n')
explore_data(google, 0, 5, rows_and_columns = True)
print('\n')
print('Apple first rows', '\n')
explore_data(apple, 0, 5, rows_and_columns = True)
print('\n')
print('Google columns', '\n', apps_data_google[0])
print('\n')
print('Apple columns', '\n', apps_data_apple[0])


# In[4]:


print('Old #10472 row:')
print(google[10472])
#Here, if we take a look at the Google columns above, we get to the conclusion
#that the row printed below jumps from 'App' to 'Rating', and ommits the 'Category'

del google[10472]
#Deleting an example of wrong data
print('\n')
print('New #10472 row:')
print(google[10472])


# ## Cleaning data
# 
# English:
# Now, we're gonna go over both of our datasets and check if there's any duplicates. If we find these duplicated information, we should take a look at it and clean it. To do that, we're gonna use the `for loop`. The main idea is to ask Python: "hey, loop through the `apps name` and check if we already have something like that in our name list"
# 
# Portuguese:
# Agora, vamos passar por ambos nossos datasets e checar se eles possuem alguma duplicata. Se encontrarmos essas informações duplicadas, devemos dar uma olhada nelas e limpa-las. Para fazer isso, nós vamos usar o `for loop`. A ideia central é perguntar para o Python: "ei, passe um loop pelos nomes dos aplicativos e veja se nós já temos algo parecido na nossa lista de nomes"

# In[5]:


def duplicates_overall(dataset):
    unique_values = []
    duplicate_values = []
    
    for row in dataset:
        name = row[0]
        
        if name in unique_values:
            duplicate_values.append(name)
        else:
            unique_values.append(name)
            
    print('Number of unique apps: ', len(unique_values))
    print('Number of duplicate apps: ', len(duplicate_values))
    print('Examples of duplicate apps: ', '\n', duplicate_values[:10])
        
duplicates_overall(google)
print('\n')
duplicates_overall(apple)


# English: so now we have a function that runs over any of our datasets and print the number of unique apps, duplicate apps and give us some of the duplicate apps names. Below, we're gonna go for a function that can print for us the duplicate rows by the name of the app, so we can analyze these rows and make sure we delete the right ones, not just randomly.
# 
# Portuguese: então agora temos uma função que passa por qualquer dos nossos datasets e mostra o número de aplicativos únicos, aplicativos duplicados, e dá alguns exemplos dos aplicativos duplicados. Abaixo, vamos tentar fazer uma função que nos mostre as linhas duplicadas pelo nome do aplicativo, para podermos analisar essas linhas e ter certeza de que excluiremos as linhas corretas, e não apenas aleatoriamente.

# In[6]:


for app in google:
    name = app[0]
    if name == 'Instagram':
        print(app)
        
#would be nice to turn this into a function, but we gotta move a little
#bit faster at this point.


# English: above we printed an example of a duplicate. However, we notice that the number of review of each one of the rows is different. That lead us to the conclusion that we should keep the one row which has the highest number of reviews, because that's probably the most recent one.
# 
# Portuguese: acima nós imprimimos o exemplo de uma duplicata. Entretanto, podemos notar que o número de *reviews* em cada uma das linhas é diferente. Isso nos leva à conclusão de que devemos manter a linha que tem o maior número de *reviews*, porque ela é provavelmente a linha com informações mais recentes.

# In[7]:


print('Expected length: ', len(google) - 1181)
#this will help us to know if our next function is evaluating the right numbers

#def duplicates_searching(dataset):

reviews_max = {}
    
for row in google:
    name = row[0]
    n_reviews = float(row[3])
        
    if name in reviews_max and reviews_max[name] < n_reviews:
        reviews_max[name] = n_reviews
    elif name not in reviews_max:
        reviews_max[name] = n_reviews

print('Dictionary length: ', len(reviews_max))

#duplicates_searching(google)


# In[8]:


data_clean = []
already_added = []

def cleaning_data(dataset):
    
    #clean = []
    #already_added = []
    
    for row in google:
        
        name = row[0]
        n_reviews = float(row[3])
        
        if (n_reviews == reviews_max[name]) and (name not in already_added):
        
            data_clean.append(row)
            already_added.append(name)
        
    return data_clean
        
google_cleaned = cleaning_data(google)


# In[9]:


def characters(string):
    
    non_ascii = 0
    
    for character in string:
    
        if ord(character) > 127:
            non_ascii += 1
            
        if non_ascii > 3:
            return False

       
    return True


print(characters('Instagram'))
print(characters('爱奇艺PPS -《欢乐颂2》电视剧热播'))
print(characters('Docs To Go™ Free Office Suite'))
print(characters('Instachat 😜'))


# In[10]:


#def characters_dataset(dataset):
    
google_english_app = []
    
for row in google_cleaned:
    name = row[0]
        
    if characters(name):
        google_english_app.append(row)

print('The length of the original dataset was: ', len(google_cleaned))
print('The length of the new list is: ', len(google_english_app))
print('Amount of rows deleted: ', len(google_cleaned) - len(google_english_app))
print('\n')
print('Here is a sample of the new list: ','\n', google_english_app[:5])
print('\n')
print('\n')


apple_english_app = []
    
for row in apple:
    name = row[1]
        
    if characters(name):
        apple_english_app.append(row)
    
    
print('The length of the original dataset was: ', len(apple))
print('The length of the new list is: ', len(apple_english_app))
print('Amount of rows deleted: ', len(apple) - len(apple_english_app))
print('\n')
print('Here is a sample of the new list: ','\n', apple_english_app[:5])


# In[11]:


google_free_apps = []
apple_free_apps = []

for row in google_english_app:
    price = row[7]
    
    if price == '0':
        google_free_apps.append(row)

print('Length of free apps: ', len(google_free_apps))        
print('Sample of free apps: ','\n', google_free_apps[:5])
print('\n')


apple_free_apps = []

for row in apple_english_app:
    price = row[4]
    
    if price == '0.0':
        apple_free_apps.append(row)
        
print('Length of free apps: ', len(apple_free_apps))        
print('Sample of free apps: ','\n', apple_free_apps[:5])


# English: so with this we finish cleaning our datasets. In this last step, we created a new list that only contains free apps. This will help us to understand what kind of free apps are more successful, and probably more profitable in the free app market. In the next step, we will begin to build on this cleaned data we now have.
# 
# Portuguese: agora nós terminamos de limpar nossos *datasets*. Nesse último passo, nós criamos uma lista que contém apenas aplicativos grátis. Isso nos ajudará a entender que tipos de aplicativos gratuitos fazem mais sucesso, e provavelmente que são mais lucrativos no mercado de aplicativos gratuitos. No próximo passo, vamos começar a construir em cima desses dados limpos que temos agora.

# ## Analyzing our data
# 
# English: the main goal of our company is to make revenue on free apps. So the plan is: 1) to build a minimal android app and add it to Google Play; 2)if things go well and people like it, it's gonna be developed; 3) if the app is profitable after six months, we will build a version for App Store.
# 
# So now we're going to dive in a little deeper in our datasets, and try to discover what app profile is more suitable for our purposes.
# 
# Portuguese: o objetivo principal da nossa companhia é criar receita em aplicativos gratuitos. Então o plano é: 1) criar um aplicativo básico e adicionar à Google Play; 2) se as coisas correrem bem e as pessoas gostarem, o aplicativo será de fato desenvolvido; 3) se o aplicativo se mostrar lucrativo nos próximos seis meses, será desenvolvida uma versão para a App Store.
# 
# Então agora vamos mergulhar um pouco mais funto nos nossos *datasets* e tentar descobrir que perfil de aplicativo se encaixa melhor nos nossos planos.

# In[12]:


def freq_table(dataset, index):
    frequency_table = {}
    total = 0
    
    for row in dataset:
        total += 1
        key = row[index]
        
        if key in frequency_table:
            frequency_table[key] = frequency_table[key] + 1
            
        else:
            frequency_table[key] = 1
            
    frequency_percentage = {}
    
    for key in frequency_table:
        
        percentage = (frequency_table[key] / total) * 100
        frequency_percentage[key] = percentage
            
    return frequency_percentage


# In[13]:


def display_table(dataset, index):
    table = freq_table(dataset, index)
    table_display = []
    for key in table:
        key_val_as_tuple = (table[key], key)
        table_display.append(key_val_as_tuple)

    table_sorted = sorted(table_display, reverse = True)
    for entry in table_sorted:
        print(entry[1], ':', entry[0])
        
print('Apple Genres: ')
display_table(apple_free_apps, -5)

print('\n')

print('Google Categories: ')
display_table(google_free_apps, 1)

print('\n')

print('Google Genres: ')
display_table(google_free_apps, 9)


# English:
# We'll try to answer some questions, so we can have an idea about what those percentages tell us. We should keep in mind we are talking about free english apps, and our conclusions apply only to this group.
# 
# **About App Store:**
# 
# What is the most common genre? What is the runner-up? What other patterns do we see? What is the general impression — are most of the apps designed for practical purposes  or more for entertainment?
# 
# ***
# 
# The most common `Prime Genre` is Games (58.16%) by far, covering more than half of the amount of free english apps. The runner-up is Entertainment (7.88%), followed by Photo & Video (4.96%), Education (3.66%) and Social Networking (3.29%).
# 
# Besides Education, which seems to be "the man in the middle" so to speak, the top rank of free english apps is composed basically by apps for entertainment like games, photo and video and social networking.
# 
# Below the Social Networking genre, the other apps share their market with other genres with percentages from 2.6% (Shopping) down to 0.12% (Catalogs).
# 
# Although Games is dominant about the amount of free english apps, it would be a mistake to imply that it also has a large number of users.
# 
# 
# **About Google Play:**
# 
# What are the most common genres? What other patterns do you see? Compare the patterns you see for the Google Play market with those you saw for the App Store market. Can you recommend an app profile based on what you found so far? Do the frequency tables you generated reveal the most frequent app genres or what genres have the most users?
# 
# ***
# 
# The most common `Categories` in Google Play are Family (18.9%), Games (9.72%) and Tools (8.46%).
# 
# This top rank is followed by the categories Business, Lifestyle and Productivity.
# 
# When it comes to `Genres`, Tools comes first (8.45%), followed by Entertainment (6.07%) and Education (5.35%).
# 
# We can see that this top rank is followed by the genres Business, Productivity and Lifestyle.
# 
# It looks like the top ranks in Play Store are more related to practical purposes like education, business, productivity and so on.
# 
# The percentage of apps in each category and genre seems to be more evenly distributed, as opposed to what we saw in App Store.
# 
# We can tell by our table what apps have the higher frequency, but we still can't recommend an app profile based on what we got so far.
# 
# **Note**
# ***
# 
# In Google Play it is hard to tell the difference between `Genres` and `Categories`. 
# 
# If we go to Google Play we can se that the Family category is filled up most with games for kids. Does that mean that games are more representative on free english apps in Google Play as well? We can't assume that. And the other categories seems to be evenly distributed. So we continue with our initial observations.
# 
# ![Image](https://camo.githubusercontent.com/9bf24b9efc3d88a3d55f5c09e314987941f0bab5/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f64712d636f6e74656e742f3335302f7079316d385f66616d696c792e706e67)

# In[14]:


rating_avarage = freq_table(apple_free_apps, -5)

for genre in rating_avarage:
    total = 0
    len_genre = 0
    
    for app in apple_free_apps:
        
        genre_app = app[-5]
        
        if genre_app == genre:
            n_ratings = float(app[5])
            total += n_ratings
            len_genre += 1
            
    result = total / len_genre
    print(genre, ': ', result)


# ## First impressions
# 
# English: now we have a nice clue of which apps profiles from App Store might be of interest of our company.
# 
# We could say that Navigation, Reference and Social Networking have more ratings per amount of apps in that genre. But what is Reference genre is all about? Navigation is probably influenced by few giant apps like Google Maps and Waze. The same occurs to Social Networking, influenced by Instagram, Facebook and others giants. So, probably other apps in this category may struggle to get users.
# 
# Following those, we have Music, Weather, Book and Finance, that may be more democratic categories to our company to get in.
# 
# So if we need to recommend some profile for our developers team, we could say the genres: Navigation, Social Networking, Music, Weather, Book and Finance.

# In[27]:


google_freq_category = freq_table(google_free_apps, 1)

for category in google_freq_category:
    total = 0
    len_category = 0
    
    for row in google_free_apps:
        
        category_app = row[1]
        
        if category_app == category:
            n_installs = row[5]
            n_installs = n_installs.replace('+', '')
            n_installs = n_installs.replace(',', '')
            total = float(n_installs)
            len_category += 1
            
    avg_n_installs = total / len_category
    
    print(category, avg_n_installs)
            


# English: when we look from the perspective of number of installs, we have a more clear idea about the path to our main goal. We can see that the category Communication and Dating have large amounts of installs. However these categroies are populated by apps like Whatsapp, Facebook Messenger, Tinder, etc. So, it would be risky to recommend a category like that. On the other hand, we can notice interesting like Libraries and Demo, Lifestyle, Beauty and News and Magazines.
