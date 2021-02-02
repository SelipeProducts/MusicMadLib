class Word:
  the_characters = ""
  the_word_type = ""

  def __init__(self): 
      #self.the_word_type = the_word_type
    pass
  # getter method for subject
  def get_characters(self): 
      return self.the_characters
  # setter method for subject
  def set_characters(self, x): 
      self.the_characters = x 

  # getter method for word type
  def get_word_type(self): 
      return self.the_word_type
  # setter method for word type
  def set_word_type(self, x): 
      self.the_word_type = x 


class Sentence:
  the_subject = Word()
  the_verb = Word()
  the_object = Word()

  #constructor
  def __init__(self, subject, verb, obj): 
      self.the_subject = subject
      self.the_verb = verb
      self.the_object = obj
    
  # getter method for subject
  def get_subject(self): 
      return self.the_subject 
  # setter method for subject
  def set_subject(self, x): 
      self.the_subject = x 
  
  # getter method for verb
  def get_verb(self): 
      return self.the_verb 
  # setter method for verb
  def set_verb(self, x): 
      self.the_verb = x

  # getter method for object
  def get_object(self): 
      return self.the_object
  # setter method for object
  def set_object(self, x): 
      self.the_object = x  


class Pharagraph:
  #array of sentence  classes
  the_sentence_List = []

  def __init__(self, sentence_List):
    self.the_sentence_List = sentence_List
  
  def add_sentence(self, added_sentence):
    self.the_sentence_List.append(added_sentence)
  
  # getter method for the_sentence_List
  def get_sentence_List(self): 
    return self.the_sentence_List
  # setter method for the_sentence_List
  def set_sentence_List(self, x): 
    self.the_sentence_List = x

  def get_element(self, num):
    return self.the_sentence_List[num]
  
  def get_list_size(self):
    return len(self.the_sentence_List)

class Song:
  word1 = Word()
  word2 = Word()
  word3 = Word()
  word4 = Word()
  word5 = Word()
  word6 = Word()
  word7 = Word()
  word8 = Word()
  word9 = Word()
  sentence1 = Sentence(word1, word2, word3)
  sentence2 = Sentence(word4, word5, word6)
  sentence3 = Sentence(word7, word8, word9)
  the_list = [sentence1, sentence2, sentence3]
  the_pharagraph = Pharagraph(the_list)
  the_song_name = ""
  the_artist = ""
  
  #constructor
  def __init__(self, the_pharagraph, the_song_name, the_artist):
    self.the_pharagraph = the_pharagraph
    self.the_song_name = the_song_name
    self.the_artist = the_artist

  #print pharagraph
  def ask_to_fill(self):
    ph_length = len(self.the_pharagraph.get_sentence_List())
    for i in range(ph_length):
        print("\nWord Filler #" + str(i+1) + ")")
        filler_word_subj_type = self.the_pharagraph.get_element(i).get_subject().get_word_type()
        filler_word_verb_type = self.the_pharagraph.get_element(i).get_verb().get_word_type()
        filler_word_obj_type = self.the_pharagraph.get_element(i).get_object().get_word_type()

        subj = input(filler_word_subj_type + ": ")
        verb = input(filler_word_verb_type + ": ")
        obj = input(filler_word_obj_type + ": ")

        self.the_pharagraph.get_element(i).set_subject(subj)
        self.the_pharagraph.get_element(i).set_verb(verb)
        self.the_pharagraph.get_element(i).set_object(obj)

  def set_ph(self, x): 
    self.the_pharagraph = x
  
  def get_ph(self, num):
    return self.the_pharagraph


class Song_cardib(Song):
  def __init__(self, the_pharagraph, the_song_name, the_artist):
    super().__init__(the_pharagraph, "WAP", "Cardi B")

  #WAP Lyrics
  #(Whores in this house)
  # (There's some whores in this house)
  # (There's some whores in this house)
  # (There's some whores in this house)

  # I said, certified freak
  # Seven days a week
  # Wet-ass pussy
  # Make that pull-out game weak, woo

  # Yeah, yeah, yeah, yeah
  # Yeah, you fucking with some wet-ass pussy
  # Bring a bucket and a mop for this wet-ass pussy
  # Give me everything you got for this wet-ass pussy

  def printMadLib(self, a1, a2, a3, b1, b2, b3):
    print("\nOutput:")
    print("(" + a1 +" "+ a2 , "this " + a3 + ")")
    print("(There's some " + a1 + " " + a2 + " this " + a3 + ")")
    print("(There's some " + a1 + " " + a2 + " this " + a3 + ")")
    print("(There's some " + a1 + " " + a2 + " this " + a3 + ")")
    print(b1 + " " + b2 + ", certified " + b3)

