# Part 1 -> data base creation
import difflib

class Discovery:
    discoveries = []
    discovery_words = ["discovery", "what", "dicoveries"]
    year_words = ["when", "when", "discovered", "discovered", "year", "what time", "year", "discovery"]
    explain_words = ["explain", "define", "definition", "theory", "explanation","introduce"]
    class_discovery_words = []
    class_discovery_dict = {}
    disc_year = {}
    disc_exp = {}
    splitted_words = []

    def __init__(self, discovery, year, explanation):
        self.discovery = discovery
        self.year = year
        self.explanation = explanation

    def main_instance(self):
        self.add_discovery()
        self.add_dict()

    @classmethod
    def main_class(cls):
        cls.split_words()
        cls.combine_class_words()
        cls.add_split_data()
        cls.dict_for_methods()

    @classmethod
    def dict_for_methods(cls):
        cls.class_discovery_dict["discovery"] = cls.discovery_words
        cls.class_discovery_dict["year"] = cls.year_words
        cls.class_discovery_dict["explain"] = cls.explain_words

    @classmethod
    def add_split_data(cls):
        cls.discovery_words.extend(cls.splitted_words)
        cls.year_words.extend(cls.splitted_words)
        cls.explain_words.extend(cls.splitted_words)

    # done
    @classmethod
    def combine_class_words(cls):
        cls.class_discovery_words.extend(cls.year_words)
        cls.class_discovery_words.extend(cls.explain_words)
        cls.class_discovery_words.extend(cls.discovery_words)
        cls.class_discovery_words.extend(cls.splitted_words)

    # done
    @classmethod
    def split_words(cls):
        cls.splitted_words = [word for sentence in Discovery.discoveries for word in sentence.split()]

    # done
    def add_discovery(self):
        Discovery.discoveries.append(self.discovery)

    # done
    def add_dict(self):
        Discovery.disc_year[self.discovery] = self.year
        Discovery.disc_exp[self.discovery] = self.explanation

text_d_1=""""In this, space and time were no longer absolute, no longer 
a fixed backgroundto events. Instead, they were dynamical quantities 
that were shaped by thematter and energy in the universe. They were 
defined only within theuniverse, so it made no sense to talk of a time
before the universe began."""
text_d_2=""""By an analysis of the light from other galaxies, Hubble was able to measure
whether they were moving towards us or away. To his great surprise, he
found they were nearly all moving away. Moreover, the further they were
from us, the faster they were moving away. In other words, the universe is
expanding. Galaxies are moving away from each other.If the
galaxies are moving apart, they must have been closer together in the past."""
text_d_3="""The universe would have existed for ever, andwould have looked the same at all times. This last property had the great
virtue of being a definite prediction that could be tested by observation.For many reasonfs the steady-state theory was abandoned."""
text_d_4="""If
you ever set your television to an empty channel, a few per cent of the snowyou saw on the screen was caused by this background of microwaves. The
only reasonable interpretation of the background is that it is radiation left
over from an early very hot and dense state. As the universe expanded, the
radiation would have cooled until it is just the faint remnant we observe
today.
That the universe began with a singularity was not an idea that I or a
number of other people were happy with."""
text_d_5="""One cannot accurately predict both the position and the speed
of a particle. The more accurately the position is predicted, the less
accurately you will be able to predict the speed, and vice versa."""
# instances
relativity=Discovery(discovery="theory of relativity", year=1915,
                    explanation=text_d_1)
relativity.main_instance()
expansion_of_universe=Discovery(discovery="expansion of the universe", year=1929,
                    explanation=text_d_1)
expansion_of_universe.main_instance()
stead_state=Discovery(discovery="steady-state theory", year=1948,
                    explanation=text_d_3)
stead_state.main_instance()
universe_beginning=Discovery(discovery="the universe has beginning", year=1965,
                    explanation=text_d_4)
universe_beginning.main_instance()
uncertainty_principle=Discovery(discovery="uncertainity principle", year=1927,
                    explanation=text_d_5)
uncertainty_principle.main_instance()
Discovery.main_class()





