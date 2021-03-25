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


```python
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


```


```python
print('Google first rows', '\n')
explore_data(google, 0, 5, rows_and_columns = True)
print('\n')
print('Apple first rows', '\n')
explore_data(apple, 0, 5, rows_and_columns = True)
print('\n')
print('Google columns', '\n', apps_data_google[0])
print('\n')
print('Apple columns', '\n', apps_data_apple[0])
```

    Google first rows 
    
    ['Photo Editor & Candy Camera & Grid & ScrapBook', 'ART_AND_DESIGN', '4.1', '159', '19M', '10,000+', 'Free', '0', 'Everyone', 'Art & Design', 'January 7, 2018', '1.0.0', '4.0.3 and up']
    
    
    ['Coloring book moana', 'ART_AND_DESIGN', '3.9', '967', '14M', '500,000+', 'Free', '0', 'Everyone', 'Art & Design;Pretend Play', 'January 15, 2018', '2.0.0', '4.0.3 and up']
    
    
    ['U Launcher Lite – FREE Live Cool Themes, Hide Apps', 'ART_AND_DESIGN', '4.7', '87510', '8.7M', '5,000,000+', 'Free', '0', 'Everyone', 'Art & Design', 'August 1, 2018', '1.2.4', '4.0.3 and up']
    
    
    ['Sketch - Draw & Paint', 'ART_AND_DESIGN', '4.5', '215644', '25M', '50,000,000+', 'Free', '0', 'Teen', 'Art & Design', 'June 8, 2018', 'Varies with device', '4.2 and up']
    
    
    ['Pixel Draw - Number Art Coloring Book', 'ART_AND_DESIGN', '4.3', '967', '2.8M', '100,000+', 'Free', '0', 'Everyone', 'Art & Design;Creativity', 'June 20, 2018', '1.1', '4.4 and up']
    
    
    Number of rows: 10841
    Number of columns: 13
    
    
    Apple first rows 
    
    ['284882215', 'Facebook', '389879808', 'USD', '0.0', '2974676', '212', '3.5', '3.5', '95.0', '4+', 'Social Networking', '37', '1', '29', '1']
    
    
    ['389801252', 'Instagram', '113954816', 'USD', '0.0', '2161558', '1289', '4.5', '4.0', '10.23', '12+', 'Photo & Video', '37', '0', '29', '1']
    
    
    ['529479190', 'Clash of Clans', '116476928', 'USD', '0.0', '2130805', '579', '4.5', '4.5', '9.24.12', '9+', 'Games', '38', '5', '18', '1']
    
    
    ['420009108', 'Temple Run', '65921024', 'USD', '0.0', '1724546', '3842', '4.5', '4.0', '1.6.2', '9+', 'Games', '40', '5', '1', '1']
    
    
    ['284035177', 'Pandora - Music & Radio', '130242560', 'USD', '0.0', '1126879', '3594', '4.0', '4.5', '8.4.1', '12+', 'Music', '37', '4', '1', '1']
    
    
    Number of rows: 7197
    Number of columns: 16
    
    
    Google columns 
     ['App', 'Category', 'Rating', 'Reviews', 'Size', 'Installs', 'Type', 'Price', 'Content Rating', 'Genres', 'Last Updated', 'Current Ver', 'Android Ver']
    
    
    Apple columns 
     ['id', 'track_name', 'size_bytes', 'currency', 'price', 'rating_count_tot', 'rating_count_ver', 'user_rating', 'user_rating_ver', 'ver', 'cont_rating', 'prime_genre', 'sup_devices.num', 'ipadSc_urls.num', 'lang.num', 'vpp_lic']



```python
print('Old #10472 row:')
print(google[10472])
#Here, if we take a look at the Google columns above, we get to the conclusion
#that the row printed below jumps from 'App' to 'Rating', and ommits the 'Category'

del google[10472]
#Deleting an example of wrong data
print('\n')
print('New #10472 row:')
print(google[10472])
```

    Old #10472 row:
    ['Life Made WI-Fi Touchscreen Photo Frame', '1.9', '19', '3.0M', '1,000+', 'Free', '0', 'Everyone', '', 'February 11, 2018', '1.0.19', '4.0 and up']
    
    
    New #10472 row:
    ['osmino Wi-Fi: free WiFi', 'TOOLS', '4.2', '134203', '4.1M', '10,000,000+', 'Free', '0', 'Everyone', 'Tools', 'August 7, 2018', '6.06.14', '4.4 and up']