class Song_dababy(Song):
  def __init__(self, the_pharagraph, the_song_name, the_artist):
    super().__init__(the_pharagraph, "Rockstar", "Da Baby")

  #Rockstar  Lyrics
  # Woo, woo
  # I pull up like 
  # How you pull up, Baby? How you pull up? (Oh, oh, oh)
  # How you pull up? I pull up (Woo, Seth in the kitchen)
  # Let's go

  # Brand new Lamborghini, fuck a cop car
  # With the pistol on my hip like I'm a cop (Yeah, yeah, yeah)
  # Have you ever met a real nigga rockstar?
  # This ain't no guitar, bitch, this a Glock (Woo)
  # My Glock told me to promise you gon' squeeze me (Woo)
  # You better let me go the day you need me (Woo)
  # Soon as you up me on that nigga, get to bustin' (Woo)
  
  # And if I ain't enough, go get the chop
  # It's safe to say I earned it
  # Ain't a nigga gave me nothin' (Yeah, yeah, yeah)
  # I'm ready to hop out on a nigga, get to bustin'
  # Know you heard me say, "You play, you lay"
  # Don't make me push the button
  # Full of pain, dropped enough tears to fill up a fuckin' bucket

  def printMadLib(self, a1, a2, a3, b1, b2, b3, c1, c2, c3, d1, d2, d3, e1, e2, e3, f1, f2, f3, g1, g2, g3, h1, h2, h3, i1, i2, i3 ):
    print("\nOutput:")
    print(a1 + " " + a2 + " " + a3 + " like	")
    print("How " + b1 + " " + a2 + " " + a3 + ", Baby? How " + b2 + a2 + " " + a3)
    print("How " + b1 + a2 + a3 +"? " + a1 + " " + a2 + " " + a3 + "(Woo, Seth in the kitchen)")
    print("Let's Go\n")

    print("Brand new " + c1 + ", " + c2 + " a cop " + c3)
    print("With the " + d1 + " on my " + d2 + " like im a cop (" + d3 + ", " + d3 + ", " + d3 + ")")
    print("Have " + e1 + " ever " + e2 +" a real " + e3 + " rockstar?")
    print("This aint no " + f1 + ", " + f2 + ", this a " + f3 + " (Woo)")
    print("My " + g1 + " " + g2 + " me to promise " + g3 + " gon squeeze me (Woo)")
    print(a1 + " better let me " + h1 + " the " + h2 + a1 + " need me (Woo)")
    print("Soon as you " + i1 + " on that " + i2, " get to " + i3)

class Song_Axwell(Song):
  def __init__(self, the_pharagraph, the_song_name, the_artist):
    super().__init__(the_pharagraph, "More Then You Kow", "Axwell")

  #More Then You Kow", "Axwell"
  # I saw it coming, from miles away
  # I better speak up if I got something to say
  # 'Cause it ain't over, until she sings
  # You had your reasons, you had a few
  # But you knew that I would go anywhere for you
  # 'Cause it ain't over, until she sings

  # I just need to get it off my chest
  # Yeah, more than you know
  # Yeah, more than you know
  # You should know that baby you're the best
  # Yeah, more than you know
  # Yeah, more than you know

  def printMadLib(self, a1, a2, a3, b1, b2, b3, c1, c2, c3, d1, d2, d3, e1, e2, e3, f1, f2, f3, g1, g2, g3, h1, h2, h3, i1, i2, i3, j1, j2, j3, k1 , k2, k3, l1, l2, l3 ):
    print("\nOutput:")
    print(a1 + " saw " + a2 + " coming, from "+ a3 + " away")
    print(b1 + " better " + b2 + " up if I got " + b3 + " to say")
    print("Cause "+ c1 +" aint over, untill " + c2 + " " +c3)
    print(d1 + " had your " + d2 + ", you had a "+ d3)
    print("But "+ e1 + " " + e2 + " that I would " + e3 + " anywhere for you")
    print("Cause " + f1 +" aint over, untill " + f2 + " " + f3)
    print(g1 + " just need to " + g2 +" it off my " +g3)
    print(h1 + ", " + h2 + " than " + h3 +" know")
    print(i1 + ", " + i2 + " than " + i3 + " know")
    print(j1 + " should " + j2 + " that " + j3 + " the best")
    print(k1 + ", " + k2 + " than " + k3 + " know")
    print(l1 + ", " + l2 + " than "+ l3 + " know")
  