class Scientist:
    scientists = [] # ok
    name_words = ["name", "full", "what", "called", "surname", "who", "scientists",
                  "mentioned", "who", "who", "names"] #ok
    born_words = ["where", "which", "country", "nationality", "born", "born"] #ok
    god_words = ["god", "believe", "does", "belief"] #ok
    class_scientist_words = []
    class_scientist_dict = {}
    dict_name_born = {}
    dict_name_god = {}
    scientists_split = []

    def __init__(self, name, born, god_exist):
        self.name = name
        self.born = born
        self.god_exist = god_exist

    def main_instance(self):
        self.add_scientist() # done
        self.add_dict() # done

    @classmethod
    def main_class(cls):
        cls.split_words() # done
        cls.combine_class_words() # done
        cls.add_split_data() # done
        cls.dict_for_methods() # done

    @classmethod
    def dict_for_methods(cls):
        cls.class_scientist_dict["name"] = cls.name_words
        cls.class_scientist_dict["born"] = cls.born_words
        cls.class_scientist_dict["god"] = cls.god_words

    @classmethod
    def add_split_data(cls):
        cls.name_words.extend(cls.scientists_split)
        cls.born_words.extend(cls.scientists_split)
        cls.god_words.extend(cls.scientists_split)

    # done
    @classmethod
    def combine_class_words(cls):
        cls.class_scientist_words.extend(cls.name_words)
        cls.class_scientist_words.extend(cls.born_words)
        cls.class_scientist_words.extend(cls.god_words)
        cls.class_scientist_words.extend(cls.scientists_split)

    # done
    @classmethod
    def split_words(cls):
        cls.scientists_split = [word for sentence in Scientist.scientists for word in sentence.split()]

    # done
    def add_scientist(self):
        self.scientists.append(self.name)

    def add_dict(self):
        Scientist.dict_name_born[self.name] = self.born
        Scientist.dict_name_god[self.name] = self.god_exist
# instances
einstein=Scientist("albert einstein", "germany", True)
einstein.main_instance()
hawking=Scientist("stieven hawking", "england", False)
hawking.main_instance()
hubble=Scientist("Edwin Hubble", "american", False)
hubble.main_instance()
bondi=Scientist("herman bondi", "austrain", True)
bondi.main_instance()
gold=Scientist("thomas gold", "austrain-british", None)
gold.main_instance()
hoyle=Scientist("Fred Hoyle", "english", False)
hoyle.main_instance()
penrose=Scientist("Roger Penrose", "british", False)
penrose.main_instance()
heisenberg=Scientist("laureate Werner Heisenberg", "german", True)
heisenberg.main_instance()
Scientist.main_class()


class Hawking(Scientist):
    profession = ["physicist, cosmologist,"]
    will = "To research and try to answer the many questions that science asks us."
    discoveries = []
    quotes = ["God did Not Create Universe",
              "My work is about finding a rational framework tounderstand the universe around us"]
    believe = ["science", "laws of nature"]

    def __init__(self, name):
        # Call the constructor of the base class (Scientist)
        super().__init__(name, "england", False)

    def say_quotes(self):
        pass

    def believe_in(self):
        return "Everything can be explained another way, by the laws of nature."

hawking=Hawking("Stieven Hawking")


class Science:
    scientific_events = {}
    class_science_words=["science", "scientific", "scientists", "and", "discoveries"
                          "intoduce", "which", "what", "list", "list", "list",
                         "science", "scientist", "science", "science", "science",
                         "albert", "einstein", "stieven", "hawking", "herman", "bondi",
                         "edwin" ,"hubble", "thomas"," gold", "Fred ","Hoyle",
                         "Roger"," Penrose", "laureate","Werner", "Heisenberg",
                         "scientific"]

    def __init__(self, scientist, discovery):
        self.scientist = scientist
        self.discovery = discovery

    @classmethod
    def main_class(cls):
        cls.combine_class_words()

    @classmethod
    def combine_class_words(cls):
        cls.class_science_words.extend(Discovery.discovery_words)
        cls.class_science_words.extend(Scientist.name_words)



    def combination(self):
        # creates dict of science and the scientist
        key, value = self.scientist, self.discovery
        Science.scientific_events[key] = value


# instances
science_instance_1 = Science(einstein.name, relativity.discovery)
science_instance_1.combination()
science_instance_2 = Science(hawking.name, universe_beginning.discovery)
science_instance_2.combination()
science_instance_3 = Science(hubble.name, expansion_of_universe.discovery)
science_instance_3.combination()
science_instance_4 = Science(gold.name, stead_state.discovery)
science_instance_4.combination()
science_instance_5 = Science(bondi.name, stead_state.discovery)
science_instance_5.combination()
science_instance_6 = Science(hoyle.name, stead_state.discovery)
science_instance_6.combination()
science_instance_7 = Science(heisenberg.name, uncertainty_principle.discovery)
science_instance_7.combination()
# Science.main_class()

print(Science.scientific_events)