## Cleaning data

English:
Now, we're gonna go over both of our datasets and check if there's any duplicates. If we find these duplicated information, we should take a look at it and clean it. To do that, we're gonna use the `for loop`. The main idea is to ask Python: "hey, loop through the `apps name` and check if we already have something like that in our name list"

Portuguese:
Agora, vamos passar por ambos nossos datasets e checar se eles possuem alguma duplicata. Se encontrarmos essas informações duplicadas, devemos dar uma olhada nelas e limpa-las. Para fazer isso, nós vamos usar o `for loop`. A ideia central é perguntar para o Python: "ei, passe um loop pelos nomes dos aplicativos e veja se nós já temos algo parecido na nossa lista de nomes"


```python
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
```

    Number of unique apps:  9659
    Number of duplicate apps:  1181
    Examples of duplicate apps:  
     ['Quick PDF Scanner + OCR FREE', 'Box', 'Google My Business', 'ZOOM Cloud Meetings', 'join.me - Simple Meetings', 'Box', 'Zenefits', 'Google Ads', 'Google My Business', 'Slack']
    
    
    Number of unique apps:  7197
    Number of duplicate apps:  0
    Examples of duplicate apps:  
     []


English: so now we have a function that runs over any of our datasets and print the number of unique apps, duplicate apps and give us some of the duplicate apps names. Below, we're gonna go for a function that can print for us the duplicate rows by the name of the app, so we can analyze these rows and make sure we delete the right ones, not just randomly.

Portuguese: então agora temos uma função que passa por qualquer dos nossos datasets e mostra o número de aplicativos únicos, aplicativos duplicados, e dá alguns exemplos dos aplicativos duplicados. Abaixo, vamos tentar fazer uma função que nos mostre as linhas duplicadas pelo nome do aplicativo, para podermos analisar essas linhas e ter certeza de que excluiremos as linhas corretas, e não apenas aleatoriamente.


```python
for app in google:
    name = app[0]
    if name == 'Instagram':
        print(app)
        
#would be nice to turn this into a function, but we gotta move a little
#bit faster at this point.
```

    ['Instagram', 'SOCIAL', '4.5', '66577313', 'Varies with device', '1,000,000,000+', 'Free', '0', 'Teen', 'Social', 'July 31, 2018', 'Varies with device', 'Varies with device']
    ['Instagram', 'SOCIAL', '4.5', '66577446', 'Varies with device', '1,000,000,000+', 'Free', '0', 'Teen', 'Social', 'July 31, 2018', 'Varies with device', 'Varies with device']
    ['Instagram', 'SOCIAL', '4.5', '66577313', 'Varies with device', '1,000,000,000+', 'Free', '0', 'Teen', 'Social', 'July 31, 2018', 'Varies with device', 'Varies with device']
    ['Instagram', 'SOCIAL', '4.5', '66509917', 'Varies with device', '1,000,000,000+', 'Free', '0', 'Teen', 'Social', 'July 31, 2018', 'Varies with device', 'Varies with device']


English: above we printed an example of a duplicate. However, we notice that the number of review of each one of the rows is different. That lead us to the conclusion that we should keep the one row which has the highest number of reviews, because that's probably the most recent one.

Portuguese: acima nós imprimimos o exemplo de uma duplicata. Entretanto, podemos notar que o número de *reviews* em cada uma das linhas é diferente. Isso nos leva à conclusão de que devemos manter a linha que tem o maior número de *reviews*, porque ela é provavelmente a linha com informações mais recentes.


```python
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
```

    Expected length:  9659
    Dictionary length:  9659



```python
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
```


```python
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


```

    True
    False
    True
    True



