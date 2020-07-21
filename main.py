                                        #===============================================================================#
                                        # Automated mentions respond in TW using Tweepy library in Python.              #
                                        # BY HISHAM Alatni Hishamalatni@gmail.com.                                      #
                                        #===============================================================================#
import tweepy
import schedule, time
import random



class accounts():
    
    #authnticating
    def __init__(self,consumer_key,consumer_secret,access_token,access_token_secret):
        
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret
        auth = tweepy.OAuthHandler(self.consumer_key,self.consumer_secret)
        auth.set_access_token(self.access_token,self.access_token_secret)
        self.api = tweepy.API(auth)
        me = self.api.me()
        
        print ("Account Name: ",me.name)
        print("Location: ",me.location)

    #collecting new mentions IDs    
    def proccess_mention(self,number_mention):
        
        
        print('#----------------LAST MENTIONS-------------------#')
        f = open('New_Mentions.txt','w')
        for mentions in tweepy.Cursor(self.api.mentions_timeline).items(number_mention):
            tweetid = (str(mentions.id))
            f.write(tweetid)
            f.write('\n')
            print(tweetid)
        f.close() 
        print('#---------------------------Proccessing-------------------------#')
        
        
    #compar new mentions IDs with old ones (alreadyrespondto.txt need to be created)
    def compar(self):
        
        f2 = open('alreadyrespondto.txt','r')
        mylines = [] 
        with open ('New_Mentions.txt', 'r') as New_Mention:  # Open New_Mentions.txt for reading text.
            for line in New_Mention:                   # For each line of New_Mentions.txt
                if line in open('alreadyrespondto.txt').readlines(): # make sure to not process what already processed
                    pass
                else:
                    mylines.append(line) 
                    print("The mention", line, "is ready for proccessing" )
        f2.close()
        
        return mylines
    # main function

        
    def respo_(self,nOfMentions):
        
        accounts.proccess_mention(self,nOfMentions)
        #get mylines mentions ID list 
        letsrespIDs = accounts.compar(self)
        print('#------------------check for proper respond------------------------#')
        sha3r=""
        genre=""
        for ID in letsrespIDs:

            tweett = self.api.get_status(ID)
            print(tweett.text)
            id_str = (str(ID))
            l = [] 
            l.insert(0,tweett.text.split())
            self.user_screen = '@'
            self.user_screen += (tweett.user.screen_name)
            print("\nMention from : ",self.user_screen)
            # 
            #main function
            case1 = ["Complaint","Suggestion"]
            case2 = ["monetary","service"]
            #
            for words in case2 :
                if any(words in s for s in l):
                    sha3r = words
                    print(sha3r) 
                    # responding to mentions
                    self.api.update_status(" . ", in_reply_to_status_id = id_str)
                    accounts.done_respond("hisham",id_str)
                    sha3r = ""
                        
                
            for wordd in case1 :                 
                    
                if any(wordd in hr for hr in l):
                    genre = wordd
                    print(genre)
                    accounts.done_respond("hisham",id_str) 
                    self.api.update_status(" . ", in_reply_to_status_id = id_str)

            if (sha3r != "" and genre != ""):
                
                if (sha3r in case2 and genre in case1):
                    print("full reqest")

                    
                    mylines5 = []
                    with open((str(sha3r)) + (str(genre)) + ".txt", encoding='utf-8') as file:
                        mylines5 = [l.strip() for l in file]
                        print(random.choice(mylines5))
                        accounts.done_respond("hisham",id_str) 
                        self.api.update_status(random.choice(mylines5), in_reply_to_status_id = id_str)
                        print('#------------------check for proper respond------------------------#')
                        
                        
                    
                    #empty verabiles for next round
                    sha3r = ""
                    genre = ""
                elif (sha3r in case2):
                    print("sha3rrrrrrrrrrr")

                    
                    mylines5 = []
                    with open((str(sha3r)) + ".txt", encoding='utf-8') as file:
                        mylines5 = [l.strip() for l in file]
                        print(random.choice(mylines5))
                        accounts.done_respond("hisham",id_str) 
                        self.api.update_status(random.choice(mylines5), in_reply_to_status_id = id_str)
                        print('#------------------check for proper respond------------------------#')
                    
                    
                    
                    sha3r = ""
                elif (genre in case1):
                    print("gnereeeeeeeeeeeee")
                    
                    mylines5 = []
                    with open((str(genre)) + ".txt", encoding='utf-8') as file:
                        mylines5 = [l.strip() for l in file]
                        print(random.choice(mylines5))
                        accounts.done_respond("hisham",id_str) 
                        self.api.update_status(random.choice(mylines5), in_reply_to_status_id = id_str)
                        print('#------------------check for proper respond------------------------#')                   
                    
                    
                    
                    
                    genre = ""
                else:
                    print("no responding is availabel")
                    print('#------------------check for proper respond------------------------#')
                    
            elif (sha3r == "" and genre != ""):
                if (genre in case1):
                    print("only genre")
                    
                    mylines5 = []
                    with open((str(genre)) + ".txt", encoding='utf-8') as file:
                        mylines5 = [l.strip() for l in file]
                        print(random.choice(mylines5))
                        accounts.done_respond("hisham",id_str) 
                        self.api.update_status(random.choice(mylines5), in_reply_to_status_id = id_str)
                        print('#------------------check for proper respond------------------------#')
                    
                    
                    
                    genre = ""
            elif (sha3r != "" and genre == ""):
                if (sha3r in case2):
                    print("only sha3r")
                    
                    
                    mylines5 = []
                    with open((str(sha3r)) + (str(genre)) + ".txt", encoding='utf-8') as file:
                        mylines5 = [l.strip() for l in file]
                        print(random.choice(mylines5))
                        accounts.done_respond("hisham",id_str) 
                        self.api.update_status(random.choice(mylines5), in_reply_to_status_id = id_str)
                        print('#------------------check for proper respond------------------------#')
                    
                    
                    
                    sha3r = ""
            else:
                print("no actions needed")
                print('#------------------check for proper respond------------------------#')


    
    def done_respond(self,tweetID):
    
        f = open('alreadyrespondto.txt','a')
        f.write(tweetID)
        f.write('\n')
        f.close()
        

def autma(minutes_,n_mention):
    schedule.every(minutes_).minutes.do(Hish.respo_,n_mention)
    while True:
        schedule.run_pending()
        time.sleep(60) # wait one minute
        
autma(time,numbers of mentions)        
hisham = accounts('consumer_key','consumer_secret','access_token','access_token_secret')
