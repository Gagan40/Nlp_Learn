#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 12:36:38 2019

@author: singhgagan
# Accessing Text Corpora and Lexical Resources
# Source: NLTK book chapter2

Practical work in Natural Language Processing typically uses large bodies of linguistic data, or corpora. The goal of this chapter is to answer the following questions:

What are some useful text corpora and lexical resources, and how can we access them with Python?
Which Python constructs are most helpful for this work?
How do we avoid repeating ourselves when writing Python code?
"""

# A text corpora is large body of text
# Accessing the text corpora
"""
Gutenberg Corpus
NLTK includes a small selection of texts from the Project Gutenberg electronic text archive, 
which contains some 25,000 free electronic books, hosted at http://www.gutenberg.org/. 
We begin by getting the Python interpreter to load the NLTK package, 
then ask to see nltk.corpus.gutenberg.fileids(), the file identifiers in this corpus
"""
from nltk.book import *
import nltk
nltk.corpus.gutenberg.fileids()

"""
The gutenberg corpus contains the following 18 fileids
['austen-emma.txt','austen-persuasion.txt','austen-sense.txt','bible-kjv.txt','blake-poems.txt',
 'bryant-stories.txt','burgess-busterbrown.txt','carroll-alice.txt','chesterton-ball.txt',
 'chesterton-brown.txt','chesterton-thursday.txt','edgeworth-parents.txt',
 'melville-moby_dick.txt','milton-paradise.txt','shakespeare-caesar.txt',
 'shakespeare-hamlet.txt','shakespeare-macbeth.txt','whitman-leaves.txt']

"""
#Let's pick out the first of these texts — Emma by Jane Austen — 
# and give it a short name, emma, then find out how many words it contains:

emma=nltk.corpus.gutenberg.words('austen-emma.txt')
len(emma) # 192427
emma = nltk.Text(nltk.corpus.gutenberg.words('austen-emma.txt'))
emma.concordance('surprize')

"""
When we defined emma, we invoked the words() function of the gutenberg object in NLTK's corpus package. But since it is cumbersome to type such long names all the time,
Python provides another version of the import statement, as follows:
"""
from nltk.corpus import gutenberg
gutenberg.fileids()

for fileid in gutenberg.fileids():
    num_chars=len(gutenberg.raw(fileid))
    num_words=len(gutenberg.words(fileid))
    num_sents=len(gutenberg.sents(fileid))
    num_vocab=len(set(w.lower() for w in gutenberg.words(fileid )))
    print(round(num_chars/num_words), round(num_words/num_sents),round(num_words/num_vocab),fileid)

"""
This program displays three statistics for each text: 
1.average word length, 
2.average sentence length, 
3.The number of times each vocabulary item appears in the text on average(our lexical diversity score).
Observe that average word length appears to be a general property of English, 
since it has a recurrent value of 4. 
(In fact, the average word length is really 3 not 4, since the num_chars variable counts spacecharacters.) 
By contrast average sentence length and lexical diversity appear to be characteristics of particular authors.


The previous example also showed how we can access the "raw" text of the book [1], not split up into tokens. 
The raw() function gives us the contents of the file without any linguistic processing. 
So, for example,  len(gutenberg.raw('blake-poems.txt')) tells us 
how many letters occur in the text, including the spaces between words. 
The sents() function divides the text up into its sentences, where each sentence is a list of words:

"""


macbeth_sentences=gutenberg.sents('shakespeare-macbeth.txt')
macbeth_sentences
macbeth_sentences[1116]
longest_len=max(len(s) for s in macbeth_sentences)
[s for s in macbeth_sentences if len(s)==longest_len]

"""
Note

Most NLTK corpus readers include a variety of access methods 
apart from words(), raw(), and sents(). 
Richer linguistic content is available from some corpora, such as part-of-speech tags, 
dialogue tags, syntactic trees, and so forth; we will see these in later chapters.