```python
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


```

    The length of the original dataset was:  9659
    The length of the new list is:  9614
    Amount of rows deleted:  45
    
    
    Here is a sample of the new list:  
     [['Photo Editor & Candy Camera & Grid & ScrapBook', 'ART_AND_DESIGN', '4.1', '159', '19M', '10,000+', 'Free', '0', 'Everyone', 'Art & Design', 'January 7, 2018', '1.0.0', '4.0.3 and up'], ['U Launcher Lite – FREE Live Cool Themes, Hide Apps', 'ART_AND_DESIGN', '4.7', '87510', '8.7M', '5,000,000+', 'Free', '0', 'Everyone', 'Art & Design', 'August 1, 2018', '1.2.4', '4.0.3 and up'], ['Sketch - Draw & Paint', 'ART_AND_DESIGN', '4.5', '215644', '25M', '50,000,000+', 'Free', '0', 'Teen', 'Art & Design', 'June 8, 2018', 'Varies with device', '4.2 and up'], ['Pixel Draw - Number Art Coloring Book', 'ART_AND_DESIGN', '4.3', '967', '2.8M', '100,000+', 'Free', '0', 'Everyone', 'Art & Design;Creativity', 'June 20, 2018', '1.1', '4.4 and up'], ['Paper flowers instructions', 'ART_AND_DESIGN', '4.4', '167', '5.6M', '50,000+', 'Free', '0', 'Everyone', 'Art & Design', 'March 26, 2017', '1.0', '2.3 and up']]
    
    
    
    
    The length of the original dataset was:  7197
    The length of the new list is:  6183
    Amount of rows deleted:  1014
    
    
    Here is a sample of the new list:  
     [['284882215', 'Facebook', '389879808', 'USD', '0.0', '2974676', '212', '3.5', '3.5', '95.0', '4+', 'Social Networking', '37', '1', '29', '1'], ['389801252', 'Instagram', '113954816', 'USD', '0.0', '2161558', '1289', '4.5', '4.0', '10.23', '12+', 'Photo & Video', '37', '0', '29', '1'], ['529479190', 'Clash of Clans', '116476928', 'USD', '0.0', '2130805', '579', '4.5', '4.5', '9.24.12', '9+', 'Games', '38', '5', '18', '1'], ['420009108', 'Temple Run', '65921024', 'USD', '0.0', '1724546', '3842', '4.5', '4.0', '1.6.2', '9+', 'Games', '40', '5', '1', '1'], ['284035177', 'Pandora - Music & Radio', '130242560', 'USD', '0.0', '1126879', '3594', '4.0', '4.5', '8.4.1', '12+', 'Music', '37', '4', '1', '1']]



```python
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
```

    Length of free apps:  8864
    Sample of free apps:  
     [['Photo Editor & Candy Camera & Grid & ScrapBook', 'ART_AND_DESIGN', '4.1', '159', '19M', '10,000+', 'Free', '0', 'Everyone', 'Art & Design', 'January 7, 2018', '1.0.0', '4.0.3 and up'], ['U Launcher Lite – FREE Live Cool Themes, Hide Apps', 'ART_AND_DESIGN', '4.7', '87510', '8.7M', '5,000,000+', 'Free', '0', 'Everyone', 'Art & Design', 'August 1, 2018', '1.2.4', '4.0.3 and up'], ['Sketch - Draw & Paint', 'ART_AND_DESIGN', '4.5', '215644', '25M', '50,000,000+', 'Free', '0', 'Teen', 'Art & Design', 'June 8, 2018', 'Varies with device', '4.2 and up'], ['Pixel Draw - Number Art Coloring Book', 'ART_AND_DESIGN', '4.3', '967', '2.8M', '100,000+', 'Free', '0', 'Everyone', 'Art & Design;Creativity', 'June 20, 2018', '1.1', '4.4 and up'], ['Paper flowers instructions', 'ART_AND_DESIGN', '4.4', '167', '5.6M', '50,000+', 'Free', '0', 'Everyone', 'Art & Design', 'March 26, 2017', '1.0', '2.3 and up']]
    
    
    Length of free apps:  3222
    Sample of free apps:  
     [['284882215', 'Facebook', '389879808', 'USD', '0.0', '2974676', '212', '3.5', '3.5', '95.0', '4+', 'Social Networking', '37', '1', '29', '1'], ['389801252', 'Instagram', '113954816', 'USD', '0.0', '2161558', '1289', '4.5', '4.0', '10.23', '12+', 'Photo & Video', '37', '0', '29', '1'], ['529479190', 'Clash of Clans', '116476928', 'USD', '0.0', '2130805', '579', '4.5', '4.5', '9.24.12', '9+', 'Games', '38', '5', '18', '1'], ['420009108', 'Temple Run', '65921024', 'USD', '0.0', '1724546', '3842', '4.5', '4.0', '1.6.2', '9+', 'Games', '40', '5', '1', '1'], ['284035177', 'Pandora - Music & Radio', '130242560', 'USD', '0.0', '1126879', '3594', '4.0', '4.5', '8.4.1', '12+', 'Music', '37', '4', '1', '1']]


