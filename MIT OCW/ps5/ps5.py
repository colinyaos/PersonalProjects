# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name:
# Collaborators:
# Time:

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz


#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
          #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================

# Problem 1

# TODO: NewsStory

class NewsStory(object):
    def __init__(self, guid, title, description, link, pubdate):
        """
        The constructor for NewsStory. 
        Takes guid, title, description, link (all str), as well as pubdate (datetime)
        Stores these arguments, and allows access with appropriate get methods. 
        """
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate 

    def get_guid(self):
        return self.guid
    def get_title(self):
        return self.title
    def get_description(self):
        return self.description
    def get_link(self):
        return self.link
    def get_pubdate(self):
        return self.pubdate


#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError

# PHRASE TRIGGERS

# Problem 2
# TODO: PhraseTrigger

class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        """
        Takes in phrase (str), and stores it. 
        Implements method: is_phrase_in:
        Takes in arg (str) as input
        returns T/F is arg is / is not in phrase
        Note: not case-sensitive
        strings split on spaces and punctuation
        Stores own phrase as lowercase. 
        """
        self.phrase = phrase.lower()
        # print("instantiating with", self.phrase, "as target phrase")

    def is_phrase_in(self, bigger_phrase):
        """
        arg is a string. 
        Test if arg is in bigger_phrase. 
        Note: not case-sensitive
        strings split on spaces, punctuation
        Assuming arg has no punctuation
        """
        replace_string = string.punctuation

        search_phrase = bigger_phrase.lower()

        space_phrase = self.phrase.lower()

        # print(replace_string)

        for char in replace_string:
            space_phrase = space_phrase.replace(char, " ")
            search_phrase = search_phrase.replace(char, " ")

        # print(search_phrase)

        word_list = space_phrase.split()
        bp_list = search_phrase.split()


        # print("own phrase is", word_list)
        # print("big phrase is", bp_list)

        # print("wl_len", len(word_list), "bp_len", len(bp_list))
        for i in range(len(bp_list) - len(word_list) + 1):
            # print("Effective range:", len(bp_list) - len(word_list))
            # print("thing to be tested:", bp_list[i:i + len(word_list)])
            if bp_list[i:i+len(word_list)] == word_list:
                # print("test for search:", search_phrase, ". space:", space_phrase, "!true")
                return True
        
        # print("test for search:", search_phrase, ". space:", space_phrase, "!false")
        return False

# Problem 3
# TODO: TitleTrigger

class TitleTrigger(PhraseTrigger):
    """We use this to evaluate if the title of a news story
    contains the particular phrase combo we're looking for.
    Implement evaluate as before. "
    """
    def evaluate(self, story):
        """story is an object of type NewsStory"""
        title = story.get_title()
        # print(title)
        # print(self.phrase)
        if self.is_phrase_in(title):
            return True
        else:
            return False

# Problem 4
# TODO: DescriptionTrigger

class DescriptionTrigger(PhraseTrigger):
    """We use this to evaluate if the description of a news story
    contains the particular phrase combo we're looking for.
    Implement evaluate as before. 
    Shamelessly stolen from class above. 
    """
    def evaluate(self, story):
        """story is an object of type NewsStory"""
        descript = story.get_description()
        # print(title)
        # print(self.phrase)
        if self.is_phrase_in(descript):
            return True
        else:
            return False

# TIME TRIGGERS

# Problem 5
# TODO: TimeTrigger
# Constructor:
#        Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
#        Convert time from string to a datetime before saving it as an attribute.

class TimeTrigger(Trigger):
    def __init__(self, time):
        """time is a string, need to turn it into a datetime object"""
        Trigger.__init__(self)

        #now, we use the magic strptime function
        #"magic" doesn't work so well unless we manually set timezone to EST
        self.datetime = datetime.strptime(time, "%d %b %Y %H:%M:%S") #takes datestring, format
        # self.datetime = self.datetime.replace(tzinfo=pytz.timezone("EST"))

        #ignore below
        # timebits = time.split() ## This should be in format D M Y Time
        # timebits += timebits.pop(3).split(":") #Now we have D M Y H M S
        # print(timebits)
        # d, mon, y, h, min, s = [timebits[i] for i in range(5)] #magic of list comprehension
        # print(d, mon, y, h, min, s)
        # self.datetime = datetime(y, mon, d, h, min, s) #has to be Y M D H M S