class Game:
  the_song_choice = 0
  
  def __init__(self, the_song_choice):
    self.the_song_choice = the_song_choice
  
  def song_selection(self):
    the_list = []
    the_ph = Pharagraph(the_list)
    print("Pick a song to fill in: ")
    print("1) WAP by Cardi B\n2) Rockstar by DaBaby\n3) More Than You Know by Axwell")
    self.song_choice = int(input("Choice: "))
    if(self.song_choice == 1):
      word1 = Word()
      word1.set_word_type("Plural Noun")
      word2 = Word()
      word2.set_word_type("Past Tense Verb")
      word3 = Word()
      word3.set_word_type("Place")
      sent1 = Sentence(word1, word2, word3)
      
      word4 = Word()
      word4.set_word_type("Noun")
      word5 = Word()
      word5.set_word_type("Past Tense Verb")
      word6 = Word()
      word6.set_word_type("Verb")
      sent2 = Sentence(word4, word5, word6)

      sent_list = [sent1, sent2]
    
      the_ph.set_sentence_List(sent_list)    
      song_cardib_wap = Song_cardib(the_ph, "wap", "play boy carti")
      song_cardib_wap.ask_to_fill()

      song_cardib_wap.printMadLib(the_ph.get_element(0).get_subject(), the_ph.get_element(0).get_verb(), the_ph.get_element(0).get_object(), the_ph.get_element(1).get_subject(), the_ph.get_element(1).get_verb(), the_ph.get_element(1).get_object())
      
    elif(self.song_choice == 2):
      word1 = Word()
      word1.set_word_type("Noun")
      word2 = Word()
      word2.set_word_type("Verb")
      word3 = Word()
      word3.set_word_type("Direction")
      sent1 = Sentence(word1, word2, word3)
      
      word4 = Word()
      word4.set_word_type("Noun")
      word5 = Word()
      word5.set_word_type("Verb")
      word6 = Word()
      word6.set_word_type("Direction")
      sent2 = Sentence(word4, word5, word6)

      word7 = Word()
      word7.set_word_type("Object")
      word8 = Word()
      word8.set_word_type("Verb")
      word9 = Word()
      word9.set_word_type("Related Object")
      sent3 = Sentence(word7, word8, word9)

      word10 = Word()
      word10.set_word_type("Object")
      word11 = Word()
      word11.set_word_type("Body Part")
      word12 = Word()
      word12.set_word_type("Exclamation")
      sent4 = Sentence(word10, word11, word12)

      word13 = Word()
      word13.set_word_type("Noun")
      word14 = Word()
      word14.set_word_type("Verb")
      word15 = Word()
      word15.set_word_type("Noun")
      sent5 = Sentence(word13, word14, word15)

      word16 = Word()
      word16.set_word_type("Object")
      word17 = Word()
      word17.set_word_type("Mean Noun")
      word18 = Word()
      word18.set_word_type("Object")
      sent6 = Sentence(word16, word17, word18)

      word19 = Word()
      word19.set_word_type("Object")
      word20 = Word()
      word20.set_word_type("Verb")
      word21 = Word()
      word21.set_word_type("Pronoun")
      sent7 = Sentence(word19, word20, word21)

      word22 = Word()
      word22.set_word_type("Noun")
      word23 = Word()
      word23.set_word_type("Verb")
      word24 = Word()
      word24.set_word_type("Time Increment")
      sent8 = Sentence(word22, word23, word24)

      word25 = Word()
      word25.set_word_type("Verb")
      word26 = Word()
      word26.set_word_type("Noun")
      word27 = Word()
      word27.set_word_type("Verb")
      sent9 = Sentence(word25, word26, word24)

      sent_list = [sent1, sent2, sent3, sent4, sent5, sent6, sent7, sent8, sent9]

      the_ph.set_sentence_List(sent_list)

      song_dababy_rockstar = Song_dababy(the_ph, "Rockstar", "Da Baby")
      song_dababy_rockstar.ask_to_fill()

      song_dababy_rockstar.printMadLib(the_ph.get_element(0).get_subject(), the_ph.get_element(0).get_verb(), the_ph.get_element(0).get_object(), the_ph.get_element(1).get_subject(), the_ph.get_element(1).get_verb(), the_ph.get_element(1).get_object(), the_ph.get_element(2).get_subject(), the_ph.get_element(2).get_verb(), the_ph.get_element(2).get_object(), the_ph.get_element(3).get_subject(), the_ph.get_element(3).get_verb(), the_ph.get_element(3).get_object(), the_ph.get_element(4).get_subject(), the_ph.get_element(4).get_verb(), the_ph.get_element(4).get_object(), the_ph.get_element(5).get_subject(), the_ph.get_element(5).get_verb(), the_ph.get_element(5).get_object(), the_ph.get_element(6).get_subject(), the_ph.get_element(6).get_verb(), the_ph.get_element(6).get_object(), the_ph.get_element(7).get_subject(), the_ph.get_element(7).get_verb(), the_ph.get_element(7).get_object(), the_ph.get_element(8).get_subject(), the_ph.get_element(8).get_verb(), the_ph.get_element(8).get_object())

    elif(self.song_choice == 3):
      word1 = Word()
      word1.set_word_type("Noun")
      word2 = Word()
      word2.set_word_type("Pronoun")
      word3 = Word()
      word3.set_word_type("Distance")
      sent1 = Sentence(word1, word1, word3)
      
      word4 = Word()
      word4.set_word_type("Noun")
      word5 = Word()
      word5.set_word_type("Verb")
      word6 = Word()
      word6.set_word_type("Pronoun")
      sent2 = Sentence(word4, word5, word6)

      word7 = Word()
      word7.set_word_type("Pronoun")
      word8 = Word()
      word8.set_word_type("Noun")  
      word9 = Word()
      word9.set_word_type("Verb")
      sent3 = Sentence(word7, word8, word9)

      word10 = Word()
      word10.set_word_type("Pronoun")
      word11 = Word()
      word11.set_word_type("Noun")
      word12 = Word()
      word12.set_word_type("Quantifier")
      sent4 = Sentence(word10, word11, word12)

      word13 = Word()
      word13.set_word_type("Person")
      word14 = Word()
      word14.set_word_type("Verb")
      word15 = Word()
      word15.set_word_type("Verb")
      sent5 = Sentence(word13, word14, word15)
      
      # word16 = word7  #same as line 3 
      # word17 = word8
      # word18 = word9
      sent6 = Sentence(word7, word8, word9)

      word19 = Word()
      word19.set_word_type("Noun")
      word20 = Word()
      word20.set_word_type("Verb")
      word21 = Word()
      word21.set_word_type("Body Part")
      sent7 = Sentence(word19, word20, word21)

      word22 = Word()
      word22.set_word_type("Exclamation")
      word23 = Word()
      word23.set_word_type("Quantafier")
      word24 = Word()
      word24.set_word_type("Pronoun")
      sent8 = Sentence(word22, word23, word24)

      # word25 = word7
      # word26 = word8
      # word27 = word9
      sent9 = Sentence(word22, word23, word24)

      word28 = Word()
      word28.set_word_type("Pronoun")
      word29 = Word()
      word29.set_word_type("Verb")
      word30 = Word()
      word30.set_word_type("Noun")
      sent10 = Sentence(word28, word29, word30)

      # word31 = word22
      # word32 = word23
      # word33 = word24
      sent11 = Sentence(word22, word23, word24)
      sent12 = Sentence(word22, word23, word24)

      sent_list = [sent1, sent2, sent3, sent4, sent5, sent6, sent7, sent8, sent9, sent10, sent11, sent12]

      the_ph.set_sentence_List(sent_list)
      song_Axwell_moreThenYouKnow = Song_Axwell(the_ph, "More Then You Know", "Axwell")
      song_Axwell_moreThenYouKnow.ask_to_fill()


      song_Axwell_moreThenYouKnow.printMadLib(the_ph.get_element(0).get_subject(), the_ph.get_element(0).get_verb(), the_ph.get_element(0).get_object(), the_ph.get_element(1).get_subject(), the_ph.get_element(1).get_verb(), the_ph.get_element(1).get_object(), the_ph.get_element(2).get_subject(), the_ph.get_element(2).get_verb(), the_ph.get_element(2).get_object(), the_ph.get_element(3).get_subject(), the_ph.get_element(3).get_verb(), the_ph.get_element(3).get_object(), the_ph.get_element(4).get_subject(), the_ph.get_element(4).get_verb(), the_ph.get_element(4).get_object(), the_ph.get_element(5).get_subject(), the_ph.get_element(5).get_verb(), the_ph.get_element(5).get_object(), the_ph.get_element(6).get_subject(), the_ph.get_element(6).get_verb(), the_ph.get_element(6).get_object(), the_ph.get_element(7).get_subject(), the_ph.get_element(7).get_verb(), the_ph.get_element(7).get_object(), the_ph.get_element(8).get_subject(), the_ph.get_element(8).get_verb(), the_ph.get_element(8).get_object(), the_ph.get_element(9).get_subject(), the_ph.get_element(9).get_verb(), the_ph.get_element(9).get_object(), the_ph.get_element(10).get_subject(), the_ph.get_element(10).get_verb(), the_ph.get_element(10).get_object(), the_ph.get_element(11).get_subject(), the_ph.get_element(11).get_verb(), the_ph.get_element(11).get_object()
      
      
      
      )
    else:
      print("hmmmm...")
      

#-------------------------------------------------------------
music_madlib_game = Game(0)
music_madlib_game.song_selection()