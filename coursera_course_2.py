input_file = open("D:/My Files/Projects/Python Programming/coursera_course_2/files/project_twitter_data.csv","r")
output_file = open("D:/My Files/Projects/Python Programming/coursera_course_2/files/resulting_data.csv","w")

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
def strip_punctuation(string):
        for char in punctuation_chars:
            string = string.replace(char, "")
        return string
positive_words = []
with open("D:/My Files/Projects/Python Programming/coursera_course_2/files/positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())
            
    def get_pos(str_sentence):
        str_sentence = strip_punctuation(str_sentence.lower())
        lst_str_sentence = str_sentence.split()
       
        count=0
        for word in lst_str_sentence:
            for pos_word in positive_words:
                if pos_word == word:
                    count+=1
        return count

negative_words = []
with open("D:/My Files/Projects/Python Programming/coursera_course_2/files/negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
            
    def get_neg(str_sentence):
        str_sentence = strip_punctuation(str_sentence.lower())
        lst_str_sentence = str_sentence.split()
       
        count=0
        for word in lst_str_sentence:
            for neg_word in negative_words:
                if neg_word == word:
                    count+=1
        return count
    
def write_file(output_file):
    output_file.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
    output_file.write("\n")

    lines = input_file.readlines()
    header= lines.pop(0)
    for line in lines:
        lst = line.strip().split(',')
        output_file.write("{}, {}, {}, {}, {}".format(lst[1], lst[2], get_pos(lst[0]), get_neg(lst[0]), (get_pos(lst[0])-get_neg(lst[0]))))    
        output_file.write("\n")
        
write_file(output_file)
input_file.close()
output_file.close()
