import time
import pickle
import random

def printin_styl(str,spd):

    for item in str:
        print(item,end="")
        time.sleep(spd)

def get_words():
    file = "wordlist.pkl"
    fileobj = open(file,"rb")
    word_list = pickle.load(fileobj)
    fileobj.close()
    return word_list

def gameloop(word_list):
    time_left = 10
    score = 0
    stat_dict = {}

    high_score = highscore()
    printin_styl("Existing Highscore = "+high_score,0.05)
    input()


    while True:
        if time_left < 0:
            printin_styl("G A M E - O V E R",0.2)
            print()
            break

        word = (random.choices(word_list)[0])
        print(word,end=" : ")

        start_time = time.time()
        word_inp = input(" ")
        time_taken = time.time() - start_time

        if word == word_inp:
            time_left += 2
            score += 10
            time_left -= time_taken

        else:
            score -= 20
            time_left -= time_taken

        stats_of_game = f"Time taken : {time_taken}\nTime left : {time_left}\nScore : {score}\n"
        print(stats_of_game)
        word_list.remove(word)
        stat_dict[word] = time_taken
        input()
    if score > int(high_score):
        write_highscore(str(score))
    return stat_dict

def welcome():
    msg = "HELLO\nWELCOME!\t\tWELCOME!\t\tWELCOME!\n"
    printin_styl(msg,0.05)

    msg2 = "This is a typing game...\nYou have to type word that comes...\nIts that's simple...😉😋\n"
    printin_styl(msg2,0.02)

def options():
    msg = "Press enter to play the game...\nTo quit TYPE 'quit' : "
    printin_styl(msg,0.02)
    n = input()
    if n == "":
        return True
    elif n == "quit":
        return False

def highscore():
    f = open("high_score.txt","r")
    high_score = f.read()
    f.close()
    return high_score

def write_highscore(score):
    f = open("high_score.txt", 'w')
    f.write(score)
    f.close()

def more_option():
    pass



if __name__ == '__main__':
    welcome()
    while True:
        n = options()
        if n:
            word_list = get_words()
            stat_dict = gameloop(word_list)
        elif n == False :
            break