English: so with this we finish cleaning our datasets. In this last step, we created a new list that only contains free apps. This will help us to understand what kind of free apps are more successful, and probably more profitable in the free app market. In the next step, we will begin to build on this cleaned data we now have.

Portuguese: agora nós terminamos de limpar nossos *datasets*. Nesse último passo, nós criamos uma lista que contém apenas aplicativos grátis. Isso nos ajudará a entender que tipos de aplicativos gratuitos fazem mais sucesso, e provavelmente que são mais lucrativos no mercado de aplicativos gratuitos. No próximo passo, vamos começar a construir em cima desses dados limpos que temos agora.

## Analyzing our data

English: the main goal of our company is to make revenue on free apps. So the plan is: 1) to build a minimal android app and add it to Google Play; 2)if things go well and people like it, it's gonna be developed; 3) if the app is profitable after six months, we will build a version for App Store.

So now we're going to dive in a little deeper in our datasets, and try to discover what app profile is more suitable for our purposes.

Portuguese: o objetivo principal da nossa companhia é criar receita em aplicativos gratuitos. Então o plano é: 1) criar um aplicativo básico e adicionar à Google Play; 2) se as coisas correrem bem e as pessoas gostarem, o aplicativo será de fato desenvolvido; 3) se o aplicativo se mostrar lucrativo nos próximos seis meses, será desenvolvida uma versão para a App Store.

Então agora vamos mergulhar um pouco mais funto nos nossos *datasets* e tentar descobrir que perfil de aplicativo se encaixa melhor nos nossos planos.


```python
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
```