"""


# Web and Chat Text
"""
Although Project Gutenberg contains thousands of books, it represents established literature. 
It is important to consider less formal language as well. 
NLTK's small collection of web text includes content from a 
Firefox discussion forum, 
conversations overheard in New York, 
the movie script of Pirates of the Carribean, 
personal advertisements, 
and wine reviews:
"""

from nltk.corpus import webtext
for fileid in webtext.fileids():
    print(fileid,webtext.raw(fileid)[:65],'...')


"""
There is also a corpus of instant messaging chat sessions, 
originally collected by the Naval Postgraduate School for research 
on automatic detection of Internet predators. 
The corpus contains over 10,000 posts, anonymized by replacing usernames with generic names of
the form "UserNNN", and manually edited to remove any other identifying information. 
The corpus is organized into 15 files, where each file contains several hundred posts 
collected on a given date, 
for an age-specific chatroom (teens, 20s, 30s, 40s, plus a generic adults chatroom). 
The filename contains the date, chatroom, 
and number of posts; e.g., 10-19-20s_706posts.xml contains 706 posts gathered
 from the 20s chat room on 10/19/2006.
"""

from nltk.corpus import nps_chat
chatroom=nps_chat.posts('10-19-20s_706posts.xml')
chatroom[123]


# ********************* Starting Brown Corpus **************************#


"""
The Brown Corpus was the first million-word electronic corpus of English, 
created in 1961 at Brown University. 
This corpus contains text from 500 sources, and the sources have been categorized by genre, 
such as news, editorial, and so on. 
1.1 gives an example of each genre 
(for a complete list, see http://icame.uib.no/brown/bcm-los.html).

"""
# Example Document for Each Section of the Brown Corpus
"""
ID	File	Genre	      Description
A16	ca16	news	      Chicago Tribune: Society Reportage
B02	cb02	editorial	  Christian Science Monitor: Editorials
C17	cc17	reviews	      Time Magazine: Reviews
D12	cd12	religion	  Underwood: Probing the Ethics of Realtors
E36	ce36	hobbies	      Norling: Renting a Car in Europe
F25	cf25	lore	      Boroff: Jewish Teenage Culture
G22	cg22	belles_lettres	Reiner: Coping with Runaway Technology
H15	ch15	government	  US Office of Civil and Defence Mobilization: The Family Fallout Shelter
J17	cj19	learned	      Mosteller: Probability with Statistical Applications
K04	ck04	fiction	      W.E.B. Du Bois: Worlds of Color
L13	cl13	mystery	      Hitchens: Footsteps in the Night
M01	cm01	science_fiction	Heinlein: Stranger in a Strange Land
N14	cn15	adventure	  Field: Rattlesnake Ridge
P12	cp12	romance	      Callaghan: A Passion in Rome
R06	cr06	humor	      Thurber: The Future, If Any, of Comedy

We can access the corpus as a list of words, or a list of sentences
 (where each sentence is itself just a list of words). 
 We can optionally specify particular categories or files to read:

"""
from nltk.corpus import brown

brown.categories()
# ['adventure','belles_lettres','editorial','fiction','government','hobbies','humor','learned','lore','mystery','news','religion','reviews','romance','science_fiction']

brown.words(categories='news') #  ['The', 'Fulton', 'County', 'Grand', 'Jury', 'said', ...]

brown.words(fileids=['cg22']) # ['Does', 'our', 'society', 'have', 'a', 'runaway', ',', ...]

brown.words(fileids=['cp12']) # ['``', 'I', 'had', 'a', 'rather', 'small', 'place', ...]

brown.sents(categories=['news','editorial','reviews'])

"""
The Brown Corpus is a convenient resource for studying systematic differences between genres, 
a kind of linguistic inquiry known as stylistics. 
Let's compare genres in their usage of modal verbs. 
The first step is to produce the counts for a particular genre.
"""
import nltk
news_text=brown.words(categories='news')
frequency_Distribution=nltk.FreqDist(w.lower() for w in news_text)
modals=['can','could','may','might','will','must']
for m in modals:
    print(m + ':', frequency_Distribution[m], end='') # We need to include end=' ' in order for the print function to put its output on a single line.

# can: 94could: 87may: 93might: 38will: 389must: 53

reviews_text=brown.words(categories='reviews')
freDis=nltk.FreqDist(w.lower() for w in reviews_text)
model_review=['what','when','where','who','why']
for m in model_review:
    print(m+':',freDis[m], end='')

# what: 56when: 60where: 29who: 130why: 9

"""
we need to obtain counts for each genre of interest. 
We'll use NLTK's support for conditional frequency distributions
"""
cfd=nltk.ConditionalFreqDist((genre,words)
                            for genre in brown.categories()
                            for words in brown.words(categories=genre))
genres=['news','hobbies','religion','science_fiction','romance','humor']
models=['can','could','may','might','must','will']
cfd.tabulate(conditions=genres,samples=models)

"""
Observe that the most frequent modal in the news genre is will,
while the most frequent modal in the romance genre is could. 
Would you have predicted this? The idea that word counts might distinguish genres
will be taken up again in chap-data-intensive.
"""
# ****************END of Brown Corpus **************************#


# **************** Strating of Reuters Corpus **************************#

"""
The Reuters Corpus contains 10,788 news documents totaling 1.3 million words. 
The documents have been classified into 90 topics, and grouped into two sets, 
called "training" and "test"; thus, 
the text with fileid 'test/14826' is a document drawn from the test set. 
This split is for training and testing algorithms that automatically detect 
the topic of a document, as we will see in chap-data-intensive.

"""
from nltk.corpus import reuters
reuters.categories() # ['acq', 'alum', 'barley', 'bop', 'carcass', 'castor-oil', 'cocoa','coconut', 'coconut-oil',...]

reuters.fileids() # ['test/14826', 'test/14828', 'test/14829', 'test/14832', ...]

"""
Unlike the Brown Corpus, categories in the Reuters corpus overlap with each other, 
simply because a news story often covers multiple topics.
We can ask for the topics covered by one or more documents, 
or for the documents included in one or more categories. 
For convenience, the corpus methods accept a single fileid or a list of fileids.
"""
reuters.categories('training/9865') # ['barley', 'corn', 'grain', 'wheat']

reuters.categories('training/9880') # ['money-fx']

reuters.categories((['training/9865','training/9880'])) # ['barley', 'corn', 'grain', 'money-fx', 'wheat']

reuters.fileids('barley') #['test/15618','test/15649','test/15676','test/15728','test/15871','test/15875','test/15952','test/17767','test/17769', ...]

reuters.fileids((['barley','corn'])) 
"""
Similarly, we can specify the words or sentences we want in terms of files or categories. 
The first handful of words in each of these texts are the titles, 
which by convention are stored as upper case.

"""
reuters.words('training/2172')[:14] #['FRENCH','CEREAL','EXPORTS','THROUGH','ROUEN','FALL','French','cereal','exports','through','the','port','of','Rouen']

reuters.words(['training/8004','training/8759']) # ['U', '.', 'S', '.', 'SUGAR', 'PROGRAM', 'CUT', 'SENT', ...]


reuters.words(categories='barley') # ['FRENCH', 'FREE', 'MARKET', 'CEREAL', 'EXPORT', ...]

reuters.words(categories=['barley','corn']) # ['THAI', 'TRADE', 'DEFICIT', 'WIDENS', 'IN', 'FIRST', ...]

# ****************END of Reuters Corpus **************************#


# **************** Starting of Inaugural Address  Corpus **************************#

"""
we looked at the Inaugural Address Corpus, but treated it as a single text. 
The graph in fig-inaugural used "word offset" as one of the axes;
this is the numerical index of the word in the corpus, 
counting from the first word of the first address. However, 
the corpus is actually a collection of 55 texts, one for each presidential address. 
An interesting property of this collection is its time dimension:

"""

from nltk.corpus import inaugural
inaugural.fileids() # ['1789-Washington.txt','1793-Washington.txt','1797-Adams.txt','1801-Jefferson.txt','1805-Jefferson.txt','1809-Madison.txt','1813-Madison.txt','1817-Monroe.txt','1821-Monroe.txt',...]

[fileid[:4] for fileid in inaugural.fileids()] # ['1789','1793','1797','1801','1805','1809','1813','1817','1821','1825','1829',...]

"""
Notice that the year of each text appears in its filename. 
To get the year out of the filename, we extracted the first four characters, using fileid[:4].

Let's look at how the words America and citizen are used over time. 
The following code converts the words in the Inaugural corpus to lowercase using w.lower()
then checks if they start with either of the "targets" america or citizen using startswith() 
Thus it will count words like American's and Citizens
"""
import nltk
cfd=nltk.ConditionalFreqDist(
        (target,fileid[:4])
        for fileid in inaugural.fileids()
        for w in inaugural.words(fileid)
        for target in['america','citizen']
        if w.lower().startswith(target))

cfd.plot() # Plot of a Conditional Frequency Distribution: all words in the Inaugural Address Corpus that begin with america or citizen are counted; separate counts are kept for each address; these are plotted so that trends in usage over time can be observed; counts are not normalized for document length.


# **************** End of Inaugural Address  Corpus **************************#


# **************** Starting of Annotated Text Corpus **************************#

"""
Many text corpora contain linguistic annotations, representing POS tags, named entities, 
syntactic structures, semantic roles, and so forth.
NLTK provides convenient ways to access several of these corpora, 
and has data packages containing corpora and corpus samples, freely downloadable 
for use in teaching and research. 1.2 lists some of the corpora. 
For information about downloading them, see http://nltk.org/data. 
For more examples of how to access NLTK corpora, 
please consult the Corpus HOWTO at http://nltk.org/howto.
"""



# **************** End of Annotated Text Corpus **************************#


# **************** Starting Corpora in Another languages **************************#
"""
NLTK comes with corpora for many languages, though in some cases you will need to learn 
how to manipulate character encodings in Python before using these corpora
"""
nltk.corpus.cess_esp.words() # ['El', 'grupo', 'estatal', 'Electricité_de_France', ...]

nltk.corpus.floresta.words() # ['Um', 'revivalismo', 'refrescante', 'O', '7_e_Meio', ...]

nltk.corpus.indian.words('hindi.pos') #  ['पूर्ण', 'प्रतिबंध', 'हटाओ', ':', 'इराक', 'संयुक्त', ...]

nltk.corpus.udhr.fileids() # ['Abkhaz-Cyrillic+Abkh','Abkhaz-UTF8','Achehnese-Latin1','Achuar-Shiwiar-Latin1','Adja-UTF8','Afaan_Oromo_Oromiffa-Latin1','Afrikaans-Latin1','Aguaruna-Latin1','Akuapem_Twi-UTF8',...]

nltk.corpus.udhr.words('Javanese-Latin1')[11:] # ['Saben', 'umat', 'manungsa', 'lair', 'kanthi', 'hak', ...]

"""
The last of these corpora, udhr, contains the 
Universal Declaration of Human Rights in over 300 languages. 
The fileids for this corpus include information about 
the character encoding used in the file,such as UTF8 or Latin1. 
 Let's use a conditional frequency distribution to examine 
 the differences in word lengths for a selection of languages included in the udhr corpus
"""

from nltk.corpus import udhr
languages=['Chickasaw','English','German_Deutsch','Greenlandic_Inuktikut', 'Hungarian_Magyar', 'Ibibio_Efik']

cfd2=nltk.ConditionalFreqDist(
        (lang,len(word))
        for lang in languages
        for word in udhr.words(lang+'-Latin1'))
cfd2.plot(cumulative=True)

"""
Cumulative Word Length Distributions: Six translations of the Universal Declaration 
of Human Rights are processed; this graph shows that words having 5 or fewer letters account 
for about 80% of Ibibio text, 60% of German text, and 25% of Inuktitut text.
"""

"""
Unfortunately, for many languages, substantial corpora are not yet available. 
Often there is insufficient government or industrial support for developing language resources,
and individual efforts are piecemeal and hard to discover or re-use. 
Some languages have no established writing system, or are endangered.
"""

# **************** End Corpora in Another languages **************************#

# **************** Text Corpus Structure *************************************#
"""
We have seen a variety of corpus structures so far.
The simplest kind lacks any structure: it is just a collection of texts.
Often, texts are grouped into categories that might correspond to genre, source, author, language, etc. 
Sometimes these categories overlap, notably in the case of topical categories
as a text can be relevant to more than one topic. 
Occasionally, text collections have temporal structure, 
news collections being the most common example.

Common Structures for Text Corpora: 
The simplest kind of corpus is a collection of isolated texts with no particular organization;
some corpora are structured into categories like genre (Brown Corpus); 
some categorizations overlap, such as topic categories (Reuters Corpus); 
other corpora represent language use over time (Inaugural Address Corpus).

Basic Corpus Functionality defined in NLTK: 
    more documentation can be found using help(nltk.corpus.reader) and by reading the online Corpus HOWTO at http://nltk.org/howto.
**********************************************************************************************
                             Table 1.3 
                             
Example	                                Description

fileids()	                 the files of the corpus

fileids([categories])	     the files of the corpus corresponding to these categories

categories()	             the categories of the corpus

categories([fileids])	     the categories of the corpus corresponding to these files

raw()	                     the raw content of the corpus

raw(fileids=[f1,f2,f3])	     the raw content of the specified files

raw(categories=[c1,c2])	     the raw content of the specified categories

words()	                     the words of the whole corpus

words(fileids=[f1,f2,f3])	 the words of the specified fileids

words(categories=[c1,c2])	 the words of the specified categories
sents()	the sentences of     the whole corpus

sents(fileids=[f1,f2,f3])	 the sentences of the specified fileids

sents(categories=[c1,c2])	 the sentences of the specified categories

abspath(fileid)	             the location of the given file on disk

encoding(fileid)	         the encoding of the file (if known)

open(fileid)	             open a stream for reading the given corpus file

root	                     if the path to the root of locally installed corpus

readme()	                 the contents of the README file of the corpus

*******************************************************************************************
NLTK's corpus readers support efficient access to a variety of corpora, 
and can be used to work with new corpora. 
1.3 lists functionality provided by the corpus readers. 
We illustrate the difference between some of the corpus access methods below
"""
import nltk
from nltk.corpus import gutenberg
raw=gutenberg.raw("burgess-busterbrown.txt")
raw[1:20] # 'The Adventures of B'
words=gutenberg.words("burgess-busterbrown.txt")
words[1:20] # ['The','Adventures','of','Buster','Bear','by','Thornton','W','.','Burgess','1920',']','I','BUSTER','BEAR','GOES','FISHING','Buster','Bear']

sents=gutenberg.sents("burgess-busterbrown.txt")
sents[1:20]

"""
[['I'], ['BUSTER', 'BEAR', 'GOES', 'FISHING'], ['Buster', 'Bear', 'yawned', 'as',
'he', 'lay', 'on', 'his', 'comfortable', 'bed', 'of', 'leaves', 'and', 'watched',
'the', 'first', 'early', 'morning', 'sunbeams', 'creeping', 'through', ...], ...]
"""

# **************** End Text Corpus Structure *************************************#



# *************** Loading your own Corpus ****************************************#
"""
If you have your own collection of text files that you would like to access 
using the above methods, you can easily load them with the help of NLTK's PlaintextCorpusReader. 

 
"""
from nltk.corpus import PlaintextCorpusReader
corpus_root='/home/singhgagan/Gagan/Images'
word_list=PlaintextCorpusReader(corpus_root,'.*')
word_list.fileids()
word_list.words()

"""
As another example, suppose you have your own local copy of Penn Treebank (release 3), in C:\corpora. We can use the BracketParseCorpusReader to access this corpus. We specify the corpus_root to be the location of the parsed Wall Street Journal component of the corpus [1], and give a file_pattern that matches the files contained within its subfolders [2] (using forward slashes).
"""














































 




























































