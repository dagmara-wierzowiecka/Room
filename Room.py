import gym
import numpy as np
from gym import envs, spaces
import random

max_relax = 50
max_arousal = 50

# user policy
# TODO implementacja klasy użytkownika tak, żeby można było za jej pomocą utworzyć 3-6 obiektów przykładowych użytkowników na podstawie konkretnych respondentów z ankiety
class User(gym.Env):
    def generateRandomArousalRelax(self, max_arousal=max_arousal, max_relax=max_relax):
        # losowanie nastroju użytkownika
        current_arousal = round(random.randrange(0, max_arousal), 2)
        print("Initial arousal = ", current_arousal)
        current_relax = round(random.randrange(0, max_relax), 2)
        print("Initial relax = ", current_relax)

        return [current_arousal, current_relax]

    # zwraca numeryczną wartość nastroju na podstawie poziomu current_arousal i current_relax
    def getMoodNumber(self):
        if self.current_relax < max_relax / 2:
            if self.current_arousal < max_arousal / 2:
                current_mood = 0
            else:
                current_mood = 1
        else:
            if self.current_arousal < max_arousal / 2:
                current_mood = 3
            else:
                current_mood = 2

        return current_mood

    # zwraca słowną nazwę nastroju na podstawie wartości numerycznej 0-3
    def getMoodName(self):
        if self.current_mood == 0:
            mood_name = "STRESSED, DROWSY :("
        if self.current_mood == 1:
            mood_name = "Initial mood: STRESSED, AROUSED :<"
        if self.current_mood == 2:
            mood_name = "Initial mood: RELAXED, AROUSED :D"
        if self.current_mood == 3:
            mood_name = ("Initial mood: RELAXED, DROWSY :)")

        return mood_name

    def __init__(self, age, name, target_mood, preferences_set=[]):
        self.preferences_set = []
        self.age = age
        self.name = name
        self.preferences_set = preferences_set
        [self.current_arousal, self.current_relax] = self.generateRandomArousalRelax()
        self.current_mood = self.getMoodNumber()
        self.target_mood = target_mood
        self.step_mood = target_mood
        print(self.name)
        print("Current mood: ", self.getMoodName())

        # return self.current_arousal, self.current_relax, self.current_mood

    def reset(self, age, name, target_mood, preferences_set=[]):
        self.preferences_set = []
        self.age = age
        self.name = name
        self.preferences_set = preferences_set
        [self.current_arousal, self.current_relax] = self.generateRandomArousalRelax()
        self.current_mood = self.getMoodNumber()
        self.target_mood = target_mood
        self.step_mood = target_mood

        return self.current_arousal, self.current_relax, self.current_mood

    def step(self):  # TODO jak w sumie działa wywoływanie tej funkcji, czy można ją wywołać z poziomu Room ????
        # TODO obliczyć reakcję użytkownika (zmianę nastroju) na podstawie

        # # aktualizacja (sprawdzenie, czy nastrój już się nie zmienił
        # self.getMoodNumber()
        #
        # # wybór zostawu preferencji na podstawie sceriusza (porównania current_mood i target_mood)
        # # scenariusz A:
        # if self.current_mood == 1 & self.step_mood == 2:
        #     current_scenario = "A"
        #     current_user_scenario_preferences = self.preferences_set[0]
        # # scenariusz B:
        # if self.current_mood == 2 & self.step_mood == 3:
        #     current_scenario = "B"
        #     current_user_scenario_preferences = self.preferences_set[1]
        # # scenariusz C:
        # if self.current_mood == 0 & self.step_mood == 3:
        #     current_scenario = "C"
        #     current_user_scenario_preferences = self.preferences_set[2]
        # # scenariusz D:
        # if self.current_mood == 3 & self.step_mood == 2:
        #     current_scenario = "D"
        #     current_user_scenario_preferences = self.preferences_set[3]
        # else:
        #     print("None of the scenarios could be applied")
        #
        # if current_scenario == "A":
        #     mood_change = np.multiply(current_user_scenario_preferences, env.current_room_settings) # ??? czy nie lepiej przenieść to wszystko do Room()?
        #

        # if env.light == 0:  # warm
        #     self.current_arousal -= 0.1
        #     self.current_relax += 0.2
        # elif env.light == 1:  # neutral
        #     self.current_arousal += 0.1
        #     self.current_relax += 0
        # elif env.light == 2:  # cold
        #     self.current_arousal += 0.2
        #     self.current_relax -= 0.1

        return self.current_arousal, self.current_relax