class Universe:
    ingredient_words=["matter", "energy", "space", "ingredients", "universe",
                      "ingredients", "ingredients", "ingredients"]
    consist_word=["galaxies","stars","planets,black holes", "universe"
                  "consist", "of", "consists" ]
    creation_word=["created", "creation", "big bang", "how", "appear", "create",
                   "idea", "universe"]
    class_universe_words=[]
    class_universe_dict={}
    def __init__(self, ingredients, consists_of, creation):
        self.ingredients = ingredients
        self.consists_of = consists_of
        self.creation = creation

    @classmethod
    def main_class(cls):
        cls.combine_class_words()
        cls.dict_for_methods()

    def ingredient(self, ing, question=None):
        has_mass = None
        examples = None
        description = None
        if ing == self.ingredients[0]:
            if question == "mass":
                has_mass = True
                return has_mass
            elif question == "examples":
                examples = ["rock", "ice", "liquids", "stars"]
                return examples
            elif question == "description":
                description = "All around us"
                return description
        elif ing == self.ingredients[1]:
            if question == "mass":
                has_mass = False
                return has_mass
            elif question == "examples":
                examples = ["Sun energy on your face", "Stars"]
                return examples
            elif question == "description":
                description = "Driving the processes that keep it a dynamic"
                return description
        elif ing == self.ingredients[2]:
            if question == "mass":
                has_mass = False
                return has_mass
            elif question == "description":
                description = "AStretching in all directions."
                return description
        else:
            print("This book does not contain that answer.")

    @classmethod
    def combine_class_words(cls):
        cls.class_universe_words.extend(cls.ingredient_words)
        cls.class_universe_words.extend(cls.consist_word)
        cls.class_universe_words.extend(cls.creation_word)

    @classmethod
    def dict_for_methods(cls):
        cls.class_universe_dict["ingredients"] = cls.ingredient_words
        cls.class_universe_dict["consist of"] = cls.consist_word
        cls.class_universe_dict["creation"] = cls.creation_word




uni=Universe(["matter", "energy", "space"], ["galaxies","stars",
                                             "planets,black holes"],
            ["spontaneously created out of nothing from Big Bang"])

Universe.main_class()


class God:
    believe_words=["believe", "not atheist", "religious", "god"]
    not_believe_words=["atheist", "not believe", "not religious"]
    class_god_words=[]
    class_god_dict={}
    believed_by = []
    not_believed_by = []
    unknown = []

    def __init__(self, scientist_name, has_belief):
        self.scientist_name = scientist_name
        self.has_belief = has_belief

    def scientist_sort(self):
        if self.has_belief == True:
            God.believed_by.append(self.scientist_name)
        elif self.has_belief == False:
            God.not_believed_by.append(self.scientist_name)
        else:
            God.unknown.append(self.scientist_name)

    @classmethod
    def main_class(cls):
        cls.combine_class_words()
        cls.dict_for_methods()

    @classmethod
    def combine_class_words(cls):
        cls.class_god_words.extend(cls.believe_words)
        cls.class_god_words.extend(cls.not_believe_words)

    @classmethod
    def dict_for_methods(cls):
        cls.class_god_dict["believer"] = cls.believe_words
        cls.class_god_dict["not believer"] = cls.not_believe_words

god_sort_1=God(einstein.name, einstein.god_exist)
god_sort_1.scientist_sort()
god_sort_2=God(hawking.name, hawking.god_exist)
god_sort_2.scientist_sort()
god_sort_3=God(hubble.name, hubble.god_exist)
god_sort_3.scientist_sort()
god_sort_4=God(bondi.name, bondi.god_exist)
god_sort_4.scientist_sort()
god_sort_5=God(gold.name, gold.god_exist)
god_sort_5.scientist_sort()
god_sort_6=God(hoyle.name, hoyle.god_exist)
god_sort_6.scientist_sort()
god_sort_7=God(penrose.name, penrose.god_exist)
god_sort_7.scientist_sort()
god_sort_8=God(heisenberg.name, heisenberg.god_exist)
god_sort_8.scientist_sort()

God.main_class()

# Bag of words
bag_of_words=[]
bag_of_words.extend(Discovery.class_discovery_words)
bag_of_words.extend(Scientist.class_scientist_words)
bag_of_words.extend(Universe.class_universe_words)
bag_of_words.extend(God.class_god_words)
bag_of_words.extend(Science.class_science_words)
bag_of_dicts = {
    "discovery": Discovery.class_discovery_words,
    "scientist": Scientist.class_scientist_words,
    "science": Science.class_science_words,
    "universe": Universe.class_universe_words,
    "god": God.class_god_words}

# print(God.class_god_words)
keys = list(bag_of_dicts.keys())
# print(Scientist.name_words)

# Engine

def g_method(weights,lst):
    max_key = max(weights, key=weights.get)
    if max_key == "believer":
        print(God.believed_by)
    elif max_key == "not believer":
        print(God.not_believed_by)


def u_method(weights,lst):
    max_key = max(weights, key=weights.get)
    if max_key == "ingredients":
        print(uni.ingredients)
    elif max_key == "consist of":
        print(uni.consists_of)
    elif max_key == "creation":
        print(uni.creation)
    elif max_key == "other":
        for word in lst:
            # print("I am here")
            # print(word)
            for key in Scientist.dict_name_god.keys():
                # print(key)
                similarity_ratio = difflib.SequenceMatcher(None, word, key).ratio()
                if similarity_ratio > 0.4:
                    # print(similarity_ratio)
                    # print(key)
                    print(Scientist.dict_name_god[key])
                    return True