```python
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
```

    Apple Genres: 
    Games : 58.16263190564867
    Entertainment : 7.883302296710118
    Photo & Video : 4.9658597144630665
    Education : 3.662321539416512
    Social Networking : 3.2898820608317814
    Shopping : 2.60707635009311
    Utilities : 2.5139664804469275
    Sports : 2.1415270018621975
    Music : 2.0484171322160147
    Health & Fitness : 2.0173805090006205
    Productivity : 1.7380509000620732
    Lifestyle : 1.5828677839851024
    News : 1.3345747982619491
    Travel : 1.2414649286157666
    Finance : 1.1173184357541899
    Weather : 0.8690254500310366
    Food & Drink : 0.8069522036002483
    Reference : 0.5586592178770949
    Business : 0.5276225946617008
    Book : 0.4345127250155183
    Navigation : 0.186219739292365
    Medical : 0.186219739292365
    Catalogs : 0.12414649286157665
    
    
    Google Categories: 
    FAMILY : 18.907942238267147
    GAME : 9.724729241877256
    TOOLS : 8.461191335740072
    BUSINESS : 4.591606498194946
    LIFESTYLE : 3.9034296028880866
    PRODUCTIVITY : 3.892148014440433
    FINANCE : 3.7003610108303246
    MEDICAL : 3.531137184115524
    SPORTS : 3.395758122743682
    PERSONALIZATION : 3.3167870036101084
    COMMUNICATION : 3.2378158844765346
    HEALTH_AND_FITNESS : 3.0798736462093865
    PHOTOGRAPHY : 2.944494584837545
    NEWS_AND_MAGAZINES : 2.7978339350180503
    SOCIAL : 2.6624548736462095
    TRAVEL_AND_LOCAL : 2.33528880866426
    SHOPPING : 2.2450361010830324
    BOOKS_AND_REFERENCE : 2.1435018050541514
    DATING : 1.861462093862816
    VIDEO_PLAYERS : 1.7937725631768955
    MAPS_AND_NAVIGATION : 1.3989169675090252
    FOOD_AND_DRINK : 1.2409747292418771
    EDUCATION : 1.1620036101083033
    ENTERTAINMENT : 0.9589350180505415
    LIBRARIES_AND_DEMO : 0.9363718411552346
    AUTO_AND_VEHICLES : 0.9250902527075812
    HOUSE_AND_HOME : 0.8235559566787004
    WEATHER : 0.8009927797833934
    EVENTS : 0.7107400722021661
    PARENTING : 0.6543321299638989
    ART_AND_DESIGN : 0.6430505415162455
    COMICS : 0.6204873646209386
    BEAUTY : 0.5979241877256317
    
    
    Google Genres: 
    Tools : 8.449909747292418
    Entertainment : 6.069494584837545
    Education : 5.347472924187725
    Business : 4.591606498194946
    Productivity : 3.892148014440433
    Lifestyle : 3.892148014440433
    Finance : 3.7003610108303246
    Medical : 3.531137184115524
    Sports : 3.463447653429603
    Personalization : 3.3167870036101084
    Communication : 3.2378158844765346
    Action : 3.1024368231046933
    Health & Fitness : 3.0798736462093865
    Photography : 2.944494584837545
    News & Magazines : 2.7978339350180503
    Social : 2.6624548736462095
    Travel & Local : 2.3240072202166067
    Shopping : 2.2450361010830324
    Books & Reference : 2.1435018050541514
    Simulation : 2.0419675090252705
    Dating : 1.861462093862816
    Arcade : 1.8501805054151623
    Video Players & Editors : 1.7712093862815883
    Casual : 1.7599277978339352
    Maps & Navigation : 1.3989169675090252
    Food & Drink : 1.2409747292418771
    Puzzle : 1.128158844765343
    Racing : 0.9927797833935018
    Role Playing : 0.9363718411552346
    Libraries & Demo : 0.9363718411552346
    Auto & Vehicles : 0.9250902527075812
    Strategy : 0.9138086642599278
    House & Home : 0.8235559566787004
    Weather : 0.8009927797833934
    Events : 0.7107400722021661
    Adventure : 0.6768953068592057
    Comics : 0.6092057761732852
    Beauty : 0.5979241877256317
    Art & Design : 0.5979241877256317
    Parenting : 0.4963898916967509
    Card : 0.45126353790613716
    Casino : 0.42870036101083037
    Trivia : 0.41741877256317694
    Educational;Education : 0.39485559566787
    Board : 0.3835740072202166
    Educational : 0.3722924187725632
    Education;Education : 0.33844765342960287
    Word : 0.2594765342960289
    Casual;Pretend Play : 0.236913357400722
    Music : 0.2030685920577617
    Racing;Action & Adventure : 0.16922382671480143
    Puzzle;Brain Games : 0.16922382671480143
    Entertainment;Music & Video : 0.16922382671480143
    Casual;Brain Games : 0.13537906137184114
    Casual;Action & Adventure : 0.13537906137184114
    Arcade;Action & Adventure : 0.12409747292418773
    Action;Action & Adventure : 0.10153429602888085
    Educational;Pretend Play : 0.09025270758122744
    Simulation;Action & Adventure : 0.078971119133574
    Parenting;Education : 0.078971119133574
    Entertainment;Brain Games : 0.078971119133574
    Board;Brain Games : 0.078971119133574
    Parenting;Music & Video : 0.06768953068592057
    Educational;Brain Games : 0.06768953068592057
    Casual;Creativity : 0.06768953068592057
    Art & Design;Creativity : 0.06768953068592057
    Education;Pretend Play : 0.056407942238267145
    Role Playing;Pretend Play : 0.04512635379061372
    Education;Creativity : 0.04512635379061372
    Role Playing;Action & Adventure : 0.033844765342960284
    Puzzle;Action & Adventure : 0.033844765342960284
    Entertainment;Creativity : 0.033844765342960284
    Entertainment;Action & Adventure : 0.033844765342960284
    Educational;Creativity : 0.033844765342960284
    Educational;Action & Adventure : 0.033844765342960284
    Education;Music & Video : 0.033844765342960284
    Education;Brain Games : 0.033844765342960284
    Education;Action & Adventure : 0.033844765342960284
    Adventure;Action & Adventure : 0.033844765342960284
    Video Players & Editors;Music & Video : 0.02256317689530686
    Sports;Action & Adventure : 0.02256317689530686
    Simulation;Pretend Play : 0.02256317689530686
    Puzzle;Creativity : 0.02256317689530686
    Music;Music & Video : 0.02256317689530686
    Entertainment;Pretend Play : 0.02256317689530686
    Casual;Education : 0.02256317689530686
    Board;Action & Adventure : 0.02256317689530686
    Video Players & Editors;Creativity : 0.01128158844765343
    Trivia;Education : 0.01128158844765343
    Travel & Local;Action & Adventure : 0.01128158844765343
    Tools;Education : 0.01128158844765343
    Strategy;Education : 0.01128158844765343
    Strategy;Creativity : 0.01128158844765343
    Strategy;Action & Adventure : 0.01128158844765343
    Simulation;Education : 0.01128158844765343
    Role Playing;Brain Games : 0.01128158844765343
    Racing;Pretend Play : 0.01128158844765343
    Puzzle;Education : 0.01128158844765343
    Parenting;Brain Games : 0.01128158844765343
    Music & Audio;Music & Video : 0.01128158844765343
    Lifestyle;Pretend Play : 0.01128158844765343
    Lifestyle;Education : 0.01128158844765343
    Health & Fitness;Education : 0.01128158844765343
    Health & Fitness;Action & Adventure : 0.01128158844765343
    Entertainment;Education : 0.01128158844765343
    Communication;Creativity : 0.01128158844765343
    Comics;Creativity : 0.01128158844765343
    Casual;Music & Video : 0.01128158844765343
    Card;Action & Adventure : 0.01128158844765343
    Books & Reference;Education : 0.01128158844765343
    Art & Design;Pretend Play : 0.01128158844765343
    Art & Design;Action & Adventure : 0.01128158844765343
    Arcade;Pretend Play : 0.01128158844765343
    Adventure;Education : 0.01128158844765343


