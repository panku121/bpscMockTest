"""English language bank: original passages and grammar items."""

from qutil import fixed

def P(passage, questions):
    """questions: list of (q, [a,b,c], answer_index, explain)."""
    out = []
    for q, abc, ans, ex in questions:
        out.append(fixed(
            "en", "reading", q, "",
            abc, abc, ans, ex,
            passage=passage,
        ))
    return out


def build_english():
    bank = []

    bank += P(
        "The school library is quieter than the playground, but it is not empty. "
        "Students come there to read, to finish homework, and sometimes simply to sit where nobody is shouting. "
        "Meera, the librarian, keeps a wooden box near the door. Anyone who finds a torn page or a missing cover drops a note into the box. "
        "On Friday she mends the books herself. She says a repaired book can travel through many more hands than a new one that is left on a high shelf. "
        "Last month the youngest class started a reading hour. They do not have to choose difficult books. They only have to bring back what they borrow.",
        [
            ("Why does Meera keep a wooden box near the door?",
             ["So that students can report damaged books", "So that students can pay a fine", "So that new books can be sold"],
             0, "The passage says notes about a torn page or a missing cover are dropped into the box. So it is for reporting damage."),
            ("What does Meera do on Friday?",
             ["She mends the books", "She closes the library", "She buys new shelves"],
             0, "The passage states: On Friday she mends the books herself."),
            ("Which idea is supported by the passage?",
             ["A repaired book can be used by many readers", "Only difficult books are useful", "The library is always empty"],
             0, "Meera says a repaired book can travel through many more hands. The library is quiet, not empty, and easy books are allowed."),
            ("The word ‘mends’ most nearly means:",
             ["repairs", "throws away", "counts"],
             0, "She mends damaged books, so ‘mends’ means repairs."),
            ("Which of the following is NOT stated in the passage?",
             ["Students must choose difficult books", "There is a reading hour for the youngest class", "Borrowed books are to be brought back"],
             0, "The passage says they do not have to choose difficult books. The other two points are stated. The question asks what is NOT stated, so (A) is correct. (B) and (C) are stated, so the answer is not ‘more than one’."),
        ],
    )

    bank += P(
        "Before the monsoon, the science teacher took her class to the riverbank outside Patna. "
        "The water was low, and the children could see the marks left by the last flood on the trunks of the trees. "
        "She asked them not to throw wrappers into the current. ‘The river does not eat plastic,’ she said. ‘It only carries it to somebody else’s field.’ "
        "They measured the speed of the water by timing a floating leaf between two sticks. "
        "Ravi’s leaf got caught in a clump of grass, so his time was longer than the others. "
        "The teacher did not call it a mistake. She said even a stuck leaf teaches something: water near the bank moves more slowly than water in the middle.",
        [
            ("Where did the class go?",
             ["To the riverbank outside Patna", "To a science museum", "To the Bay of Bengal"],
             0, "The opening sentence places the class on the riverbank outside Patna."),
            ("Why was Ravi’s time longer?",
             ["His leaf got caught in grass", "He started late", "His stick was shorter"],
             0, "The passage says Ravi’s leaf got caught in a clump of grass, so his time was longer."),
            ("What lesson did the teacher draw from the stuck leaf?",
             ["Water near the bank moves more slowly", "Leaves cannot float", "Floods never leave marks"],
             0, "She says water near the bank moves more slowly than water in the middle."),
            ("‘The river does not eat plastic’ suggests that:",
             ["Plastic is carried onward and remains a problem", "The river dissolves every wrapper", "Plastic should be thrown in the middle"],
             0, "She adds that the river carries plastic to somebody else’s field, so the waste is not destroyed."),
            ("Which statement agrees with the passage?",
             ["Flood marks were visible on tree trunks", "The water was already in high flood that day", "The teacher called Ravi’s result a mistake"],
             0, "Marks of the last flood were on the trunks, the water was low, and the teacher did not call it a mistake."),
        ],
    )

    bank += P(
        "A password is not a decoration on a screen. It is a lock. "
        "In the computer period, Mr. Hussain wrote three rules on the board. "
        "First, do not use your name or your date of birth. Second, do not share the password with a friend, even a kind one. "
        "Third, change it when you think someone else may know it. "
        "Anita had been using ‘anita123’ for every account. She laughed, then changed it before the bell. "
        "Mr. Hussain also showed them a message that promised a free mobile phone if they clicked a link. "
        "Nobody in the room received a phone. The link only wanted their passwords. He called this phishing: a trick that wears the clothes of a gift.",
        [
            ("According to the passage, a password is compared to:",
             ["a lock", "a decoration", "a mobile phone"],
             0, "The first lines say a password is not a decoration; it is a lock."),
            ("Which of these is one of Mr. Hussain’s rules?",
             ["Do not share the password with a friend", "Use your date of birth so you remember it", "Click every link that offers a gift"],
             0, "The second rule is not to share the password, even with a kind friend."),
            ("Why did the link not give anyone a phone?",
             ["It was a trick to collect passwords", "The school network was off", "The phones were already sold"],
             0, "The passage says the link only wanted their passwords. It was phishing."),
            ("The phrase ‘wears the clothes of a gift’ means the trick:",
             ["looks like a present", "is kept in a cupboard", "can be worn on the wrist"],
             0, "Phishing is described as a trick that appears to be a gift."),
            ("Anita’s old password was weak mainly because:",
             ["it used her name and simple numbers", "it was written in Hindi", "it had been changed every day"],
             0, "‘anita123’ uses her name and an easy number sequence, which breaks the first rule."),
        ],
    )

    bank += P(
        "On the morning of the annual sports day, the ground was still wet. "
        "The march-past was moved to the paved path, but the sack race stayed on the grass. "
        "Farhan fell twice and still finished, holding the sack around his knees and laughing. "
        "The loudspeaker failed during the relay. A teacher stood at each bend and shouted the names of the teams. "
        "Nobody missed a change of the baton. Afterwards the principal said that a programme is not only what is printed on a card. "
        "It is also what people do when the card is of no help.",
        [
            ("Why was the march-past moved?",
             ["The ground was still wet", "The loudspeaker failed", "Farhan was late"],
             0, "The ground was wet, so the march-past was moved to the paved path."),
            ("What happened to Farhan in the sack race?",
             ["He fell twice and still finished", "He left the race", "He won without falling"],
             0, "The passage says he fell twice and still finished, laughing."),
            ("How did the relay continue when the loudspeaker failed?",
             ["Teachers shouted the team names at the bends", "The race was cancelled", "Students used a microphone from home"],
             0, "A teacher at each bend shouted the names, and the baton changes still happened."),
            ("The principal’s remark means that:",
             ["people should manage when a plan fails", "printed cards are useless at all times", "only the relay matters"],
             0, "He says a programme is also what people do when the printed card cannot help. That is about adapting."),
            ("Which detail is true?",
             ["The sack race remained on the grass", "The relay baton was lost", "The principal cancelled the day"],
             0, "The sack race stayed on the grass. The baton was exchanged, and the day continued."),
        ],
    )

    bank += P(
        "A good program is a set of clear steps, not a pile of clever tricks. "
        "When Sana wrote her first program to find the average of five numbers, she forgot to divide the total by five. "
        "The screen showed a large sum and she thought the computer was angry. "
        "Her teacher pointed to the last line and said, ‘The machine did exactly what you asked. It did not know what you intended.’ "
        "Sana added the missing step, ran the program again, and the average appeared. "
        "She wrote in her notebook: a bug is not an enemy. It is a place where the instruction and the intention do not match.",
        [
            ("What mistake did Sana make?",
             ["She did not divide the total by five", "She used six numbers", "She switched the computer off"],
             0, "She forgot to divide the total by five while finding the average."),
            ("Why did the computer show a large sum?",
             ["It followed her instructions", "It was angry", "The keyboard was broken"],
             0, "The teacher says the machine did exactly what she asked."),
            ("After the correction, the program showed:",
             ["the average", "an error message only", "the names of the students"],
             0, "When she added the missing step, the average appeared."),
            ("In this passage, a ‘bug’ means:",
             ["a mismatch between instruction and intention", "an insect inside the keyboard", "a very large sum"],
             0, "Sana defines a bug as a place where instruction and intention do not match."),
            ("Which sentence best gives the main idea?",
             ["The computer follows steps; unclear steps give the wrong result", "Computers refuse to do arithmetic", "Averages cannot be calculated by a program"],
             0, "The whole story turns on a missing step. The machine was faithful to the written steps."),
        ],
    )

    bank += P(
        "Every Sunday the village market spreads along one street. "
        "Farmers bring vegetables before sunrise, and by noon the best brinjals are gone. "
        "Old Yusuf sells earthen pots under the peepal tree. He does not shout. "
        "People who need a pot already know his place. A new concrete shop nearby plays film songs and sells plastic buckets. "
        "Yusuf says both things are useful: a bucket is light, a pot keeps water cool. "
        "His grandson, who studies in town, helps him count the money in the evening. "
        "The boy once asked him to print a price list. Yusuf replied, ‘My customers can ask me. A list cannot answer.’",
        [
            ("When are the best brinjals usually gone?",
             ["By noon", "Before sunrise", "On Monday"],
             0, "The passage says that by noon the best brinjals are gone."),
            ("Where does Yusuf sell his pots?",
             ["Under the peepal tree", "Inside the concrete shop", "At the school"],
             0, "He sells earthen pots under the peepal tree."),
            ("What difference does Yusuf mention between a bucket and a pot?",
             ["A bucket is light and a pot keeps water cool", "A pot is lighter than a bucket", "A bucket keeps water cool"],
             0, "His words are: a bucket is light, a pot keeps water cool."),
            ("Why does Yusuf refuse a printed price list?",
             ["He says a list cannot answer the customer", "He cannot count money", "His grandson forbids speaking"],
             0, "He says customers can ask him, while a list cannot answer."),
            ("The grandson’s role in the passage is to:",
             ["help count the money in the evening", "play film songs", "bring vegetables before sunrise"],
             0, "The grandson helps him count the money in the evening."),
        ],
    )

    bank += P(
        "During a dust storm the classroom windows were shut, and the fans only moved warm air. "
        "The teacher stopped the lesson on maps and asked the students to list what they could observe without going outside. "
        "They wrote: the sky had turned brown, the neem tree was bending, and the water in the open pot was no longer clear. "
        "Ten minutes later the wind dropped. A thin layer of dust sat on the desks. "
        "The teacher said observation is the first instrument of science. A person who looks carefully has already begun the experiment, even before any tool is picked up.",
        [
            ("Why were the windows shut?",
             ["There was a dust storm", "The fans were new", "The maps were wet"],
             0, "The opening line says the windows were shut during a dust storm."),
            ("What did the students notice about the neem tree?",
             ["It was bending", "It had fallen", "It was being cut"],
             0, "They wrote that the neem tree was bending."),
            ("What sat on the desks after the wind dropped?",
             ["A thin layer of dust", "Drops of rain", "Pieces of the map"],
             0, "A thin layer of dust sat on the desks."),
            ("According to the teacher, the first instrument of science is:",
             ["observation", "a microscope", "a closed window"],
             0, "The teacher says observation is the first instrument of science."),
            ("The water in the pot was no longer clear because:",
             ["dust had entered it", "the students had painted it", "the lesson was about ink"],
             0, "The context is a dust storm. The unclear water is one of the observations caused by the dust."),
        ],
    )

    bank += P(
        "Lata’s bus was late, so she reached the examination hall with twenty minutes already gone. "
        "The invigilator allowed her to sit but did not give extra time. "
        "She did not start with question one. She read the whole paper once, marked the questions she knew, and answered those first. "
        "A long paragraph about the internet looked familiar, yet she left it until the end because it needed slow reading. "
        "When the bell rang she had attempted every short question and half of the paragraph. "
        "On the way home she told her brother, ‘I could not catch the bus, but I could still choose the order of my work.’",
        [
            ("How late was Lata when she sat down?",
             ["Twenty minutes", "Twenty seconds", "She was early"],
             0, "She reached with twenty minutes already gone."),
            ("Did the invigilator give her extra time?",
             ["No", "Yes, twenty minutes", "Yes, until evening"],
             0, "The invigilator allowed her to sit but did not give extra time."),
            ("Why did she leave the long paragraph until the end?",
             ["It needed slow reading", "It was not printed", "Her brother told her to skip it"],
             0, "She left it because it needed slow reading, even though it looked familiar."),
            ("What had she finished when the bell rang?",
             ["Every short question and half of the paragraph", "The entire paper", "Nothing"],
             0, "She had attempted every short question and half of the paragraph."),
            ("The last sentence shows that Lata is talking about:",
             ["using time wisely inside the hall", "buying a faster bus", "leaving the examination"],
             0, "She contrasts missing the bus with still choosing the order of her work. The point is planning under a time limit."),
        ],
    )

    # Grammar and vocabulary. answer index is among A B C, or 3/4 for D/E.
    grammar = [
        ("articles", "She bought ___ orange and ___ umbrella.",
         ["an, an", "a, a", "a, an"], 0,
         "‘Orange’ and ‘umbrella’ both begin with vowel sounds, so ‘an’ is used with each. Hence (A)."),
        ("articles", "___ Ramayana is an epic.",
         ["The", "A", "An"], 0,
         "The name of a particular book takes ‘the’: The Ramayana."),
        ("articles", "He is ___ honest officer.",
         ["an", "a", "the"], 0,
         "‘Honest’ begins with a silent h and a vowel sound, so the article is ‘an’."),
        ("articles", "I saw ___ one-eyed man near the gate.",
         ["a", "an", "the"], 0,
         "‘One’ begins with the sound ‘w’, a consonant sound, so ‘a’ is correct: a one-eyed man."),
        ("articles", "She plays ___ piano in the evening.",
         ["the", "a", "an"], 0,
         "Names of musical instruments take ‘the’ when we speak of playing them: the piano."),
        ("articles", "___ gold is a precious metal.",
         ["No article", "A", "The"], 0,
         "A material noun used in a general sense takes no article: Gold is a precious metal."),
        ("articles", "He returned after ___ hour.",
         ["an", "a", "the"], 0,
         "‘Hour’ begins with a vowel sound, so ‘an hour’."),
        ("articles", "My father is ___ engineer in the water department.",
         ["an", "a", "the"], 0,
         "‘Engineer’ begins with a vowel sound, and the post is not a particular one already known. Use ‘an’."),
        ("prepositions", "The book is lying ___ the table.",
         ["on", "in", "over the idea of"], 0,
         "A thing resting on a surface takes ‘on’: on the table."),
        ("prepositions", "She has been teaching ___ 2018.",
         ["since", "for", "from the last"], 0,
         "‘Since’ is used with a point of time (2018). ‘For’ would need a period, such as ‘for six years’."),
        ("prepositions", "They walked ___ the park for an hour.",
         ["in", "on", "at"], 0,
         "We walk in a park. ‘On the park’ and ‘at the park’ are not the natural choice here."),
        ("prepositions", "He is afraid ___ dogs.",
         ["of", "from", "by"], 0,
         "The adjective ‘afraid’ takes the preposition ‘of’."),
        ("prepositions", "The train arrived ___ the platform.",
         ["at", "to", "on the idea"], 0,
         "A train arrives at a platform or station. ‘Arrive’ is not followed by ‘to’."),
        ("prepositions", "Divide the sweets ___ the four children.",
         ["among", "between", "into the hands of only two"], 0,
         "‘Among’ is used for more than two people. ‘Between’ is for two."),
        ("prepositions", "She cut the apple ___ a knife.",
         ["with", "by", "from"], 0,
         "An instrument takes ‘with’: with a knife. ‘By’ would introduce an agent in the passive."),
        ("prepositions", "I prefer tea ___ coffee.",
         ["to", "than", "from"], 0,
         "‘Prefer’ is followed by ‘to’, not ‘than’: prefer tea to coffee."),
        ("tenses", "The earth ___ round the sun.",
         ["revolves", "revolved", "is revolving yesterday"], 0,
         "A permanent truth is stated in the simple present: revolves."),
        ("tenses", "She ___ to school when the rain started.",
         ["was going", "goes", "will go"], 0,
         "An action in progress in the past takes the past continuous: was going."),
        ("tenses", "I ___ him yesterday.",
         ["met", "have met", "meet"], 0,
         "‘Yesterday’ is a finished time, so the simple past ‘met’ is used, not the present perfect."),
        ("tenses", "By next June she ___ her training.",
         ["will have completed", "completed", "has completed"], 0,
         "A future action finished before a future point uses the future perfect: will have completed."),
        ("tenses", "He ___ here since Monday.",
         ["has been living", "is living yesterday", "lived since"], 0,
         "An action continuing from a past point till now uses the present perfect continuous with ‘since’."),
        ("tenses", "If you heat ice, it ___.",
         ["melts", "melted", "would melted"], 0,
         "A general conditional fact uses the simple present in both clauses: if you heat ice, it melts."),
        ("tenses", "When I reached the station, the train ___.",
         ["had left", "has left", "leaves tomorrow"], 0,
         "The train left before I reached, so the earlier past action is past perfect: had left."),
        ("tenses", "Look at those clouds. It ___ now.",
         ["is raining", "rained", "rain"], 0,
         "The situation is happening at the moment of speaking, so the present continuous is natural if rain has begun. ‘It is raining’ matches ‘look’."),
        ("vocabulary", "Choose the synonym of ‘brief’.",
         ["short", "angry", "bright"], 0,
         "‘Brief’ means short in time or words."),
        ("vocabulary", "Choose the synonym of ‘ancient’.",
         ["old", "future", "tiny"], 0,
         "‘Ancient’ means belonging to the distant past; ‘old’ is the nearest of the three."),
        ("vocabulary", "Choose the synonym of ‘rapid’.",
         ["quick", "slow", "heavy"], 0,
         "‘Rapid’ means quick or fast."),
        ("vocabulary", "Choose the antonym of ‘expand’.",
         ["contract", "increase", "spread"], 0,
         "‘Expand’ means to grow larger. Its opposite is ‘contract’."),
        ("vocabulary", "Choose the antonym of ‘scarce’.",
         ["plentiful", "rare", "little"], 0,
         "‘Scarce’ means in short supply. The opposite is ‘plentiful’."),
        ("vocabulary", "Choose the antonym of ‘victory’.",
         ["defeat", "prize", "joy"], 0,
         "The opposite of victory is defeat."),
        ("vocabulary", "A person who can speak two languages is called:",
         ["bilingual", "illiterate", "translator only by birth"], 0,
         "‘Bi-’ means two and ‘lingual’ refers to languages: bilingual."),
        ("vocabulary", "A place where books are kept for reading is a:",
         ["library", "laboratory", "granary"], 0,
         "A library keeps books. A laboratory is for experiments and a granary for grain."),
        ("vocabulary", "‘Benevolent’ most nearly means:",
         ["kind", "cruel", "silent"], 0,
         "A benevolent person wishes to do good; the nearest word here is kind."),
        ("vocabulary", "Choose the correctly spelt word.",
         ["accommodation", "accomodation", "acommodation"], 0,
         "The standard spelling is accommodation: two c’s and two m’s."),
        ("vocabulary", "Choose the correctly spelt word.",
         ["committee", "commitee", "comittee"], 0,
         "Committee has two m’s, two t’s and two e’s at the end."),
        ("vocabulary", "Choose the correctly spelt word.",
         ["receive", "recieve", "receeve"], 0,
         "The rule ‘i before e except after c’ gives receive."),
        ("voice", "Change to passive: ‘She writes a letter.’",
         ["A letter is written by her.", "A letter was written by her.", "A letter wrote her."], 0,
         "Simple present passive: object + is/are + past participle. A letter is written by her."),
        ("voice", "Change to passive: ‘The boys were playing cricket.’",
         ["Cricket was being played by the boys.", "Cricket is played by the boys.", "Cricket played the boys."], 0,
         "Past continuous passive: was/were + being + past participle."),
        ("voice", "Change to active: ‘The song was sung by Lata.’",
         ["Lata sang the song.", "Lata was sung by the song.", "The song sang Lata."], 0,
         "The agent ‘by Lata’ becomes the subject, and the simple past ‘sang’ replaces ‘was sung’."),
        ("voice", "‘Open the window.’ In the passive it becomes:",
         ["Let the window be opened.", "The window opened you.", "Window is open by you yesterday."], 0,
         "An imperative is often made passive with ‘let + object + be + past participle’."),
        ("error", "Which sentence is correct?",
         ["Each of the boys has a pen.", "Each of the boys have a pen.", "Each of the boys having a pen."], 0,
         "‘Each’ is singular, so the verb is ‘has’, not ‘have’."),
        ("error", "Which sentence is correct?",
         ["He is senior to me.", "He is senior than me.", "He is senior from me."], 0,
         "‘Senior’, ‘junior’, ‘superior’ and ‘prefer’ take ‘to’, not ‘than’."),
        ("error", "Which sentence is correct?",
         ["One of the students was absent.", "One of the students were absent.", "One of the student were absent."], 0,
         "‘One of’ takes a plural noun and a singular verb: one of the students was absent."),
        ("error", "Which sentence is correct?",
         ["Neither Ravi nor his friends are ready.", "Neither Ravi nor his friends is ready.", "Neither Ravi or his friends is ready."], 0,
         "With ‘neither…nor’, the verb agrees with the nearer subject. ‘Friends’ is plural, so ‘are’. The pair is ‘nor’, not ‘or’."),
        ("error", "Find the sentence with an error.",
         ["She discussed about the plan.", "She discussed the plan.", "They described the picture."], 0,
         "‘Discuss’ is not followed by ‘about’. ‘Discussed the plan’ is correct, so (A) has the error."),
        ("error", "Find the sentence with an error.",
         ["He returned back from Delhi.", "He returned from Delhi.", "He came back from Delhi."], 0,
         "‘Return’ already means come back, so ‘returned back’ is redundant. (A) is wrong."),
        ("error", "Choose the correct question tag: ‘You are a teacher, ___?’",
         ["aren’t you", "are you", "isn’t it"], 0,
         "A positive statement takes a negative tag, and the pronoun matches ‘you’: aren’t you."),
        ("error", "‘If I ___ a bird, I would fly.’ The blank takes:",
         ["were", "am", "was being"], 0,
         "An unreal present wish uses ‘were’ for every person: If I were a bird."),
        ("narration", "She said, ‘I am tired.’ In indirect speech:",
         ["She said that she was tired.", "She said that I am tired.", "She said that she is tired yesterday."], 0,
         "The present ‘am’ shifts to ‘was’, and the pronoun ‘I’ becomes ‘she’."),
        ("narration", "He said to me, ‘Where do you live?’",
         ["He asked me where I lived.", "He asked me where do you live.", "He said me where I live."], 0,
         "A question in indirect speech uses ‘asked’ and statement order: where I lived. There is no ‘said me’."),
        ("narration", "The teacher said, ‘The earth moves round the sun.’",
         ["The teacher said that the earth moves round the sun.", "The teacher said that the earth moved round the sun.", "The teacher told that earth moved."], 0,
         "A universal truth does not shift its tense in indirect speech."),
        ("prepositions", "He died ___ cholera.",
         ["of", "from", "by"], 0,
         "We say ‘die of’ a disease: died of cholera."),
        ("prepositions", "The cat jumped ___ the wall.",
         ["over", "under the sky of", "between"], 0,
         "To go from one side to the other above the wall, the natural preposition is ‘over’."),
        ("articles", "___ Himalayas lie to the north of India.",
         ["The", "A", "An"], 0,
         "Names of mountain ranges take ‘the’: the Himalayas."),
        ("tenses", "I ___ my work before the guests arrived.",
         ["had finished", "have finished", "finish"], 0,
         "The work was completed before another past event, so past perfect ‘had finished’ is required."),
        ("vocabulary", "Choose the synonym of ‘diligent’.",
         ["hard-working", "lazy", "angry"], 0,
         "A diligent person works with steady care. The nearest word is hard-working."),
        ("vocabulary", "Choose the antonym of ‘permanent’.",
         ["temporary", "lasting", "fixed"], 0,
         "The opposite of permanent is temporary."),
        ("vocabulary", "A speech made without preparation is:",
         ["impromptu", "manuscript", "silent"], 0,
         "An impromptu speech is given without prior preparation."),
        ("vocabulary", "‘Fragile’ most nearly means:",
         ["easily broken", "very heavy", "newly painted"], 0,
         "Fragile means delicate and easily broken."),
        ("error", "Which sentence is correct?",
         ["The news is true.", "The news are true.", "The news were true in plural form always."], 0,
         "‘News’ is an uncountable noun and takes a singular verb: the news is true."),
        ("error", "Which sentence is correct?",
         ["Mathematics is his favourite subject.", "Mathematics are his favourite subject.", "Mathematics were a subjects."], 0,
         "Names of subjects such as mathematics take a singular verb."),
        ("voice", "Change to passive: ‘Someone has stolen my pen.’",
         ["My pen has been stolen.", "My pen had stolen.", "My pen is steal by someone."], 0,
         "Present perfect passive: has/have been + past participle. The agent ‘someone’ may be omitted."),
        ("narration", "Mother said to the child, ‘Do not waste water.’",
         ["Mother advised the child not to waste water.", "Mother said the child do not waste water.", "Mother told that waste water."], 0,
         "A negative command becomes ‘advised/told + not to + verb’."),
        ("prepositions", "He is good ___ mathematics.",
         ["at", "in the talent of", "on"], 0,
         "We are ‘good at’ a subject or skill."),
        ("articles", "She is ___ M.A. in history.",
         ["an", "a", "the"], 0,
         "‘M’ is pronounced ‘em’, a vowel sound, so ‘an M.A.’"),
        ("tenses", "They ___ football every Sunday.",
         ["play", "plays", "is playing"], 0,
         "A habitual action with a plural subject takes the simple present plural: play."),
        ("vocabulary", "Choose the synonym of ‘conceal’.",
         ["hide", "reveal", "open"], 0,
         "To conceal is to hide."),
        ("vocabulary", "Choose the antonym of ‘arrival’.",
         ["departure", "coming", "entrance"], 0,
         "The opposite of arrival is departure."),
        ("error", "Which sentence is correct?",
         ["Between you and me, he is wrong.", "Between you and I, he is wrong.", "Between you and myself are wrong."], 0,
         "A preposition takes the object form: between you and me. ‘I’ is a subject form."),
        ("voice", "Change to active: ‘A cake was made by grandmother.’",
         ["Grandmother made a cake.", "A cake made grandmother.", "Grandmother was made a cake."], 0,
         "The agent becomes the subject and the verb becomes simple past: Grandmother made a cake."),
        ("reading_skill", "Choose the best connective: ‘He was tired; ___, he finished the work.’",
         ["nevertheless", "because", "although he finished already"], 0,
         "The second clause contrasts with the first. ‘Nevertheless’ marks that contrast."),
        ("reading_skill", "‘The hall was packed.’ ‘Packed’ here means:",
         ["full of people", "closed with a lock", "painted"],
         0, "When a hall is packed, it is completely full."),
        # D / E traps
        ("articles", "Which of the following is correct?",
         ["an hour", "an honest man", "a hour"],
         3, "(A) and (B) are both correct because ‘hour’ and ‘honest’ begin with vowel sounds. (C) is wrong. Hence more than one, (D)."),
        ("prepositions", "Which of the following is correct?",
         ["prefer tea to coffee", "afraid of dogs", "senior than me"],
         3, "(A) and (B) follow the right prepositions. ‘Senior’ takes ‘to’, not ‘than’, so (C) is wrong. Answer (D)."),
        ("tenses", "Which of the following is correct?",
         ["I met him yesterday.", "She has met him yesterday.", "The earth revolved round the sun as a daily habit worded that way."],
         0, "(A) is correct. Present perfect does not take ‘yesterday’, so (B) is wrong. (C) is not a valid sentence. Only (A) stands."),
        ("vocabulary", "Which of the following pairs is an antonym pair?",
         ["victory – defeat", "scarce – plentiful", "ancient – old"],
         3, "(A) and (B) are antonym pairs. (C) is closer to a synonym pair. So more than one of (A) and (B), answer (D)."),
        ("error", "Which of the following sentences is wrong?",
         ["Discuss about the matter.", "Returned back home.", "The news is true."],
         3, "(A) and (B) are both wrong usage. (C) is correct. The question asks which is wrong, and two are wrong, so (D)."),
        ("voice", "Which change into the passive is acceptable?",
         ["A letter is written by her.", "Cricket was being played by the boys.", "She writes a letter by passive without change."],
         3, "(A) and (B) are proper passive forms. (C) is not a passive sentence. Answer (D)."),
        ("narration", "Which indirect sentence is correct?",
         ["She said that she was tired.", "He asked me where I lived.", "She said that I am tired while pointing to herself in the same words."],
         3, "(A) and (B) follow the rules of narration. (C) keeps the wrong pronoun and tense. Answer (D)."),
        ("vocabulary", "Which spelling is wrong?",
         ["accomodation", "recieve", "committee"],
         3, "Both ‘accomodation’ and ‘recieve’ are misspelt. ‘Committee’ is correct. Two are wrong, so (D)."),
        ("articles", "Choose the sentence that needs no article before the noun in italics, shown here in plain words: ‘Gold is costly.’ Which statement is true?",
         ["Material nouns in a general sense take no article", "‘The gold is a precious metal’ is always required", "‘A gold’ is used for the metal in general"],
         0, "A material noun used generally takes no article. (B) and (C) overstate the rule."),
        ("prepositions", "None of these is a correct English sentence. Choose accordingly.",
         ["He discussed about the plan.", "He is senior than me.", "She returned back yesterday."],
         4, "All three sentences are incorrect. ‘Discuss’ takes no ‘about’, ‘senior’ takes ‘to’, and ‘return’ does not take ‘back’. None of (A)–(C) is correct, so (E)."),
        ("tenses", "None of these fits a universal truth. Choose accordingly.",
         ["The sun rose in the east every eternal day as a past habit only.", "The sun is rising in the east yesterday.", "The sun had risen in the east as a definition."],
         4, "A universal truth is ‘The sun rises in the east.’ None of these wordings is that sentence, so (E)."),
    ]

    for topic, q, abc, ans, ex in grammar:
        bank.append(fixed("en", topic, q, "", abc, abc, ans, ex))

    # unique stems
    seen = set()
    out = []
    for item in bank:
        key = item["q"] + "|" + item.get("passage", "")[:40]
        if key in seen:
            continue
        seen.add(key)
        out.append(item)
    return out


if __name__ == "__main__":
    b = build_english()
    print("english", len(b), "passages", sum(1 for x in b if x["passage"]))