def s_method(lst):
    for word in lst:
        for n in Science.scientific_events.keys():
            similarity_ratio = difflib.SequenceMatcher(None, n, word).ratio()
            if similarity_ratio > 0.4:
                # print(similarity_ratio)
                print(Science.scientific_events[n])
                return True
            else:
                if word in ["matter", "space", "energy", "mass", "does", "have"]:
                    Universe.ingredient()
                # else:
                #     print("The answer is not mentioned in this book")
    print(Science.scientific_events)

def st_method(weights,lst):
    max_key = max(weights, key=weights.get)
    if max_key == "name":
        print(Scientist.scientists)
    elif max_key == "born":
        for word in lst:
            for key in Scientist.dict_name_born.keys():
                similarity_ratio = difflib.SequenceMatcher(None, word, key).ratio()
                if similarity_ratio > 0.4:
                    # print(similarity_ratio)
                    print(Scientist.dict_name_born[key])
                    return True
    elif max_key == "god":
        for word in lst:
            # print("I am here")
            # print(word)
            for key in Scientist.dict_name_god.keys():
                # print(key)
                similarity_ratio = difflib.SequenceMatcher(None, word, key).ratio()
                if similarity_ratio > 0.2:
                    # print(similarity_ratio)
                    # print(key)
                    print(Scientist.dict_name_god[key])
                    return True

def d_method(weights, lst):
    max_key = max(weights, key=weights.get)
    if max_key == "discovery":
        print(Discovery.discoveries)
    elif max_key == "year":
        for word in lst:
            for key in Discovery.disc_year.keys():
                similarity_ratio = difflib.SequenceMatcher(None, word, key).ratio()
                if similarity_ratio > 0.3:
                    # print(similarity_ratio)
                    print(Discovery.disc_year[key])
                    return True
    elif max_key == "explain":
        for word in lst:
            for key in Discovery.disc_exp.keys():
                similarity_ratio = difflib.SequenceMatcher(None, word, key).ratio()
                if similarity_ratio > 0.3:
                    # print(similarity_ratio)
                    print(Discovery.disc_exp[key])
                    return True


def method(l, keys, dict):
    methods={}
    for key in keys:
        points=0
        for input in l:
            for word in dict[key]:
                  if input==word:
                      points+=1
            methods[key]=points

    return methods
    # method_3(methods,l)



# defines by weights for each class
def connect(lst_words, dict, keys):
    weights={}
    for key in keys:
          point=0
#         print(key)
          for word in lst_words:
#             print(word)
              for value in dict[key]:
                  if word == value:
                        point+=1

          weights[key]=point
    print(weights)
    max_key = max(weights, key=weights.get)
    if max_key == "discovery":
        d=method(lst_words, Discovery.class_discovery_dict.keys(), Discovery.class_discovery_dict)
        d_method(d, lst_words)
    elif max_key == "scientist":
        d = method(lst_words, Scientist.class_scientist_dict.keys(), Scientist.class_scientist_dict)
        st_method(d, lst_words)
    elif max_key == "science":
        s_method(lst_words)
    elif max_key == "universe":
        d=method(lst_words, Universe.class_universe_dict.keys(), Universe.class_universe_dict)
        u_method(d, lst_words)
    elif max_key == "god":
        d = method(lst_words, God.class_god_dict.keys(), God.class_god_dict)
        g_method(d, lst_words)
    # method(weights,lst_words)

# if finds matching words then passes for the next function to
# determine the class
def engine(user_input, classes):
    matched_words=[]
    for index,word in enumerate(classes):
        for words in user_input:
              similarity_ratio = difflib.SequenceMatcher(None, word, words).ratio()
              if similarity_ratio > 0.7:
                       matched_words.append(word)
    if len(matched_words)>0:
        connect(matched_words, bag_of_dicts, keys)
    else:
        return "This book does not contain such information.Ask something else."


def remove_symbols(input_string):
    # Define a translation table with None for all symbol characters
    translation_table = str.maketrans('', '', "!@#$%^&*()_-+=<>?/.,;:'\"[]{}\\|`~")

    # Use translate to remove symbols
    cleaned_string = input_string.translate(translation_table)
    return cleaned_string


# Example usage
# Where was born Albert Einstein?
# Explain the theory of relativity ?
# What disoveries are mentioined in this book ?
# What are the ingredients of the Universe ?
# where was born Hawking ?
# did gold believe in god ?




# User inptut
user_input = input("Ask what interests you in this book: ")
print(user_input)
result_1 = remove_symbols(user_input)
question = user_input.lower().split()
result = engine(question , bag_of_words)
print(result)
