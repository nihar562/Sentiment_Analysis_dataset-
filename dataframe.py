## Reading output file
output = pd.read_excel('Output Data Structure.xlsx')

## storing all data in output file
output['POSITIVE SCORE'] = positive
output['NEGATIVE SCORE'] = negative
output['POLARITY SCORE'] = polarity
output['SUBJECTIVITY SCORE'] = subjectivity
output['AVG SENTENCE LENGTH'] = Average_sentence_len
output['PERCENTAGE OF COMPLEX WORDS'] = complex_word_precentage
output['FOG INDEX'] = fog_index
output['AVG NUMBER OF WORDS PER SENTENCE'] = Average_word_len
output['COMPLEX WORD COUNT'] = complex_count
output['WORD COUNT'] = word_count
output['SYLLABLE PER WORD'] = len_syllable
output['PERSONAL PRONOUNS'] = Personal_pronouns
output['AVG WORD LENGTH'] = Average_word_len

output = output.drop(['Unnamed: 15', 'Unnamed: 16', 'Unnamed: 17', 'Unnamed: 18',
       'Unnamed: 19', 'Unnamed: 20'],axis = 1)
output.head()

## convert output to csv file
output.to_csv('output.csv')
