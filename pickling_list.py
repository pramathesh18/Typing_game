import pickle

word_list0 = ['Africa', 'Among', 'Asia', 'Basin', 'Bengal', 'Bhutan', 'Bhārat', 'China', 'Crown', 'Delhi', 'During', 'Early', 'East', 'Empire', 'From', 'Ganges', 'Gupta', 'Hindi', 'Hindu', 'India', 'Indian', 'Indo', 'Indus', 'Islam', 'Lanka', 'Maurya', 'Middle', 'Modern', 'Mughal', 'Muslim', 'Nepal', 'Ocean', 'Punjab', 'South', 'Their', 'Valley', 'also', 'amid', 'among', 'area', 'arisen', 'armies', 'based', 'basin', 'became', 'become', 'been', 'began', 'being', 'belief', 'border', 'capita', 'caste', 'child', 'class', 'coasts', 'cost', 'cover', 'down', 'early', 'east', 'ending', 'ethnic', 'faces', 'factor', 'fast', 'forest', 'form', 'forms', 'four', 'from', 'gave', 'gender', 'global', 'grew', 'high', 'highly', 'human', 'humans', 'hunter', 'ideas', 'income', 'into', 'knit', 'land', 'large', 'later', 'legacy', 'levels', 'life', 'long', 'loose', 'loss', 'made', 'major', 'marked', 'middle', 'most', 'movies', 'multi', 'music', 'north', 'noted', 'only', 'orders', 'over', 'peace', 'plains', 'play', 'public', 'ranks', 'rate', 'region', 'rights', 'rise', 'rising', 'river', 'role', 'root', 'roots', 'rule', 'same', 'scale', 'second', 'share', 'shares', 'since', 'slowly', 'social', 'socio', 'south', 'space', 'state', 'status', 'system', 'than', 'these', 'third', 'though', 'time', 'took', 'viewed', 'weapon', 'were', 'west', 'which', 'wide', 'with', 'within', 'women', 'world', 'years']
word_list = []
for item in word_list0:
    obj = item.lower()
    word_list.append(obj)

print(word_list)

file = "wordlist.pkl"

fileobj = open(file,"wb")
pickle.dump(word_list,fileobj)
fileobj.close()