English:
We'll try to answer some questions, so we can have an idea about what those percentages tell us. We should keep in mind we are talking about free english apps, and our conclusions apply only to this group.

**About App Store:**

What is the most common genre? What is the runner-up? What other patterns do we see? What is the general impression — are most of the apps designed for practical purposes  or more for entertainment?

***

The most common `Prime Genre` is Games (58.16%) by far, covering more than half of the amount of free english apps. The runner-up is Entertainment (7.88%), followed by Photo & Video (4.96%), Education (3.66%) and Social Networking (3.29%).

Besides Education, which seems to be "the man in the middle" so to speak, the top rank of free english apps is composed basically by apps for entertainment like games, photo and video and social networking.

Below the Social Networking genre, the other apps share their market with other genres with percentages from 2.6% (Shopping) down to 0.12% (Catalogs).

Although Games is dominant about the amount of free english apps, it would be a mistake to imply that it also has a large number of users.


**About Google Play:**

What are the most common genres? What other patterns do you see? Compare the patterns you see for the Google Play market with those you saw for the App Store market. Can you recommend an app profile based on what you found so far? Do the frequency tables you generated reveal the most frequent app genres or what genres have the most users?

***

The most common `Categories` in Google Play are Family (18.9%), Games (9.72%) and Tools (8.46%).

This top rank is followed by the categories Business, Lifestyle and Productivity.

When it comes to `Genres`, Tools comes first (8.45%), followed by Entertainment (6.07%) and Education (5.35%).

We can see that this top rank is followed by the genres Business, Productivity and Lifestyle.

It looks like the top ranks in Play Store are more related to practical purposes like education, business, productivity and so on.