# docelowy nastrój użytkowników, z którym uruchamiana jest symulacja, może być tylko 2 lub 3 (z założenia systemu użytkownik dostaje tylko takie do wyboru)
user1_target_mood = 2
user2_target_mood = 2
user3_target_mood = 2
#preferencje użytkowników
user1_preferences = [
            [
                [1, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                # [0, 1, 0, 0, 0, 0] # time needed
            ],
            [
                [0, 0, 0, 1, 0],
                [1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0],
                [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                # [1, 0, 0, 0, 0, 0]  # time needed
            ],

            [
                [0, 0, 1, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0],
                [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                # [1, 0, 0, 0, 0, 0] # time needed
            ],
            [
                [0, 0, 1, 0, 0],
                [1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                # [0, 1, 0, 0, 0, 0] # time needed
            ]
        ]
user2_preferences = [
    [
        [1, 0, 0, 0, 0],
        [0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        # [1, 0, 0, 0, 0, 0] # time needed
    ],
    [
        [0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0],
        [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        # [0, 1, 0, 0, 0, 0] # time needed
    ],
    [
        [0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        # [0, 1, 0, 0, 0, 0] # time needed
    ],
    [
        [1, 0, 0, 0, 0],
        [0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        # [0, 1, 0, 0, 0, 0] # time needed
    ]
]
user3_preferences = [
    [
        [1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        # [0, 1, 0, 0, 0, 0] # time needed
    ],
    [
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 1, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        # [0, 0, 1, 0, 0, 0] # time needed
    ],
    [
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 1, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        # [0, 0, 1, 0, 0, 0] # time needed
    ],
    [
        [1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        # [1, 0, 0, 0, 0, 0] # time needed
    ]
]
# respondent nr 1 (K, 21l.)
user1 = User(21, "User 1 (F21)", user1_target_mood, user1_preferences)
# respondent nr 40 (M, 26l.)
user2 = User(26, "User 2 (M26)", user2_target_mood, user2_preferences)
# respondent nr 45 (K, 52l.)
user3 = User(52, "User 3 (F52)", user3_target_mood, user3_preferences)

# grupa wiekowa 18-24
group_1_defualt_preferences = [
    # scenariusz A
    [
        [2, 0, 0, 0, 0],  # light intensity
        [0, 0, 2, 1, 0, 0, 0, 0, 0, 0],  # light color
        [0, 2, 1, 0],  # temperature
        [1, 0, 0, 0, 0, 0, 1, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # music
        [0, 0, 0, 2, 1, 0],  # music volume
        [2, 0, 1, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # fragrance
        [2, 2, 0, 0, 0, 0]  # time needed
    ],
    # scenariusz B
    [
        [0, 0, 0, 2, 0],  # light intensity
        [2, 0, 0, 2, 0, 0, 0, 0, 0, 0],  # light color
        [0, 2, 2, 0],  # temperature
        [2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # music
        [2, 0, 2, 0, 0, 0],  # volume
        [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # fragrance
        [2, 2, 0, 0, 0, 0]  # time needed
    ],
    # scenariusz C
    [
        [0, 0, 1, 2, 2],  # light intensity
        [2, 0, 0, 1, 0, 0, 0, 0, 0, 0],  # light color
        [0, 2, 2, 0],  # temperature
        [2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # music
        [2, 0, 1, 0, 0, 0],  # volume
        [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # fragrance
        [1, 2, 0, 0, 0, 0]  # time needed
    ],
    # scenariusz D
    [
        [2, 0, 0, 0, 0],  # light intensity
        [0, 0, 2, 0, 0, 0, 0, 0, 0, 0],  # light color
        [0, 2, 1, 0],  # temperature
        [0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0],  # music
        [0, 0, 1, 2, 2, 0],  # volume
        [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # fragrance
        [2, 2, 0, 0, 0, 0]  # time needed
    ]
]
# grupa wiekowa 25-30
group_2_defualt_preferences = [
    # scenariusz A
    [
        [2, 2, 0, 0, 0],
        [0, 0, 2, 1, 0, 0, 0, 0, 0, 0],
        [0, 2, 1, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 1, 0, 0, 0, 0]
    ],
    # scenariusz B
    [
        [0, 0, 0, 2, 0],
        [2, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 2, 2, 0],
        [2, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 1, 2, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 2, 0, 0, 0, 0]
    ],
    # scenariusz C
    [
        [0, 0, 0, 2, 1],
        [2, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 2, 2, 0],
        [2, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 2, 2, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 1, 1, 0, 0, 0]
    ],
    # scenariusz D
    [
        [2, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 2, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0]
    ]
]
# grupa wiekowa 31+
group_3_defualt_preferences = [
    # scenariusz A
    [
        [0, 2, 0, 0, 0],
        [0, 1, 1, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 0],
        [0, 1, 0, 1, 1, 2, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 1, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 2, 0, 0, 0, 0]
    ],
    # scenariusz B
    [
        [0, 0, 0, 2, 1],
        [2, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 1, 2, 1],
        [2, 1, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 2, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 1, 0, 0, 0]
    ],
    # scenariusz C
    [
        [0, 0, 0, 2, 0],
        [2, 0, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 2, 1, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 2, 0, 0]
    ],
    # scenariusz D
    [
        [2, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 2, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 2, 0],
        [2, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0]
    ]
]

class Room(gym.Env):
    min_temperature = 15
    max_temperature = 30

    # todo podmienić target mood odpowiednio na step_mood i przypisać do użytkownika
    def __init__(self, current_user,  target_mood=0, render_mode=None, size=5,):
        # initial room parameters, such as what settings are on, which devices are used
        # here i could add a variable to set which devices are being used in a test to see how the test reacts ??

        # przypisanie użytkownika
        self.current_user = current_user
        self.target_mood = target_mood
        # wybór grupy ze względu na wiek użytkownika
        if (self.current_user.age <= 24):
            self.default_group_preferences = group_1_defualt_preferences
            self.group_range = "18-24"
        elif (self.current_user.age <= 30):
            self.default_group_preferences = group_2_defualt_preferences
            self.group_range = "25-30"
        elif (self.current_user.age > 30):
            self.default_group_preferences = group_3_defualt_preferences
            self.group_range = "31+"
        # print("\nWYBRANY UŻYTKOWNIK:")
        # print("Wiek użytkownika", self.current_user.name, ": ", self.current_user.age)
        # print("Grupa wiekowa:", self.group_range)

        # initializing visualization
        if (target_mood == self.current_user.current_mood):
            print("self.current_user is already in target mood!")
        else:
            self.target_mood = target_mood
            # self.size = size  # square grid
            # self.window_size = 512  # pygame window size
            # Define action space: Light (3 values: Red, Green, Blue), Heater temperature (15 to 30 degrees)
            self.action_space = spaces.Tuple((
                spaces.Discrete(5),  # light_intensity: (1) very_bright, (2) bright,(3) dimmed, (4) semidark, (5) darkness
                spaces.Discrete(9),  # light_color: (1) none, (2) cold, (3) neutral, (4) warm), (5) red, (6) orange, (7) green, (8) blue, (9) purple
                spaces.Box(low=self.min_temperature, high=self.max_temperature, shape=(1,), dtype=np.float32),  # possible temperature between 15 and 30 degrees
                spaces.Discrete(18),  # sound_type: (1) none, (2) noise, (3) nature_forest, (4) nature_water, (5) background, (6) speech, (7) calm_instrumental, (8) calm_vocal, (9) lively, (10) hard, (11) soundtrack, (12) celtic, (13) rave, (14) focus, (15) lofi, (16) classical, (17) asmr, (18) ambient
                spaces.Discrete(6),  # sound_volume: (1) none, (2) very_quiet, (3) quiet, (4) moderate, (5) loud, (6) very_loud
                spaces.Discrete(16),  # fregrance: (1) none, (2) vanilla, (3) citrus, (4) mint, (5) lavender, (6) sweet, (7) forest, (8) coffee, (9) cake, (10) ater_lily, (11_ lilac, (12) black_opium, (13) ginger, (14) chocolate, (15) tea, (16) rain)
            ))

            print(self.action_space)
            self.current_room_settings = self.action_space
            # Observation space: the light setting and the current temperature
            self.observation_space = spaces.Tuple((
                # Light has three settings:  warm, neutral, cold
                spaces.Discrete(3),
                # possible temperature between 15 and 30 degrees
                spaces.Box(low=self.min_temperature, high=self.max_temperature, shape=(1,), dtype=np.float32),
            ))

            # SECTION ustawianie pierwszych ustawień otoczenia na preferowane ustawienia domyślnej grupy

            current_scenario = 1
            current_scenario_default_group_light_preferences = self.default_group_preferences[current_scenario][0]  # hardcode 0 jako scenariusz A, TODO podstawić automatyczny dobór scenariusza

            # Posortowane indeksy - kolejność preferowanych ustawień dla light dla podanego scenariusza
            current_scenario_default_group_light_preferences_indexes_sorted = sorted(range(len(current_scenario_default_group_light_preferences )), key=lambda i: current_scenario_default_group_light_preferences[i], reverse=True)

            # światło, które ma zostać ustawione
            room_light_setting_index = current_scenario_default_group_light_preferences_indexes_sorted[0]  # indeks ustawienia o najsilniejszej preferencji grupy domyślnej
            #TODO deklaracja self.current_room_settings
            room_light_setting = self.current_room_settings[0][room_light_setting_index]


            print("current_scenario_default_group_light_preferences: ", current_scenario_default_group_light_preferences )
            print("current_scenario_default_group_light_preferences_indexes_sorted: ", current_scenario_default_group_light_preferences_indexes_sorted)
            print("room_light_setting: ", room_light_setting)
            self.temperature = np.random.uniform(self.min_temperature, self.max_temperature)


    def reset(self):
        # Reset light and temperature to random values
        self.light = np.random.choice([0, 1, 2])
        self.temperature = np.random.uniform(12, 30)
        return self.light, np.array([self.temperature])

    def step(self, action):
        # Unpack the action (light setting, heater temperature)
        light, temperature = action

        # Update the state
        self.light = light
        self.temperature = np.clip(temperature[0], self.min_temperature, self.max_temperature)

        # TODO zaimplementować tak, żeby done=true tylko kiedy osiągnie pożądany nastrój (lub jeśli minie dany czas)
        done = False  # Generally, set this to True when the episode should end

        # Return the new observation, reward, done flag, and additional info (if any)
        return (self.light, np.array([self.temperature])), reward, done, {}

    # def render(self, mode='human'):
    #     light_colors = ["Warm", "Neutral", "Cold"]  # Mapping light settings to string
    #     light_str = light_colors[self.light]
    #     temperature_str = f"{self.temperature:.2f}"  # Convert temperature to a formatted string
    #
    #     print(f"Light setting: {light_str}, Temperature: {temperature_str}°C")


# uruchomienie symulacji dla danego użytkownika
room = Room(user1)

# Reset the roomironment
obs = room.reset()
# print("Initial observation:", obs)


# Take a step with action (red light, temperature 21)
action = (0, np.array([room.min_temperature]))
obs, reward, done, info = room.step(action)

# TODO dodać pętlę (while?) z iteracją czasu i inkrementacją czasu w każdej pętli - while z warunkiem końcowym w postaci odpowiedniej nagrody / poziomu procentowego spełnienia


# TODO iteracje uczące - doszukać jak to powinno wyglądać
while reward < 2:

    # aktualizacja(sprawdzenie, czy nastrój już się nie zmienił
    room.current_user.getMoodNumber()
    # TODO
    # # wybór zostawu preferencji na podstawie sceriusza (porównania current_mood i target_mood)
    # current_user_scenario_preferences = []
    # # scenariusz A:
    # if room.current_user.current_mood == 1 & room.current_user.step_mood == 2:
    #     current_scenario = "A"
    #     current_user_scenario_preferences = room.current_user.preferences_set[0]
    # # scenariusz B:
    # elif room.current_user.current_mood == 2 & room.current_user.step_mood == 3:
    #     current_scenario = "B"
    #     current_user_scenario_preferences = room.current_user.preferences_set[1]
    # # scenariusz C:
    # elif room.current_user.current_mood == 0 & room.current_user.step_mood == 3:
    #     current_scenario = "C"
    #     current_user_scenario_preferences = room.current_user.preferences_set[2]
    # # scenariusz D:
    # elif room.current_user.current_mood == 3 & room.current_user.step_mood == 2:
    #     current_scenario = "D"
    #     current_user_scenario_preferences = room.current_user.preferences_set[3]
    # else:
    #     print("None of the scenarios could be applied")


    # TODO zmienić format room.current_room_settings na analogiczny do current_user_scenario_preferences
    # mood_change = np.multiply(current_user_scenario_preferences, room.current_room_settings)
    #
    # # zmiana nastroju na podstawie obliczeń z preferencji użtkownika i bieżących ustawień pokoju
    # if current_scenario == "A":
    #     room.current_user.current_relax += np.sum(mood_change)
    # if current_scenario == "B":
    #     room.current_user.current_arousal -= np.sum(mood_change)
    # if current_scenario == "C":
    #     room.current_user.current_relax += np.sum(mood_change)
    # if current_scenario == "D":
    #     room.current_user.current_arousal += np.sum(mood_change)

    # przechodź po kolejnych ustawieniach otoczenia
    action = (room.light + 1, np.array(([room.temperature + 1])))

print("New observation:", obs)
print("Reward:", reward)

# Render the roomironment
room.render()
