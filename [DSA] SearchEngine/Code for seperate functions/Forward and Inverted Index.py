#!/usr/bin/env python
# coding: utf-8

# In[18]:


"""
Since webpages can have multiple words involving symbols and of length one such as single characters which aren't very useful So, in order to filter them out
We have make a list of accepted characters from a-z notice lower case since all the words are converted to lower case
Also, we have ignored all those words which will not make sence such as 'is, am, a, e...' Notice the list of words ignored by search engines is obtained
from https://www.link-assistant.com/seo-stop-words.html
"""
from bs4 import BeautifulSoup;
import operator;
import collections;
#Now since we have both the positions of words and frequencies of useful words
#Next headache is to merge them as a single hash table so that each word has its total frequency,and positions at which it appears
def merge(wordposition,frequency):
    same = set();#Initializing and empty set
    different = dict();##Initializing and empty dictionary
    #for key in the intersection of two keys of two hash maps
    for key in set(wordposition.keys()) & set(frequency.keys()):
        if wordposition[key] == frequency[key]:#if key along with their values matches we will form a tuple
            same.add(key);
        else:
            if key not in different:#since the values will not match because we have different values for the position 
                different[key] = [];#here we are forming another array in which we will store the array having positions and the total frequency of that word
            different[key].extend([frequency[key],wordposition[key]])
    print(different);















#Here we will Used Original Content without filtering to find out the original position of words
def wordspos(words):
    pos = {};#Using dictionary/Hash maps to store the word followed by an array containing its positions of occurences
    countpos = 0;
    accepted = "abcdefghijklmnopqrstuvwxyz\'"  #Ignoring the symbols like !@#$%^&*()_{}: appended with words
    for word in words:
        countpos+=1;#This variable will determine the position
        word = ''.join([ch for ch in word if ch in accepted]);
        if (len(word) == 1):#We are ignoring this because later on we have to merge the two hash maps containing the frequency of words and count to form a single table
            continue;
        key = word.encode('ascii','ignore');
        pos.setdefault(key,[]);#initially using default value of key which is none since we have empty dictionary having no key
        pos[key].append(countpos);
        
    return pos;








#Note: The word list in  countfrequency is the filtered list of words 
def countfrequency(words):
    frequency = {};#Using dictionary /Hash maps to store the word as key value followed by frequency of their occurence
    for word in words:
        if word in frequency:#Check if the word is already present in the dictionary then simply increment its count
            frequency[word] +=1;
        else:#else if the word is not in the dictionary set its count to 1 since its first time appearing
            frequency[word] = 1;

#     print(frequency);
    #Since Hash table containt a Key Value to make a linked list
    #here frequency.items() will return a tuple having ('word',Value)
    #operator.itemgetter(0) will return the first tuple and we will use it as key to sort the dictionary
    #We might not used the sorted dictionary in futre 
#     for key,value in sorted(frequency.items(),key=operator.itemgetter(0)):
#         print(key,value);
    return frequency;




