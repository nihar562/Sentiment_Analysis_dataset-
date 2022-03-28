def tokenize(text):
    text = re.sub(r'[^A-Za-z]',' ',text.lower())
    tokenized_words = word_tokenize(text)
    return tokenized_words
def remove_stopwords(words,stop_words):
    stop_words = stopwords.words('english')
    return [x for x in words if x not in stop_words]
    
def count(sent):
    score = 0
    for x in sent:
        score = score+1
    return score

def polarity(positive, negative):
    return (positive - negative)/((positive + negative)+ 0.000001)
     

def subjectivity(positive_score, negative_score, num_words):
    return (positive_score+negative_score)/(num_words+ 0.000001)


def syllables(word):
    count = 0
    vowels = 'aeiouy'
    word = word.lower()
    if word[0] in vowels:
        count +=1
    for index in range(1,len(word)):
        if word[index] in vowels and word[index-1] not in vowels:
            count +=1
    if word.endswith('e'):
        count -= 1
    if word.endswith('le'):
        count += 1
    if count == 0:
        count += 1
    return count

## Calculate all the required features

def calculate():
    posi = []
    nega = []
    neut = []
    pola = []
    sub = []
    avg_sen_len = []
    avg_len_word = []
    syllable = []
    comp_count = []
    word_count = []
    p_comp_word = []
    f_index = []
    Personal_pronouns = []
    
    for i in range(1,len(data['URL'])+1):
        with open(f'{i}.txt',encoding='utf-8') as file:
            content = file.read()
            
        tokenize_word = tokenize(content)
        l_words = []
        lemmatizer = WordNetLemmatizer()
        for word in tokenize_word:
            l_words.append(lemmatizer.lemmatize(word))
        a_remove_stopword = remove_stopwords(l_words,stopwords.words('english'))
        sentence = " ".join(a_remove_stopword)
        sia = SentimentIntensityAnalyzer()
        d = sia.polarity_scores(sentence)
        num_words = count(a_remove_stopword)
        polari = polarity(d['pos'],d['neg'])
        subje = subjectivity(d['pos'],d['neg'],num_words)
        pola.append(polari)
        posi.append(d['pos'])
        nega.append(d['neg'])
        neut.append(d['neu'])
        sub.append(subje)
        
        total_sentences=content.count(".")
        total_word = len(tokenize_word)
        Average_sentence_length=total_word/total_sentences
        avg_sen_len.append(round(Average_sentence_length))
        
        word_count.append(total_word)
        
        size_of_word=0
        for x in content:
            size_of_word=size_of_word+len(x)
        Average_size_of_word=size_of_word/total_word
        avg_len_word.append(round(Average_size_of_word))
        
        complex_count=0
        syllable_per_word=[]
        for x in content:
            k=syllables(x)
            syllable_per_word.append(k)
            if k>2:
                complex_count+=1
        syllable_per_word=sum(syllable_per_word)
        comp_count.append(complex_count)
        syllable.append(syllable_per_word)
        
        p_of_comp_words=(complex_count/total_word)*100
        p_comp_word.append(p_of_comp_words)
        
        fog_index = (Average_sentence_length+p_of_comp_words)*0.4
        f_index.append(fog_index)
        
        pp_count=0
        for x in content:
            pattern=r"(\b(I|we|my|us|ours)\b)"
            r1 = re.match(pattern, x)
            if r1:
                pp_count+=1
        Personal_pronouns.append(pp_count)
        
    return [posi,nega,neut,pola,sub,avg_sen_len,avg_len_word,syllable,comp_count,word_count,p_comp_word,f_index,Personal_pronouns]
    
    
## all calculation done
positive,negative,neutral,polarity,subjectivity,Average_sentence_len,Average_word_len,len_syllable,complex_count,word_count,complex_word_precentage,fog_index,Personal_pronouns = calculate()
