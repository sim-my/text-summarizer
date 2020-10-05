# importing the necessary libraries
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest

#adding new line to punctuation
punctuation = punctuation + '\n'

text = '''
Nepal, country of Asia, lying along the southern slopes of the Himalayan mountain ranges. 
It is a landlocked country located between India to the east, south, and west and the Tibet Autonomous Region of China to the north. 
Its territory extends roughly 500 miles (800 kilometres) from east to west and 90 to 150 miles from north to south. 
The capital is Kathmandu.
Nepal, long under the rule of hereditary prime ministers favouring a policy of isolation, remained closed to the outside world until a palace revolt in 1950 restored the crown’s authority in 1951; the country gained admission to the United Nations in 1955. 
In 1991 the kingdom established a multiparty parliamentary system. In 2008, however, after a decadelong period of violence and turbulent negotiation with a strong Maoist insurgency, the monarchy was dissolved, and Nepal was declared a democratic republic.
Wedged between two giants, India and China, Nepal seeks to keep a balance between the two countries in its foreign policy—and thus to remain independent. 
A factor that contributes immensely to the geopolitical importance of the country is the fact that a strong Nepal can deny China access to the rich Gangetic Plain.
Nepal thus marks the southern boundary of the Chinese sphere north of the Himalayas in Asia.
As a result of its years of geographic and self-imposed isolation, Nepal is one of the least developed nations of the world.
In recent years many countries, including India, China, the United States, the United Kingdom, Japan, Denmark, Germany, Canada, and Switzerland, have provided economic assistance to Nepal. 
The extent of foreign aid to Nepal has been influenced to a considerable degree by the strategic position of the country between India and China.
Nepal contains some of the most rugged and difficult mountain terrain in the world. 
Roughly 75 percent of the country is covered by mountains. From the south to the north, Nepal can be divided into four main physical belts, each of which extends east to west across the country. 
These are, first, the Tarai, a low, flat, fertile land adjacent to the border of India; second, the forested Churia foothills and the Inner Tarai zone, rising from the Tarai plain to the rugged Mahābhārat Range; third, the mid-mountain region between the Mahābhārat Range and the Great Himalayas; and, fourth, the Great Himalaya Range, rising to more than 29,000 feet (some 8,850 metres).
The Tarai forms the northern extension of the Gangetic Plain and varies in width from less than 16 to more than 20 miles, narrowing considerably in several places. A 10-mile-wide belt of rich agricultural land stretches along the southern part of the Tarai; the northern section, adjoining the foothills, is a marshy region in which wild animals abound and malaria is endemic.
The Churia Range, which is sparsely populated, rises in almost perpendicular escarpments to an altitude of more than 4,000 feet. Between the Churia Range to the south and the Mahābhārat Range to the north, there are broad basins from 2,000 to 3,000 feet high, about 10 miles wide, and 20 to 40 miles long; these basins are often referred to as the Inner Tarai. 
In many places they have been cleared of the forests and savanna grass to provide timber and areas for cultivation.
A complex system of mountain ranges, some 50 miles in width and varying in elevation from 8,000 to 14,000 feet, lie between the Mahābhārat Range and the Great Himalayas. 
The ridges of the Mahābhārat Range present a steep escarpment toward the south and a relatively gentle slope toward the north. 
To the north of the Mahābhārat Range, which encloses the valley of Kāthmāndu, are the more lofty ranges of the Inner Himalaya (Lesser Himalaya), rising to perpetually snow-covered peaks. 
The Kāthmāndu and the Pokharā valleys lying within this mid-mountain region are flat basins, formerly covered with lakes, that were formed by the deposition of fluvial and fluvioglacial material brought down by rivers and glaciers from the enclosing ranges during the four glacial and intervening warm phases of the Pleistocene Epoch (from about 2,600,000 to 11,700 years ago).
The Great Himalaya Range, ranging in elevation from 14,000 to more than 29,000 feet, contains many of the world’s highest peaks—Everest, Kānchenjunga I, Lhotse I, Makālu I, Cho Oyu, Dhaulāgiri I, Manāslu I, and Annapūrna I—all of them above 26,400 feet. Except for scattered settlements in high mountain valleys, this entire area is uninhabited.
The Kāthmāndu Valley, the political and cultural hub of the nation, is drained by the Bāghmati River, flowing southward, which washes the steps of the sacred temple of Paśupatinātha (Pashupatinath) and rushes out of the valley through the deeply cut Chhobar gorge. Some sandy layers of the lacustrine beds act as aquifers (water-bearing strata of permeable rock, sand, or gravel), and springs occur in the Kāthmāndu Valley where the sands outcrop. 
The springwater often gushes out of dragon-shaped mouths of stone made by the Nepalese; it is then collected in tanks for drinking and washing and also for raising paddy nurseries in May, before the monsoon. Drained by the Seti River, the Pokharā Valley, 96 miles west of Kāthmāndu, is also a flat lacustrine basin. There are a few remnant lakes in the Pokharā basin, the largest being Phewa Lake, which is about two miles long and nearly a mile wide. North of the basin lies the Annapūrna massif of the Great Himalaya Range.
The major rivers of Nepal—the Kosi, Nārāyani (Gandak), and Karnāli, running southward across the strike of the Himalayan ranges—form transverse valleys with deep gorges, which are generally several thousand feet in depth from the crest of the bordering ranges. The watershed of these rivers lies not along the line of highest peaks in the Himalayas but to the north of it, usually in Tibet.
The rivers have considerable potential for development of hydroelectric power. Two irrigation-hydroelectric projects have been undertaken jointly with India on the Kosi and Nārāyani rivers. Discussions have been held to develop the enormous potential of the Karnāli River. A 60,000-kilowatt hydroelectric project at Kulekhani, funded by the World Bank, Kuwait, and Japan, began operation in 1982.
In the upper courses of all Nepalese rivers, which run through mountain regions, there are little or no flood problems. In low-lying areas of the Tarai plain, however, serious floods occur.
The rivers and small streams of the Tarai, especially those in which the dry season discharge is small, are polluted by large quantities of domestic waste thrown into them. Towns and villages have expanded without proper provision for sewage disposal facilities, and more industries have been established at selected centres in the Tarai. The polluted surface water in the Kāthmāndu and Pokharā valleys, as well as in the Tarai, are unacceptable for drinking.
'''
# Getting the list of all the stop words
stop_words = list(STOP_WORDS)

