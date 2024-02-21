

def emotion(sentences):
        emotions_counter={}
        emotions_sum = 0    
        sent_splited = []
        emotions_words={    
"Joy":["Happy","Excited","Delighted","Blissful","Jubilant"],
"Sadness":["Unhappy","Depressed","Sorrowful","Mournful","Melancholic"],
"Anger":["Furious","Irritated","Enraged","Annoyed","Agitated"],
"Fear":["Scared","Terrified","Anxious","Nervous","Panicked"],
"Surprise":["Astonished","Amazed","Startled","Shocked","Stunned"],
"Disgust":["Repulsed","Revolted","Displeased","Sickened","Appalled"],
"Love":["Affectionate","Adoring","Fond","Devoted","Enamored"],
"Confusion":["Bewildered","Perplexed","Baffled","Confused","Puzzled"],
"Contentment":["Satisfied","Pleased","Gratified","Content","Fulfilled"],
"Embarrassment":["Ashamed","Humiliated","Blushing","Self-conscious","Mortified"],
}
        moods = []
    
        for key, value in emotions_words.items():
            emotions_words[key] = [word.lower() for word in value]
        for sent in sentences:

  
            sent_splited= sent.split(" ")
            for word in sent_splited:
                for emotion in emotions_words.keys():
                    if word.lower() in emotions_words[emotion]:
                
                        emotions_sum+=1
                        if emotion in emotions_counter:
                            emotions_counter[emotion] =  emotions_counter[emotion]+1
                        else :
                            emotions_counter[emotion] = 1

        for emotion1 in emotions_counter.keys():
            #  print(emotion1 + " : " + str(emotions_counter[emotion1]))
             moods.append(emotion1)
        return moods


    # emotions_percents = {}
    # for emotion1 in emotions_counter.keys():
    #     print(emotion1)
    #     emotions_percents[emotion1]= emotions_counter[emotion1] /emotions_sum *100/100
    #     print(emotion1 + " : " + str(emotions_percents[emotion1]))
# sent1 = ["i feel happy and Unhappy in the same time","kas askj Scared askl"]
# emotion(sent1)








        