The percentage of apps in each category and genre seems to be more evenly distributed, as opposed to what we saw in App Store.

We can tell by our table what apps have the higher frequency, but we still can't recommend an app profile based on what we got so far.

**Note**
***

In Google Play it is hard to tell the difference between `Genres` and `Categories`. 

If we go to Google Play we can se that the Family category is filled up most with games for kids. Does that mean that games are more representative on free english apps in Google Play as well? We can't assume that. And the other categories seems to be evenly distributed. So we continue with our initial observations.

![Image](https://camo.githubusercontent.com/9bf24b9efc3d88a3d55f5c09e314987941f0bab5/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f64712d636f6e74656e742f3335302f7079316d385f66616d696c792e706e67)


```python
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
```

    Catalogs :  4004.0
    Weather :  52279.892857142855
    Travel :  28243.8
    News :  21248.023255813954
    Utilities :  18684.456790123455
    Navigation :  86090.33333333333
    Education :  7003.983050847458
    Shopping :  26919.690476190477
    Health & Fitness :  23298.015384615384
    Games :  22788.6696905016
    Reference :  74942.11111111111
    Music :  57326.530303030304
    Book :  39758.5
    Photo & Video :  28441.54375
    Social Networking :  71548.34905660378
    Medical :  612.0
    Sports :  23008.898550724636
    Finance :  31467.944444444445
    Food & Drink :  33333.92307692308
    Business :  7491.117647058823
    Productivity :  21028.410714285714
    Lifestyle :  16485.764705882353
    Entertainment :  14029.830708661417


## First impressions

English: now we have a nice clue of which apps profiles from App Store might be of interest of our company.

We could say that Navigation, Reference and Social Networking have more ratings per amount of apps in that genre. But what is Reference genre is all about? Navigation is probably influenced by few giant apps like Google Maps and Waze. The same occurs to Social Networking, influenced by Instagram, Facebook and others giants. So, probably other apps in this category may struggle to get users.

Following those, we have Music, Weather, Book and Finance, that may be more democratic categories to our company to get in.

So if we need to recommend some profile for our developers team, we could say the genres: Navigation, Social Networking, Music, Weather, Book and Finance.


```python
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
            
```

    ART_AND_DESIGN 1.7543859649122806
    COMMUNICATION 174.21602787456445
    PERSONALIZATION 1.7006802721088434
    LIFESTYLE 28901.73410404624
    HOUSE_AND_HOME 1.36986301369863
    AUTO_AND_VEHICLES 1.2195121951219512
    PHOTOGRAPHY 38314.17624521073
    BOOKS_AND_REFERENCE 5.2631578947368425
    DATING 606.060606060606
    BUSINESS 0.02457002457002457
    PARENTING 17.24137931034483
    EVENTS 7.936507936507937
    SHOPPING 5025.125628140703
    LIBRARIES_AND_DEMO 120481.92771084337
    SPORTS 0.0033222591362126247
    PRODUCTIVITY 0.028985507246376812
    BEAUTY 1886.7924528301887
    NEWS_AND_MAGAZINES 403.2258064516129
    EDUCATION 9708.73786407767
    ENTERTAINMENT 117647.05882352941
    GAME 116.0092807424594
    FAMILY 0.059665871121718374
    WEATHER 1408.4507042253522
    FINANCE 30.48780487804878
    FOOD_AND_DRINK 0.09090909090909091
    TRAVEL_AND_LOCAL 4.830917874396135
    SOCIAL 21186.4406779661
    MAPS_AND_NAVIGATION 40.32258064516129
    VIDEO_PLAYERS 0.6289308176100629
    MEDICAL 3.194888178913738
    TOOLS 133.33333333333334
    HEALTH_AND_FITNESS 366.3003663003663
    COMICS 181.8181818181818


English: when we look from the perspective of number of installs, we have a more clear idea about the path to our main goal. We can see that the category Communication and Dating have large amounts of installs. However these categroies are populated by apps like Whatsapp, Facebook Messenger, Tinder, etc. So, it would be risky to recommend a category like that. On the other hand, we can notice interesting like Libraries and Demo, Lifestyle, Beauty and News and Magazines.