# Loading the NLP model from spacy
nlp = spacy.load('en_core_web_sm')

#fitting the text to model
def model(text):
    doc = nlp(text)
    return doc


#word tokenization 
def word_tokenization(doc):
    tokens = [tokens.text for tokens in doc]
    return tokens

#generating frequency of each word in the text
def generate_word_frequency(doc):    
    word_frequency = {}
    for word in doc:
        if word.text.lower() not in stop_words:
            if word.text.lower() not in punctuation:
                if word.text not in word_frequency.keys():
                    word_frequency[word.text] = 1
                else:
                    word_frequency[word.text] += 1
    return word_frequency

#normalization of the word frequency
def normalization_word_frequency(word_frequency):
    max_frequency = max(word_frequency.values())
    for word in word_frequency.keys():
        word_frequency[word] = word_frequency[word]/max_frequency
    return word_frequency

#sentence tokenization
def sentence_tokenization(doc):
    sentence_tokens = [sent for sent in doc.sents]
    return sentence_tokens


#generating sentence scores for each sentence
def generate_sentence_scores(sentence_tokens, word_frequency):
    sentence_scores = {}
    for sent in sentence_tokens:
        for word in sent:
            if word.text.lower() in word_frequency.keys():
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequency[word.text.lower()]
                else:
                    sentence_scores[sent] += word_frequency[word.text.lower()]
    return sentence_scores

#setting summary length
def generate_summary_length(sentence_tokens):
    summary_length = int(len(sentence_tokens)*0.3)
    return summary_length

#generating sentence summary
def generate_summary(summary_length, sentence_scores):
    summary_sentences = nlargest(summary_length, sentence_scores, key=sentence_scores.get)
    summary_words = [words.text for words in summary_sentences]
    final_summary = ' '.join(summary_words)
    return final_summary

def main(text):
    doc = model(text)
    tokens = word_tokenization(doc)
    word_frequency = generate_word_frequency(doc)
    normalized_word_frequency = normalization_word_frequency(word_frequency)
    sentence_tokens = sentence_tokenization(doc)
    sentence_scores = generate_sentence_scores(sentence_tokens, normalized_word_frequency)
    summary_length = generate_summary_length(sentence_tokens)
    final_summary = generate_summary(summary_length, sentence_scores)
    print(final_summary)

main(text)