def cleanlist(words):
    newlist = [];
    accepted = "abcdefghijklmnopqrstuvwxyz\'"  
    words_to_be_ignored =  ['a', 'able', 'about', 'above', 'abroad', 'according', 'accordingly', 'across', 'actually', 'adj', 'after', 'afterwards', 'again', 'against', 'ago', 'ahead', "ain't", 'all', 'allow', 'allows', 'almost', 'alone', 'along', 'alongside', 'already', 'also', 'although', 'always', 'am', 'amid', 'amidst', 'among', 'amongst', 'an', 'and', 'another', 'any', 'anybody', 'anyhow', 'anyone', 'anything', 'anyway', 'anyways', 'anywhere', 'apart', 'appear', 'appreciate', 'appropriate', 'are', "aren't", 'around', 'as', "a's", 'aside', 'ask', 'asking', 'associated', 'at', 'available', 'away', 'awfully', 'b', 'back', 'backward', 'backwards', 'be', 'became', 'because', 'become', 'becomes', 'becoming', 'been', 'before', 'beforehand', 'begin', 'behind', 'being', 'believe', 'below', 'beside', 'besides', 'best', 'better', 'between', 'beyond', 'both', 'brief', 'but', 'by', 'c', 'came', 'can', 'cannot', 'cant', "can't", 'caption', 'cause', 'causes', 'certain', 'certainly', 'changes', 'clearly', "c'mon", 'co', 'co.', 'com', 'come', 'comes', 'concerning', 'consequently', 'consider', 'considering', 'contain', 'containing', 'contains', 'corresponding', 'could', "couldn't", 'course', "c's", 'currently', 'd', 'dare', "daren't", 'definitely', 'described', 'despite', 'did', "didn't", 'different', 'directly', 'do', 'does', "doesn't", 'doing', 'done', "don't", 'down', 'downwards', 'during', 'e', 'each', 'edu', 'eg', 'eight', 'eighty', 'either', 'else', 'elsewhere', 'end', 'ending', 'enough', 'entirely', 'especially', 'et', 'etc', 'even', 'ever', 'evermore', 'every', 'everybody', 'everyone', 'everything', 'everywhere', 'ex', 'exactly', 'example', 'except', 'f', 'fairly', 'far', 'farther', 'few', 'fewer', 'fifth', 'first', 'five', 'followed', 'following', 'follows', 'for', 'forever', 'former', 'formerly', 'forth', 'forward', 'found', 'four', 'from', 'further', 'furthermore', 'g', 'get', 'gets', 'getting', 'given', 'gives', 'go', 'goes', 'going', 'gone', 'got', 'gotten', 'greetings', 'h', 'had', "hadn't", 'half', 'happens', 'hardly', 'has', "hasn't", 'have', "haven't", 'having', 'he', "he'd", "he'll", 'hello', 'help', 'hence', 'her', 'here', 'hereafter', 'hereby', 'herein', "here's", 'hereupon', 'hers', 'herself', "he's", 'hi', 'him', 'himself', 'his', 'hither', 'hopefully', 'how', 'howbeit', 'however', 'hundred', 'i', "i'd", 'ie', 'if', 'ignored', "i'll", "i'm", 'immediate', 'in', 'inasmuch', 'inc', 'inc.', 'indeed', 'indicate', 'indicated', 'indicates', 'inner', 'inside', 'insofar', 'instead', 'into', 'inward', 'is', "isn't", 'it', "it'd", "it'll", 'its', "it's", 'itself', "i've", 'j', 'just', 'k', 'keep', 'keeps', 'kept', 'know', 'known', 'knows', 'l', 'last', 'lately', 'later', 'latter', 'latterly', 'least', 'less', 'lest', 'let', "let's", 'like', 'liked', 'likely', 'likewise', 'little', 'look', 'looking', 'looks', 'low', 'lower', 'ltd', 'm', 'made', 'mainly', 'make', 'makes', 'many', 'may', 'maybe', "mayn't", 'me', 'mean', 'meantime', 'meanwhile', 'merely', 'might', "mightn't", 'mine', 'minus', 'miss', 'more', 'moreover', 'most', 'mostly', 'mr', 'mrs', 'much', 'must', "mustn't", 'my', 'myself', 'n', 'name', 'namely', 'nd', 'near', 'nearly', 'necessary', 'need', "needn't", 'needs', 'neither', 'never', 'neverf', 'neverless', 'nevertheless', 'new', 'next', 'nine', 'ninety', 'no', 'nobody', 'non', 'none', 'nonetheless', 'noone', 'no-one', 'nor', 'normally', 'not', 'nothing', 'notwithstanding', 'novel', 'now', 'nowhere', 'o', 'obviously', 'of', 'off', 'often', 'oh', 'ok', 'okay', 'old', 'on', 'once', 'one', 'ones', "one's", 'only', 'onto', 'opposite', 'or', 'other', 'others', 'otherwise', 'ought', "oughtn't", 'our', 'ours', 'ourselves', 'out', 'outside', 'over', 'overall', 'own', 'p', 'particular', 'particularly', 'past', 'per', 'perhaps', 'placed', 'please', 'plus', 'possible', 'presumably', 'probably', 'provided', 'provides', 'q', 'que', 'quite', 'qv', 'r', 'rather', 'rd', 're', 'really', 'reasonably', 'recent', 'recently', 'regarding', 'regardless', 'regards', 'relatively', 'respectively', 'right', 'round', 's', 'said', 'same', 'saw', 'say', 'saying', 'says', 'second', 'secondly', 'see', 'seeing', 'seem', 'seemed', 'seeming', 'seems', 'seen', 'self', 'selves', 'sensible', 'sent', 'serious', 'seriously', 'seven', 'several', 'shall', "shan't", 'she', "she'd", "she'll", "she's", 'should', "shouldn't", 'since', 'six', 'so', 'some', 'somebody', 'someday', 'somehow', 'someone', 'something', 'sometime', 'sometimes', 'somewhat', 'somewhere', 'soon', 'sorry', 'specified', 'specify', 'specifying', 'still', 'sub', 'such', 'sup', 'sure', 't', 'take', 'taken', 'taking', 'tell', 'tends', 'th', 'than', 'thank', 'thanks', 'thanx', 'that', "that'll", 'thats', "that's", "that've", 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'thence', 'there', 'thereafter', 'thereby', "there'd", 'therefore', 'therein', "there'll", "there're", 'theres', "there's", 'thereupon', "there've", 'these', 'they', "they'd", "they'll", "they're", "they've", 'thing', 'things', 'think', 'third', 'thirty', 'this', 'thorough', 'thoroughly', 'those', 'though', 'three', 'through', 'throughout', 'thru', 'thus', 'till', 'to', 'together', 'too', 'took', 'toward', 'towards', 'tried', 'tries', 'truly', 'try', 'trying', "t's", 'twice', 'two', 'u', 'unmj', 'under', 'underneath', 'undoing', 'unfortunately', 'unless', 'unlike', 'unlikely', 'until', 'unto', 'up', 'upon', 'upwards', 'us', 'use', 'used', 'useful', 'uses', 'using', 'usually', 'v', 'value', 'various', 'versus', 'very', 'via', 'viz', 'vs', 'w', 'want', 'wants', 'was', "wasn't", 'way', 'we', "we'd", 'welcome', 'well', "we'll", 'went', 'were', "we'", "weren't", "we've", 'what', 'whatever', "what'll", "what's", "what've", 'when', 'whence', 'whenever', 'where', 'whereafter', 'whereas', 'whereby', 'wherein', "where's", 'whereupon', 'wherever', 'whether', 'which', 'whichever', 'while', 'whilst', 'whither', 'who', "who'd", 'whoever', 'whole', "who'll", 'whom', 'whomever', "who's", 'whose', 'why', 'will', 'willing', 'wish', 'with', 'within', 'without', 'wonder', "won't", 'would', "wouldn't", 'x', 'y', 'yes', 'yet', 'you', "you'd", "you'll", 'your', "you're", 'yours', 'yourself', 'yourselves', "you've", 'z', 'zero']
    
   
    for word in words:
        word = ''.join([ch for ch in word if ch in accepted]);#it will loop for every character inside word string and check if its in the accepted list join them by ignoring all special characters like [!@#$%^&*()]
         #This Condition Will verify that we are not adding single characters as they don't make any sense      
        if(len(word) == 1):
            continue;
        elif(len(word)>0):
            if(word in words_to_be_ignored):
                continue;
            else:
                newlist.append(word.encode('ascii','ignore')); #Here we are encoding unicode string to ascii
              
                
    return newlist;#Returning new list containing useful words
    





