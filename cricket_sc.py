from array import array
""" Calculate the total and individual player scores in a cricket match """

def cricket_sc(sc):
    try:
        #getting input as unsigned interger
        given=array('I',sc)
        
        #Player’s dict
        #Initially players in Zero Score
        pl_sc={"pl1":0,"pl2":0}
        
        #Defining function for add the players score
        def player1(score):
            pl_sc["pl1"]=pl_sc["pl1"]+score
        def player2(score):
            pl_sc["pl2"]=pl_sc["pl2"]+score
        ch=[player1,player2]
        
        #loop through the Number of ball using range function 
        for j in range(len(given)):
            
            #Batsman has to be rotated after ever over 
            if (j+1)%6!=0:
                ch[0](given[j])
                if given[j]%2!=0:
                    ch.reverse()
            else:
                ch[0](given[j])
                if given[j]%2==0:
                    ch.reverse()
        #printing the Total score, Batsman 1 and 2 scores
        print("Total Score:",sum(given))            
        print("Batsman  1 score:",pl_sc["pl1"])
        print("Batsman  2 score:",pl_sc["pl2"])
    except:
        raise TypeError ("Please Enter the Unsinged interger array sequence")

    
if __name__=='__main__':
    cricket_sc([1,2,0,0,4,1,6,2,1,3])
    