# Problem 6
# TODO: BeforeTrigger and AfterTrigger

class BeforeTrigger(TimeTrigger):
    """Triggers and returns true if story has time earlier than own time"""
    def evaluate(self, story):
        story_time = story.get_pubdate()
        return story_time < self.datetime

class AfterTrigger(TimeTrigger):
    """Triggers and returns true if story has time later than own time"""
    def evaluate(self, story):
        story_time = story.get_pubdate()
        return story_time > self.datetime

# COMPOSITE TRIGGERS

# Problem 7
# TODO: NotTrigger

class NotTrigger(Trigger):
    """Triggers and returns true if given Trigger is False"""
    def __init__(self, T):
        self.T = T
    
    def evaluate(self, story):
        return not self.T.evaluate(story)

# Problem 8
# TODO: AndTrigger

class AndTrigger(Trigger):
    """Triggers and returns true if both given Triggers are True"""
    def __init__(self, T1, T2):
        self.T1 = T1
        self.T2 = T2
    
    def evaluate(self, story):
        return self.T1.evaluate(story) and self.T2.evaluate(story)

# Problem 9
# TODO: OrTrigger

class OrTrigger(Trigger):
    """Triggers and returns true if either given Trigger is True"""
    def __init__(self, T1, T2):
        self.T1 = T1
        self.T2 = T2
    
    def evaluate(self, story):
        return self.T1.evaluate(story) or self.T2.evaluate(story)


#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.
    stories is a list of stories, triggerlist is list of triggers
    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    # TODO: Problem 10
    # This is a placeholder
    # (we're just returning all the stories, with no filtering)

    returnlist = []

    for story in stories:
        is_triggered = False
        for trigger in triggerlist:
            if trigger.evaluate(story) == True:
                is_triggered = True
        if is_triggered:
            returnlist.append(story)

    return returnlist



#======================
# User-Specified Triggers
#======================
# Problem 11
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)

    # TODO: Problem 11
    # line is the list of lines that you need to parse and for which you need
    # to build triggers

    # Lines have format %name,%KEYWORD,%Values

    return_triggers = {} ## Dictionary of triggers, in form triggername, Trigger obj

    for line in lines:
        # print("line is " + line)
        keyword_list = line.split(",") 
        # print("keyword list is", keyword_list, "len is", len(keyword_list))
        name_trigger = keyword_list[0].lower()
        type_trigger = keyword_list[1].lower()
        # print("There is no prob")
        value_trigger = keyword_list[2].lower()
        # print("There is 1 prob")
        if len(keyword_list) > 3:
            value2_trigger = keyword_list[3].lower()
        if type_trigger == "description":
            temp_trigger = DescriptionTrigger(value_trigger)
            return_triggers[name_trigger] = temp_trigger
        if type_trigger == "title":
            temp_trigger = TitleTrigger(value_trigger)
            return_triggers[name_trigger] = temp_trigger
        if type_trigger == "before":
            temp_trigger = BeforeTrigger(value_trigger)
            return_triggers[name_trigger] = temp_trigger
        if type_trigger == "after":
            temp_trigger = AfterTrigger(value_trigger)
            return_triggers[name_trigger] = temp_trigger
        if type_trigger == "Not":
            temp_trigger = NotTrigger(return_triggers[value_trigger])
            return_triggers[name_trigger] = temp_trigger
        if type_trigger == "And":
            temp_trigger = AndTrigger(return_triggers[value_trigger], return_triggers[value2_trigger])
            return_triggers[name_trigger] = temp_trigger
        if type_trigger == "Or":
            temp_trigger = OrTrigger(return_triggers[value_trigger], return_triggers[value2_trigger])
            return_triggers[name_trigger] = temp_trigger
        # print("end of for loop")
    return return_triggers.values()




SLEEPTIME = 5 #seconds -- how often we poll

def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        t1 = TitleTrigger("Banana")
        t2 = DescriptionTrigger("Apple")
        t3 = DescriptionTrigger("Orange")
        t4 = AndTrigger(t2, t3)
        triggerlist = [t1, t4]

        # Problem 11
        # TODO: After implementing read_trigger_config, uncomment this line 
        triggerlist = read_trigger_config('triggers.txt')
        
        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/news?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            # stories.extend(process("http://news.yahoo.com/rss/topstories"))

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)


            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()