#Path which will store the location of file to be opened
#Opening a random file as a sample to check function
#file is opened in r+b mode which is read bytes
path = r'C:/wikipedia-simple-html/wikipedia-simple-html/simple/articles/e/u/r/Euro.html';
with open('C:/wikipedia-simple-html/wikipedia-simple-html/simple/articles/e/u/r/Euro.html',mode='r+b') as fp:
    soup = BeautifulSoup(fp,'html.parser');#We will convert the file into soup object and will use HTML-Parser

title = soup.title.text; #Extracting title from the webpage
framebody = soup.prettify(); #It will print the exact HTML Source Code which will help us to find the similarities between the webpages inorder to extract content
"""
        After Inspecting the Source Code of HTML Pages We found out that the useful content is inside the
        <div> </div> tag having id = bodyContent. So, We have used soup.find(); function of BeautifulSoup library
        to find all the occurences of this tag and then convert it into text which will return the result as UNICODE STRING
"""
bodycontent = soup.find('div',{'id': 'bodyContent'}).text;#Using find function to extract the content of div tag under id = bodyContent
#Since the result is in  unicode string we convert into ASCII and ignore exceptions
encodedstring = bodycontent.encode('ascii','ignore');
#Since we have a continuous stream of words converted to lower case we would like to split them into list of words seperated with commas
#For Example  Stream of words like "Hello World" would be like ['Hello','World']
words = bodycontent.lower().split();
print('Original Content');
print(words);
#Function Which will clean the list and return a new list of useful words
print('List after filtering');
cleanedlist = cleanlist(words);
print(cleanedlist);
print('Frequency of filtered words');
freq = countfrequency(cleanedlist);
print(freq);
print('Positions of words');
pos = wordspos(words);
print(pos);
merge = merge(pos,freq);
print(merge);


# In[ ]:




