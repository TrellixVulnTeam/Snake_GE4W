from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.properties import (ObjectProperty, NumericProperty)
from kivy.core.audio import SoundLoader
from kivy.uix.gridlayout import GridLayout
from random import randint
from copy import deepcopy

with open("game_configuration.txt", "r") as conf:
    a_one, b_one, c_one, d_one, e_one, f_one = conf.readline().split()

main_menu_music = SoundLoader.load("./main_menu.mp3")
main_menu_music.volume = .6

game_music = SoundLoader.load("./game_music.mp3")
game_music.volume = .6
game_music.loop = True

click_common_button_sound = SoundLoader.load("./click_common.ogg")

click_save_sound = SoundLoader.load("./save_sound.ogg")

dead_sound = SoundLoader.load("./dead_sound.ogg")
dead_music = SoundLoader.load("./dead_music.mp3")
dead_music.volume = .6

rotate = SoundLoader.load("./rotation_sound.wav")
pickup = SoundLoader.load("./pick_up_sound.wav")
newscore = SoundLoader.load("./new_best_score_sound.mp3")


class GameForm(GridLayout):
    zerozero = ObjectProperty()
    zeroone = ObjectProperty()
    zerotwo = ObjectProperty()
    zerothree = ObjectProperty()
    zerofour = ObjectProperty()
    zerofive = ObjectProperty()
    zerosix = ObjectProperty()
    zeroseven = ObjectProperty()
    zeroeight = ObjectProperty()
    zeronine = ObjectProperty()
    zeroten = ObjectProperty()
    zeroeleven = ObjectProperty()
    zerotwelve = ObjectProperty()
    zerothirteen = ObjectProperty()
    zerofourteen = ObjectProperty()
    zerofifteen = ObjectProperty()
    zerosixteen = ObjectProperty()
    zeroseventeen = ObjectProperty()
    zeroeighteen = ObjectProperty()
    zeronineteen = ObjectProperty()
    zerotwenty = ObjectProperty()
    zerotwenty_one = ObjectProperty()
    zerotwenty_two = ObjectProperty()
    onezero = ObjectProperty()
    oneone = ObjectProperty()
    onetwo = ObjectProperty()
    onethree = ObjectProperty()
    onefour = ObjectProperty()
    onefive = ObjectProperty()
    onesix = ObjectProperty()
    oneseven = ObjectProperty()
    oneeight = ObjectProperty()
    onenine = ObjectProperty()
    oneten = ObjectProperty()
    oneeleven = ObjectProperty()
    onetwelve = ObjectProperty()
    onethirteen = ObjectProperty()
    onefourteen = ObjectProperty()
    onefifteen = ObjectProperty()
    onesixteen = ObjectProperty()
    oneseventeen = ObjectProperty()
    oneeighteen = ObjectProperty()
    onenineteen = ObjectProperty()
    onetwenty = ObjectProperty()
    onetwenty_one = ObjectProperty()
    onetwenty_two = ObjectProperty()
    twozero = ObjectProperty()
    twoone = ObjectProperty()
    twotwo = ObjectProperty()
    twothree = ObjectProperty()
    twofour = ObjectProperty()
    twofive = ObjectProperty()
    twosix = ObjectProperty()
    twoseven = ObjectProperty()
    twoeight = ObjectProperty()
    twonine = ObjectProperty()
    twoten = ObjectProperty()
    twoeleven = ObjectProperty()
    twotwelve = ObjectProperty()
    twothirteen = ObjectProperty()
    twofourteen = ObjectProperty()
    twofifteen = ObjectProperty()
    twosixteen = ObjectProperty()
    twoseventeen = ObjectProperty()
    twoeighteen = ObjectProperty()
    twonineteen = ObjectProperty()
    twotwenty = ObjectProperty()
    twotwenty_one = ObjectProperty()
    twotwenty_two = ObjectProperty()
    threezero = ObjectProperty()
    threeone = ObjectProperty()
    threetwo = ObjectProperty()
    threethree = ObjectProperty()
    threefour = ObjectProperty()
    threefive = ObjectProperty()
    threesix = ObjectProperty()
    threeseven = ObjectProperty()
    threeeight = ObjectProperty()
    threenine = ObjectProperty()
    threeten = ObjectProperty()
    threeeleven = ObjectProperty()
    threetwelve = ObjectProperty()
    threethirteen = ObjectProperty()
    threefourteen = ObjectProperty()
    threefifteen = ObjectProperty()
    threesixteen = ObjectProperty()
    threeseventeen = ObjectProperty()
    threeeighteen = ObjectProperty()
    threenineteen = ObjectProperty()
    threetwenty = ObjectProperty()
    threetwenty_one = ObjectProperty()
    threetwenty_two = ObjectProperty()
    fourzero = ObjectProperty()
    fourone = ObjectProperty()
    fourtwo = ObjectProperty()
    fourthree = ObjectProperty()
    fourfour = ObjectProperty()
    fourfive = ObjectProperty()
    foursix = ObjectProperty()
    fourseven = ObjectProperty()
    foureight = ObjectProperty()
    fournine = ObjectProperty()
    fourten = ObjectProperty()
    foureleven = ObjectProperty()
    fourtwelve = ObjectProperty()
    fourthirteen = ObjectProperty()
    fourfourteen = ObjectProperty()
    fourfifteen = ObjectProperty()
    foursixteen = ObjectProperty()
    fourseventeen = ObjectProperty()
    foureighteen = ObjectProperty()
    fournineteen = ObjectProperty()
    fourtwenty = ObjectProperty()
    fourtwenty_one = ObjectProperty()
    fourtwenty_two = ObjectProperty()
    fivezero = ObjectProperty()
    fiveone = ObjectProperty()
    fivetwo = ObjectProperty()
    fivethree = ObjectProperty()
    fivefour = ObjectProperty()
    fivefive = ObjectProperty()
    fivesix = ObjectProperty()
    fiveseven = ObjectProperty()
    fiveeight = ObjectProperty()
    fivenine = ObjectProperty()
    fiveten = ObjectProperty()
    fiveeleven = ObjectProperty()
    fivetwelve = ObjectProperty()
    fivethirteen = ObjectProperty()
    fivefourteen = ObjectProperty()
    fivefifteen = ObjectProperty()
    fivesixteen = ObjectProperty()
    fiveseventeen = ObjectProperty()
    fiveeighteen = ObjectProperty()
    fivenineteen = ObjectProperty()
    fivetwenty = ObjectProperty()
    fivetwenty_one = ObjectProperty()
    fivetwenty_two = ObjectProperty()
    sixzero = ObjectProperty()
    sixone = ObjectProperty()
    sixtwo = ObjectProperty()
    sixthree = ObjectProperty()
    sixfour = ObjectProperty()
    sixfive = ObjectProperty()
    sixsix = ObjectProperty()
    sixseven = ObjectProperty()
    sixeight = ObjectProperty()
    sixnine = ObjectProperty()
    sixten = ObjectProperty()
    sixeleven = ObjectProperty()
    sixtwelve = ObjectProperty()
    sixthirteen = ObjectProperty()
    sixfourteen = ObjectProperty()
    sixfifteen = ObjectProperty()
    sixsixteen = ObjectProperty()
    sixseventeen = ObjectProperty()
    sixeighteen = ObjectProperty()
    sixnineteen = ObjectProperty()
    sixtwenty = ObjectProperty()
    sixtwenty_one = ObjectProperty()
    sixtwenty_two = ObjectProperty()
    sevenzero = ObjectProperty()
    sevenone = ObjectProperty()
    seventwo = ObjectProperty()
    seventhree = ObjectProperty()
    sevenfour = ObjectProperty()
    sevenfive = ObjectProperty()
    sevensix = ObjectProperty()
    sevenseven = ObjectProperty()
    seveneight = ObjectProperty()
    sevennine = ObjectProperty()
    seventen = ObjectProperty()
    seveneleven = ObjectProperty()
    seventwelve = ObjectProperty()
    seventhirteen = ObjectProperty()
    sevenfourteen = ObjectProperty()
    sevenfifteen = ObjectProperty()
    sevensixteen = ObjectProperty()
    sevenseventeen = ObjectProperty()
    seveneighteen = ObjectProperty()
    sevennineteen = ObjectProperty()
    seventwenty = ObjectProperty()
    seventwenty_one = ObjectProperty()
    seventwenty_two = ObjectProperty()
    eightzero = ObjectProperty()
    eightone = ObjectProperty()
    eighttwo = ObjectProperty()
    eightthree = ObjectProperty()
    eightfour = ObjectProperty()
    eightfive = ObjectProperty()
    eightsix = ObjectProperty()
    eightseven = ObjectProperty()
    eighteight = ObjectProperty()
    eightnine = ObjectProperty()
    eightten = ObjectProperty()
    eighteleven = ObjectProperty()
    eighttwelve = ObjectProperty()
    eightthirteen = ObjectProperty()
    eightfourteen = ObjectProperty()
    eightfifteen = ObjectProperty()
    eightsixteen = ObjectProperty()
    eightseventeen = ObjectProperty()
    eighteighteen = ObjectProperty()
    eightnineteen = ObjectProperty()
    eighttwenty = ObjectProperty()
    eighttwenty_one = ObjectProperty()
    eighttwenty_two = ObjectProperty()
    ninezero = ObjectProperty()
    nineone = ObjectProperty()
    ninetwo = ObjectProperty()
    ninethree = ObjectProperty()
    ninefour = ObjectProperty()
    ninefive = ObjectProperty()
    ninesix = ObjectProperty()
    nineseven = ObjectProperty()
    nineeight = ObjectProperty()
    ninenine = ObjectProperty()
    nineten = ObjectProperty()
    nineeleven = ObjectProperty()
    ninetwelve = ObjectProperty()
    ninethirteen = ObjectProperty()
    ninefourteen = ObjectProperty()
    ninefifteen = ObjectProperty()
    ninesixteen = ObjectProperty()
    nineseventeen = ObjectProperty()
    nineeighteen = ObjectProperty()
    ninenineteen = ObjectProperty()
    ninetwenty = ObjectProperty()
    ninetwenty_one = ObjectProperty()
    ninetwenty_two = ObjectProperty()
    tenzero = ObjectProperty()
    tenone = ObjectProperty()
    tentwo = ObjectProperty()
    tenthree = ObjectProperty()
    tenfour = ObjectProperty()
    tenfive = ObjectProperty()
    tensix = ObjectProperty()
    tenseven = ObjectProperty()
    teneight = ObjectProperty()
    tennine = ObjectProperty()
    tenten = ObjectProperty()
    teneleven = ObjectProperty()
    tentwelve = ObjectProperty()
    tenthirteen = ObjectProperty()
    tenfourteen = ObjectProperty()
    tenfifteen = ObjectProperty()
    tensixteen = ObjectProperty()
    tenseventeen = ObjectProperty()
    teneighteen = ObjectProperty()
    tennineteen = ObjectProperty()
    tentwenty = ObjectProperty()
    tentwenty_one = ObjectProperty()
    tentwenty_two = ObjectProperty()

    current_score_first = ObjectProperty()
    current_score_two = ObjectProperty()
    current_score_three = ObjectProperty()

    best_score_first = ObjectProperty()
    best_score_two = ObjectProperty()
    best_score_three = ObjectProperty()

    tts = ObjectProperty()

    res_screen = ObjectProperty()

    def __init__(self, **kwargs):
        super(GameForm, self).__init__(**kwargs)
        self.cells = list()
        self.flower_r = 0
        self.flower_g = 0
        self.flower_b = 0
        self.direction = "stop"
        self.first_open_gameform = 0
        self.commands_list = list()
        self.last_head_direction = ['fivefour', 'head', 'right', 0]
        self.turn_counter = 1
        self.last_head_pos_x = 0
        self.last_head_pos_y = 0
        self.copy_cl_s = list()
        self.speed = 1
        self.turns_oddity = 0
        self.prev_head_pos = list()

        self.com_pause = 0
        self.last_directions_even = list()
        self.last_directions_odd = list()
        self.last_coms_odd = list()
        self.last_coms_even = list()
        self.last_body_data = list()

        self.final_direction_list = list()
        self.current_score = 0

        self.event_one = None
        self.event_two = None
        self.global_direction = "stop"
        self.red = 0

        self.check_number_of_start = 0

        self.a_one = a_one
        self.b_one = b_one
        self.c_one = c_one
        self.d_one = d_one
        self.e_one = e_one
        self.f_one = f_one
        self.best_score = int(self.d_one)

        if self.f_one == "1":
            main_menu_music.play()

    def set_flower(self):
        if self.current_score < 252:
            case = randint(0, 5)
            if case == 0:
                self.flower_r = .99
                self.flower_g = .33
                self.flower_b = .33
            elif case == 1:
                self.flower_r = 1
                self.flower_g = .55
                self.flower_b = 0
            elif case == 2:
                self.flower_r = 1
                self.flower_g = .93
                self.flower_b = 0
            elif case == 3:
                self.flower_r = 0
                self.flower_g = .76
                self.flower_b = 1
            elif case == 4:
                self.flower_r = 0
                self.flower_g = .55
                self.flower_b = .9
            else:
                self.flower_r = .61
                self.flower_g = .24
                self.flower_b = .78
            while True:
                flower_x = randint(0, 10)
                flower_y = randint(0, 22)
                if self.cells[flower_x][flower_y][1] == "cell":
                    self.cells[flower_x][flower_y][1] = "flower"
                    break

    def on_start(self):
        for i in range(11):
            temp_cells_line = list()
            for j in range(23):
                if i == 1:
                    x = "one"
                elif i == 2:
                    x = "two"
                elif i == 3:
                    x = "three"
                elif i == 4:
                    x = "four"
                elif i == 5:
                    x = "five"
                elif i == 6:
                    x = "six"
                elif i == 7:
                    x = "seven"
                elif i == 8:
                    x = "eight"
                elif i == 9:
                    x = "nine"
                elif i == 10:
                    x = "ten"
                else:
                    x = "zero"
                if j == 1:
                    y = "one"
                elif j == 2:
                    y = "two"
                elif j == 3:
                    y = "three"
                elif j == 4:
                    y = "four"
                elif j == 5:
                    y = "five"
                elif j == 6:
                    y = "six"
                elif j == 7:
                    y = "seven"
                elif j == 8:
                    y = "eight"
                elif j == 9:
                    y = "nine"
                elif j == 10:
                    y = "ten"
                elif j == 11:
                    y = "eleven"
                elif j == 12:
                    y = "twelve"
                elif j == 13:
                    y = "thirteen"
                elif j == 14:
                    y = "fourteen"
                elif j == 15:
                    y = "fifteen"
                elif j == 16:
                    y = "sixteen"
                elif j == 17:
                    y = "seventeen"
                elif j == 18:
                    y = "eighteen"
                elif j == 19:
                    y = "nineteen"
                elif j == 20:
                    y = "twenty"
                elif j == 21:
                    y = "twenty_one"
                elif j == 22:
                    y = "twenty_two"
                else:
                    y = "zero"
                temp_cells_line.append([str(x + y), "cell", "stop", 0])
            self.cells.append(temp_cells_line)
        self.cells[5][4][1] = "head"
        self.cells[5][4][2] = self.direction
        self.set_flower()
        self.rendering()
        if int(self.b_one) == 0:
            self.speed = .5
        elif int(self.b_one) == 1:
            self.speed = .23
        else:
            self.speed = .1
        self.event_one = Clock.schedule_interval(self.moving_cells, self.speed)

    def on_touch_down(self, touch):
        if self.e_one == "1":
            rotate.play()
        x_vector = touch.x / self.size[0]
        y_vector = touch.y / self.size[1]
        reversed_x = 1 - x_vector
        body = self.check_for_body()
        if x_vector > y_vector and reversed_x > y_vector:
            if self.global_direction == "top" and body:
                self.direction = "top"
            else:
                self.direction = "bottom"
        elif x_vector > y_vector >= reversed_x:
            if self.global_direction == "left" and body:
                self.direction = "left"
            else:
                self.direction = "right"
        elif x_vector <= y_vector < reversed_x:
            if self.global_direction == "right" and body:
                self.direction = "right"
            else:
                self.direction = "left"
        else:
            if self.global_direction == "bottom" and body:
                self.direction = "bottom"
            else:
                self.direction = "top"
        if self.first_open_gameform == 0:
            self.first_open_gameform += 1
            self.tts.clear_widgets()
            self.on_start()

    def check_for_body(self):
        body = False
        if len(self.cells) > 0:
            for i in range(11):
                for j in range(23):
                    if self.cells[i][j][1] == "body":
                        body = True
        return body

    def rendering(self):
        for i in range(11):
            for j in range(23):
                if self.cells[i][j][1] == "head":
                    if self.c_one == "Green":
                        exec("self.{}.r = 0".format(self.cells[i][j][0]))
                        exec("self.{}.g = .56".format(self.cells[i][j][0]))
                        exec("self.{}.b = .2".format(self.cells[i][j][0]))
                    elif self.c_one == "Purple":
                        exec("self.{}.r = .35".format(self.cells[i][j][0]))
                        exec("self.{}.g = .2".format(self.cells[i][j][0]))
                        exec("self.{}.b = .56".format(self.cells[i][j][0]))
                    elif self.c_one == "Orange":
                        exec("self.{}.r = 1".format(self.cells[i][j][0]))
                        exec("self.{}.g = .4".format(self.cells[i][j][0]))
                        exec("self.{}.b = 0".format(self.cells[i][j][0]))
                    elif self.c_one == "Blue":
                        exec("self.{}.r = 0".format(self.cells[i][j][0]))
                        exec("self.{}.g = .07".format(self.cells[i][j][0]))
                        exec("self.{}.b = .85".format(self.cells[i][j][0]))
                    elif self.c_one == "Pink":
                        exec("self.{}.r = 1".format(self.cells[i][j][0]))
                        exec("self.{}.g = .31".format(self.cells[i][j][0]))
                        exec("self.{}.b = .58".format(self.cells[i][j][0]))
                    elif self.c_one == "Sea":
                        exec("self.{}.r = .04".format(self.cells[i][j][0]))
                        exec("self.{}.g = .62".format(self.cells[i][j][0]))
                        exec("self.{}.b = .62".format(self.cells[i][j][0]))
                    elif self.c_one == "Black":
                        exec("self.{}.r = .17".format(self.cells[i][j][0]))
                        exec("self.{}.g = .24".format(self.cells[i][j][0]))
                        exec("self.{}.b = .31".format(self.cells[i][j][0]))
                elif self.cells[i][j][1] == "flower":
                    exec("self.{}.r = {}".format(self.cells[i][j][0], self.flower_r))
                    exec("self.{}.g = {}".format(self.cells[i][j][0], self.flower_g))
                    exec("self.{}.b = {}".format(self.cells[i][j][0], self.flower_b))
                elif self.cells[i][j][1] == "body":
                    if self.c_one == "Green":
                        exec("self.{}.r = 0".format(self.cells[i][j][0]))
                        exec("self.{}.g = .84".format(self.cells[i][j][0]))
                        exec("self.{}.b = .24".format(self.cells[i][j][0]))
                    elif self.c_one == "Purple":
                        exec("self.{}.r = .58".format(self.cells[i][j][0]))
                        exec("self.{}.g = .44".format(self.cells[i][j][0]))
                        exec("self.{}.b = .84".format(self.cells[i][j][0]))
                    elif self.c_one == "Orange":
                        exec("self.{}.r = 1".format(self.cells[i][j][0]))
                        exec("self.{}.g = .62".format(self.cells[i][j][0]))
                        exec("self.{}.b = .36".format(self.cells[i][j][0]))
                    elif self.c_one == "Blue":
                        exec("self.{}.r = .38".format(self.cells[i][j][0]))
                        exec("self.{}.g = .42".format(self.cells[i][j][0]))
                        exec("self.{}.b = .85".format(self.cells[i][j][0]))
                    elif self.c_one == "Pink":
                        exec("self.{}.r = 1".format(self.cells[i][j][0]))
                        exec("self.{}.g = .62".format(self.cells[i][j][0]))
                        exec("self.{}.b = .78".format(self.cells[i][j][0]))
                    elif self.c_one == "Sea":
                        exec("self.{}.r = .15".format(self.cells[i][j][0]))
                        exec("self.{}.g = .82".format(self.cells[i][j][0]))
                        exec("self.{}.b = .84".format(self.cells[i][j][0]))
                    elif self.c_one == "Black":
                        exec("self.{}.r = .1".format(self.cells[i][j][0]))
                        exec("self.{}.g = .73".format(self.cells[i][j][0]))
                        exec("self.{}.b = .6".format(self.cells[i][j][0]))
                elif self.cells[i][j][1] == "r":
                    exec("self.{}.r = 1".format(self.cells[i][j][0]))
                    exec("self.{}.g = 0".format(self.cells[i][j][0]))
                    exec("self.{}.b = 0".format(self.cells[i][j][0]))
                else:
                    exec("self.{}.r = 1".format(self.cells[i][j][0]))
                    exec("self.{}.g = 1".format(self.cells[i][j][0]))
                    exec("self.{}.b = 1".format(self.cells[i][j][0]))

    def moving_cells(self, *args):
        self.global_direction = self.direction
        self.commands_list.clear()
        self.copy_cl_s.clear()
        create_body = False
        stop_game_body = "No"
        body = list()
        head = list()
        for _ in range(11):
            for __ in range(23):
                if self.cells[_][__][1] == "body":
                    self.commands_list.append(self.cells[_][__])
                    if self.cells[_][__][3] == self.turn_counter - 1:
                        body = deepcopy(self.cells[_][__])
                if self.cells[_][__][1] == "head":
                    head = deepcopy(self.cells[_][__])
                    self.cells[_][__][2] = self.direction
                    self.last_head_direction = self.cells[_][__]
                    self.last_head_pos_x = _
                    self.last_head_pos_y = __
        k = 1
        if self.direction == "top":
            for i in range(11):
                for j in range(23):
                    if k != 0 and self.cells[i][j][2] == "top" and self.cells[i][j][1] == "head":
                        k -= 1
                        if i == 0:
                            if self.cells[10][j][1] == "body":
                                self.stop_game("body_part", "top")
                                stop_game_body = "Yes"
                            elif self.a_one == "Yes" or self.current_score >= 252:
                                self.stop_game("body_part", "top")
                                stop_game_body = "Yes_board"
                            if self.cells[10][j][1] == "flower":
                                self.score()
                                create_body = True
                            if stop_game_body != "Yes_board":
                                self.cells[10][j][1] = self.cells[i][j][1]
                                self.cells[10][j][2] = self.cells[i][j][2]
                        else:
                            if self.current_score >= 252:
                                self.stop_game("body_part", "top")
                                stop_game_body = "Yes_board"
                            if self.cells[i - 1][j][1] == "body":
                                self.stop_game("body_part", "top")
                                stop_game_body = "Yes"
                            if self.cells[i - 1][j][1] == "flower":
                                self.score()
                                create_body = True
                            if stop_game_body != "Yes_board":
                                self.cells[i - 1][j][1] = self.cells[i][j][1]
                                self.cells[i - 1][j][2] = self.cells[i][j][2]
                        if stop_game_body != "Yes_board":
                            self.cells[i][j][1] = "cell"
                            self.cells[i][j][2] = "stop"
        elif self.direction == "bottom":
            for i in range(11):
                for j in range(23):
                    if k != 0 and self.cells[i][j][2] == "bottom" and self.cells[i][j][1] == "head":
                        k -= 1
                        if i == 10:
                            if self.cells[0][j][1] == "body":
                                self.stop_game("body_part", "bottom")
                                stop_game_body = "Yes"
                            elif self.a_one == "Yes" or self.current_score >= 252:
                                self.stop_game("body_part", "top")
                                stop_game_body = "Yes_board"
                            if self.cells[0][j][1] == "flower":
                                self.score()
                                create_body = True
                            if stop_game_body != "Yes_board":
                                self.cells[0][j][1] = self.cells[i][j][1]
                                self.cells[0][j][2] = self.cells[i][j][2]
                        else:
                            if self.current_score >= 252:
                                self.stop_game("body_part", "top")
                                stop_game_body = "Yes_board"
                            if self.cells[i + 1][j][1] == "body":
                                self.stop_game("body_part", "bottom")
                                stop_game_body = "Yes"
                            if self.cells[i + 1][j][1] == "flower":
                                self.score()
                                create_body = True
                            if stop_game_body != "Yes_board":
                                self.cells[i + 1][j][1] = self.cells[i][j][1]
                                self.cells[i + 1][j][2] = self.cells[i][j][2]
                        if stop_game_body != "Yes_board":
                            self.cells[i][j][1] = "cell"
                            self.cells[i][j][2] = "stop"
        elif self.direction == "left":
            for i in range(11):
                for j in range(23):
                    if k != 0 and self.cells[i][j][2] == "left" and self.cells[i][j][1] == "head":
                        k -= 1
                        if j == 0:
                            if self.cells[i][22][1] == "body":
                                self.stop_game("body_part", "left")
                                stop_game_body = "Yes"
                            elif self.a_one == "Yes" or self.current_score >= 252:
                                self.stop_game("body_part", "top")
                                stop_game_body = "Yes_board"
                            if self.cells[i][22][1] == "flower":
                                self.score()
                                create_body = True
                            if stop_game_body != "Yes_board":
                                self.cells[i][22][1] = self.cells[i][j][1]
                                self.cells[i][22][2] = self.cells[i][j][2]
                        else:
                            if self.current_score >= 252:
                                self.stop_game("body_part", "top")
                                stop_game_body = "Yes_board"
                            if self.cells[i][j - 1][1] == "body":
                                self.stop_game("body_part", "left")
                                stop_game_body = "Yes"
                            if self.cells[i][j - 1][1] == "flower":
                                self.score()
                                create_body = True
                            if stop_game_body != "Yes_board":
                                self.cells[i][j - 1][1] = self.cells[i][j][1]
                                self.cells[i][j - 1][2] = self.cells[i][j][2]
                        if stop_game_body != "Yes_board":
                            self.cells[i][j][1] = "cell"
                            self.cells[i][j][2] = "stop"
        elif self.direction == "right":
            for i in range(11):
                for j in range(23):
                    if k != 0 and self.cells[i][j][2] == "right" and self.cells[i][j][1] == "head":
                        k -= 1
                        if j == 22:
                            if self.cells[i][0][1] == "body":
                                self.stop_game("body_part", "right")
                                stop_game_body = "Yes"
                            elif self.a_one == "Yes" or self.current_score >= 252:
                                self.stop_game("body_part", "top")
                                stop_game_body = "Yes_board"
                            if self.cells[i][0][1] == "flower":
                                self.score()
                                create_body = True
                            if stop_game_body != "Yes_board":
                                self.cells[i][0][1] = self.cells[i][j][1]
                                self.cells[i][0][2] = self.cells[i][j][2]
                        else:
                            if self.current_score >= 252:
                                self.stop_game("body_part", "top")
                                stop_game_body = "Yes_board"
                            if self.cells[i][j + 1][1] == "body":
                                self.stop_game("body_part", "right")
                                stop_game_body = "Yes"
                            if self.cells[i][j + 1][1] == "flower":
                                self.score()
                                create_body = True
                            if stop_game_body != "Yes_board":
                                self.cells[i][j + 1][1] = self.cells[i][j][1]
                                self.cells[i][j + 1][2] = self.cells[i][j][2]
                        if stop_game_body != "Yes_board":
                            self.cells[i][j][1] = "cell"
                            self.cells[i][j][2] = "stop"
        list_of_bodies = list()
        list_of_bodies.clear()
        for lu in range(11):
            for la in range(23):
                if self.cells[lu][la][1] == "body" or self.cells[lu][la][1] == "head":
                    list_of_bodies.append(self.cells[lu][la])
        list_of_bodies.sort(key=lambda x: x[3])
        if len(body) == 0:
            if self.com_pause % 2 == 0:
                self.last_coms_even.clear()
                self.last_coms_even = deepcopy(list_of_bodies)
                self.last_directions_even.clear()
                for lol in list_of_bodies:
                    self.last_directions_even.append(lol[2])
            else:
                self.last_coms_odd.clear()
                self.last_coms_odd = deepcopy(list_of_bodies)
                self.last_directions_odd.clear()
                for lal in list_of_bodies:
                    self.last_directions_odd.append(lal[2])
            if self.com_pause % 2 == 0:
                self.last_coms_even.pop(0)
                for al in range(len(self.last_coms_even)):
                    self.last_coms_even[al][2] = self.last_directions_odd[al]
                self.implements_in_cells(stop_game_body, self.last_coms_even)
            else:
                self.last_coms_odd.pop(0)
                for al in range(len(self.last_coms_odd)):
                    self.last_coms_odd[al][2] = self.last_directions_even[al]
                self.implements_in_cells(stop_game_body, self.last_coms_odd)
            self.com_pause += 1
        else:
            list_of_bodies.pop(0)
            for al in range(len(list_of_bodies)):
                list_of_bodies[al][2] = self.final_direction_list[al][2]
            self.implements_in_cells(stop_game_body, list_of_bodies)
        self.add_body(create_body, self.commands_list, head, body)

    def implements_in_cells(self, stop_game_body, *cells_for_implementation):
        inside = list()
        for i in cells_for_implementation:
            for j in range(len(i)):
                inside.append(i[j])
        inside.sort(key=lambda x: -x[3])
        if stop_game_body == "No":
            while len(inside) != 0:
                nearest = inside.pop()
                step = 1
                for n in range(11):
                    for m in range(23):
                        if self.cells[n][m][0] == nearest[0] and nearest[2] == "top" and step != 0:
                            step -= 1
                            if n == 0:
                                self.cells[10][m][1] = nearest[1]
                                self.cells[10][m][2] = nearest[2]
                                self.cells[10][m][3] = nearest[3]
                            else:
                                self.cells[n - 1][m][1] = nearest[1]
                                self.cells[n - 1][m][2] = nearest[2]
                                self.cells[n - 1][m][3] = nearest[3]
                            self.cells[n][m][1] = "cell"
                            self.cells[n][m][2] = "stop"
                            self.cells[n][m][3] = 0
                        elif self.cells[n][m][0] == nearest[0] and nearest[2] == "bottom" and step != 0:
                            step -= 1
                            if n == 10:
                                self.cells[0][m][1] = nearest[1]
                                self.cells[0][m][2] = nearest[2]
                                self.cells[0][m][3] = nearest[3]
                            else:
                                self.cells[n + 1][m][1] = nearest[1]
                                self.cells[n + 1][m][2] = nearest[2]
                                self.cells[n + 1][m][3] = nearest[3]
                            self.cells[n][m][1] = "cell"
                            self.cells[n][m][2] = "stop"
                            self.cells[n][m][3] = 0
                        elif self.cells[n][m][0] == nearest[0] and nearest[2] == "left" and step != 0:
                            step -= 1
                            if m == 0:
                                self.cells[n][22][1] = nearest[1]
                                self.cells[n][22][2] = nearest[2]
                                self.cells[n][22][3] = nearest[3]
                            else:
                                self.cells[n][m - 1][1] = nearest[1]
                                self.cells[n][m - 1][2] = nearest[2]
                                self.cells[n][m - 1][3] = nearest[3]
                            self.cells[n][m][1] = "cell"
                            self.cells[n][m][2] = "stop"
                            self.cells[n][m][3] = 0
                        elif self.cells[n][m][0] == nearest[0] and nearest[2] == "right" and step != 0:
                            step -= 1
                            if m == 22:
                                self.cells[n][0][1] = nearest[1]
                                self.cells[n][0][2] = nearest[2]
                                self.cells[n][0][3] = nearest[3]
                            else:
                                self.cells[n][m + 1][1] = nearest[1]
                                self.cells[n][m + 1][2] = nearest[2]
                                self.cells[n][m + 1][3] = nearest[3]
                            self.cells[n][m][1] = "cell"
                            self.cells[n][m][2] = "stop"
                            self.cells[n][m][3] = 0
                        elif self.cells[n][m][0] == nearest[0] and nearest[2] == "stop" and step != 0:
                            step -= 1

            self.final_direction_list.clear()
            for lulu in range(11):
                for lala in range(23):
                    if self.cells[lulu][lala][1] == "body" or self.cells[lulu][lala][1] == "head":
                        self.final_direction_list.append(self.cells[lulu][lala])
            self.final_direction_list.sort(key=lambda x: x[3])
            self.final_direction_list = deepcopy(self.final_direction_list)
        elif stop_game_body == "Yes":
            last_body_direction = inside.pop(0)
            for i in range(11):
                for j in range(23):
                    if self.cells[i][j][0] == self.last_head_direction[0]:
                        self.cells[i][j][1] = "body"
                    if self.cells[i][j][0] == last_body_direction[0]:
                        if self.cells[i][j][1] == "head":
                            last_body_direction = inside.pop(0)
                            for n in range(11):
                                for m in range(23):
                                    if self.cells[n][m][0] == last_body_direction[0]:
                                        self.cells[n][m][1] = "cell"
                        else:
                            self.cells[i][j][1] = "cell"
            self.rendering()
            self.event_two = Clock.schedule_interval(self.red_head, .5)
        elif stop_game_body == "Yes_board":
            self.event_two = Clock.schedule_interval(self.red_head, .5)

    def red_head(self, *args):
        if self.red % 2 == 0:
            for i in range(11):
                for j in range(23):
                    if self.cells[i][j][1] == "head":
                        self.cells[i][j][1] = "r"
                    elif self.cells[i][j][1] == "r":
                        self.cells[i][j][1] = "head"
        else:
            for i in range(11):
                for j in range(23):
                    if self.cells[i][j][1] == "head":
                        self.cells[i][j][1] = "r"
                    elif self.cells[i][j][1] == "r":
                        self.cells[i][j][1] = "head"
        if self.red >= 7:
            self.event_two.cancel()
            self.result_screen()
        self.red += 1
        self.rendering()

    def add_body(self, was_flower, head_and_body, head, body):
        if was_flower:
            if len(body) > 0:
                self.prev_head_pos.append([body[0], body[1], "stop", self.turn_counter])
            else:
                self.prev_head_pos.append([head[0], "body", "stop", self.turn_counter])
            self.turn_counter += 1
            gu = self.prev_head_pos.pop()
            for _ in range(11):
                for __ in range(23):
                    if self.cells[_][__][0] == gu[0]:
                        self.cells[_][__][1] = gu[1]
                        self.cells[_][__][2] = gu[2]
                        self.cells[_][__][3] = gu[3]
            self.set_flower()
        self.rendering()

    def score(self):
        if self.e_one == "1":
            pickup.play()
        self.current_score += 1
        d = self.current_score // 100
        p = (self.current_score // 10) % 10
        s = self.current_score % 10
        if d == 0:
            self.current_score_first.source = "number_zero.png"
        elif d == 1:
            self.current_score_first.source = "number_one.png"
        elif d == 2:
            self.current_score_first.source = "number_two.png"
        elif d == 3:
            self.current_score_first.source = "number_three.png"
        elif d == 4:
            self.current_score_first.source = "number_four.png"
        elif d == 5:
            self.current_score_first.source = "number_five.png"
        elif d == 6:
            self.current_score_first.source = "number_six.png"
        elif d == 7:
            self.current_score_first.source = "number_seven.png"
        elif d == 8:
            self.current_score_first.source = "number_eight.png"
        elif d == 9:
            self.current_score_first.source = "number_nine.png"

        if p == 0:
            self.current_score_two.source = "number_zero.png"
        elif p == 1:
            self.current_score_two.source = "number_one.png"
        elif p == 2:
            self.current_score_two.source = "number_two.png"
        elif p == 3:
            self.current_score_two.source = "number_three.png"
        elif p == 4:
            self.current_score_two.source = "number_four.png"
        elif p == 5:
            self.current_score_two.source = "number_five.png"
        elif p == 6:
            self.current_score_two.source = "number_six.png"
        elif p == 7:
            self.current_score_two.source = "number_seven.png"
        elif p == 8:
            self.current_score_two.source = "number_eight.png"
        elif p == 9:
            self.current_score_two.source = "number_nine.png"

        if s == 0:
            self.current_score_three.source = "number_zero.png"
        elif s == 1:
            self.current_score_three.source = "number_one.png"
        elif s == 2:
            self.current_score_three.source = "number_two.png"
        elif s == 3:
            self.current_score_three.source = "number_three.png"
        elif s == 4:
            self.current_score_three.source = "number_four.png"
        elif s == 5:
            self.current_score_three.source = "number_five.png"
        elif s == 6:
            self.current_score_three.source = "number_six.png"
        elif s == 7:
            self.current_score_three.source = "number_seven.png"
        elif s == 8:
            self.current_score_three.source = "number_eight.png"
        elif s == 9:
            self.current_score_three.source = "number_nine.png"

        if self.current_score > self.best_score:
            self.best_score_first.source = self.current_score_first.source
            self.best_score_two.source = self.current_score_two.source
            self.best_score_three.source = self.current_score_three.source
            self.best_score = self.current_score
            if self.e_one == "1" and self.best_score % 10 == 0:
                newscore.play()

    def stop_game(self, reason, direction):
        game_music.stop()
        if self.f_one == "1":
            dead_music.play()
            dead_sound.play()
        self.event_one.cancel()
        with open("game_configuration.txt", "w") as new_conf:
            new_conf.write(
                "{} {} {} {} {} {}".format(self.a_one, self.b_one, self.c_one, str(self.best_score), self.e_one,
                                           self.f_one))

    def result_screen(self):
        x = ResultScreen()
        x.cur_score_first.source = self.current_score_first.source
        x.cur_score_second.source = self.current_score_two.source
        x.cur_score_third.source = self.current_score_three.source

        x.bsw_f.source = self.best_score_first.source
        x.bsw_s.source = self.best_score_two.source
        x.bsw_t.source = self.best_score_three.source
        self.res_screen.add_widget(x)

    def end_cleaning(self):
        if self.check_number_of_start > 0:
            self.check_number_of_start = 0
            self.res_screen.clear_widgets()
            self.tts.add_widget(Image(source="tap_to_start.png"))
            self.current_score = -1
            self.score()
            self.first_open_gameform = 0
            for i in range(11):
                for j in range(23):
                    self.cells[i][j][1] = "cell"
                    self.cells[i][j][2] = "stop"
                    self.cells[i][j][3] = 0
            self.rendering()
            self.cells.clear()
            self.red = 0

    def reset_options_list(self):
        with open("game_configuration.txt", "r") as confff:
            self.a_one, self.b_one, self.c_one, self.d_one, self.e_one, self.f_one = confff.readline().split()
        if self.f_one == "1":
            main_menu_music.play()
        elif self.f_one == "0":
            main_menu_music.stop()

    def click_music(self):
        if self.e_one == "1":
            click_common_button_sound.play()

    def click_continue(self):
        if self.e_one == "1":
            click_save_sound.play()

    def gms(self):
        with open("game_configuration.txt", "r") as confff:
            self.a_one, self.b_one, self.c_one, self.d_one, self.e_one, self.f_one = confff.readline().split()
        main_menu_music.stop()
        if self.f_one == "1":
            game_music.play()

    def op_men_con(self):
        with open("game_configuration.txt", "r") as confff:
            self.a_one, self.b_one, self.c_one, self.d_one, self.e_one, self.f_one = confff.readline().split()
        dead_music.stop()
        dead_sound.stop()
        game_music.stop()
        if self.f_one == "1":
            main_menu_music.play()


class ShowPopup(GridLayout):
    a = ObjectProperty(.4)
    six_body = ObjectProperty()
    five_body = ObjectProperty()
    four_body = ObjectProperty()
    three_body = ObjectProperty()
    two_body = ObjectProperty()
    one_body = ObjectProperty()
    self_mode = ObjectProperty()
    switch_border = ObjectProperty()
    switch_sounds = ObjectProperty()
    switch_music = ObjectProperty()

    def __init__(self, **kwargs):
        super(ShowPopup, self).__init__(**kwargs)
        with open("game_configuration.txt", "r") as confo:
            a_on, b_on, c_on, d_on, e_on, f_on = confo.readline().split()

        self.a_two = a_on
        self.b_two = b_on
        self.c_two = c_on
        self.d_two = d_on
        self.e_two = e_on
        self.f_two = f_on

        if self.c_two == "Green":
            self.n = 1
            self.six_body.r = 0
            self.six_body.g = .84
            self.six_body.b = .24

            self.five_body.r = 0
            self.five_body.g = .84
            self.five_body.b = .24

            self.four_body.r = 0
            self.four_body.g = .84
            self.four_body.b = .24

            self.three_body.r = 0
            self.three_body.g = .84
            self.three_body.b = .24

            self.two_body.r = 0
            self.two_body.g = .84
            self.two_body.b = .24

            self.one_body.r = 0
            self.one_body.g = .56
            self.one_body.b = .2
        elif self.c_two == "Purple":
            self.n = 0
            self.six_body.r = .58
            self.six_body.g = .44
            self.six_body.b = .84

            self.five_body.r = .58
            self.five_body.g = .44
            self.five_body.b = .84

            self.four_body.r = .58
            self.four_body.g = .44
            self.four_body.b = .84

            self.three_body.r = .58
            self.three_body.g = .44
            self.three_body.b = .84

            self.two_body.r = .58
            self.two_body.g = .44
            self.two_body.b = .84

            self.one_body.r = .35
            self.one_body.g = .2
            self.one_body.b = .56
        elif self.c_two == "Orange":
            self.n = 2
            self.six_body.r = 1
            self.six_body.g = .62
            self.six_body.b = .36

            self.five_body.r = 1
            self.five_body.g = .62
            self.five_body.b = .36

            self.four_body.r = 1
            self.four_body.g = .62
            self.four_body.b = .36

            self.three_body.r = 1
            self.three_body.g = .62
            self.three_body.b = .36

            self.two_body.r = 1
            self.two_body.g = .62
            self.two_body.b = .36

            self.one_body.r = 1
            self.one_body.g = .4
            self.one_body.b = 0
        elif self.c_two == "Blue":
            self.n = 3
            self.six_body.r = .38
            self.six_body.g = .42
            self.six_body.b = .85

            self.five_body.r = .38
            self.five_body.g = .42
            self.five_body.b = .85

            self.four_body.r = .38
            self.four_body.g = .42
            self.four_body.b = .85

            self.three_body.r = .38
            self.three_body.g = .42
            self.three_body.b = .85

            self.two_body.r = .38
            self.two_body.g = .42
            self.two_body.b = .85

            self.one_body.r = 0
            self.one_body.g = .07
            self.one_body.b = .85
        elif self.c_two == "Pink":
            self.n = 4
            self.six_body.r = 1
            self.six_body.g = .62
            self.six_body.b = .78

            self.five_body.r = 1
            self.five_body.g = .62
            self.five_body.b = .78

            self.four_body.r = 1
            self.four_body.g = .62
            self.four_body.b = .78

            self.three_body.r = 1
            self.three_body.g = .62
            self.three_body.b = .78

            self.two_body.r = 1
            self.two_body.g = .62
            self.two_body.b = .78

            self.one_body.r = 1
            self.one_body.g = .31
            self.one_body.b = .58
        elif self.c_two == "Sea":
            self.n = 5
            self.six_body.r = .15
            self.six_body.g = .82
            self.six_body.b = .84

            self.five_body.r = .15
            self.five_body.g = .82
            self.five_body.b = .84

            self.four_body.r = .15
            self.four_body.g = .82
            self.four_body.b = .84

            self.three_body.r = .15
            self.three_body.g = .82
            self.three_body.b = .84

            self.two_body.r = .15
            self.two_body.g = .82
            self.two_body.b = .84

            self.one_body.r = .04
            self.one_body.g = .62
            self.one_body.b = .62
        elif self.c_two == "Black":
            self.n = 6
            self.six_body.r = .1
            self.six_body.g = .73
            self.six_body.b = .6

            self.five_body.r = .1
            self.five_body.g = .73
            self.five_body.b = .6

            self.four_body.r = .1
            self.four_body.g = .73
            self.four_body.b = .6

            self.three_body.r = .1
            self.three_body.g = .73
            self.three_body.b = .6

            self.two_body.r = .1
            self.two_body.g = .73
            self.two_body.b = .6

            self.one_body.r = .17
            self.one_body.g = .24
            self.one_body.b = .31

        if self.b_two == "1":
            self.self_mode.source = "normal_mode.png"
        elif self.b_two == "0":
            self.self_mode.source = "easy_mode.png"
        else:
            self.self_mode.source = "hard_mode.png"

        if self.a_two == "Yes":
            self.switch_border.source = "on_switch.png"
        else:
            self.switch_border.source = "off_switch.png"

        if self.e_two == "1":
            self.switch_sounds.source = "on_switch.png"
        else:
            self.switch_sounds.source = "off_switch.png"

        if self.f_two == "1":
            self.switch_music.source = "on_switch.png"
        else:
            self.switch_music.source = "off_switch.png"

    def change_mode_img(self):
        if self.self_mode.source == "easy_mode.png":
            self.self_mode.source = "normal_mode.png"
            self.b_two = 1
        elif self.self_mode.source == "normal_mode.png":
            self.self_mode.source = "hard_mode.png"
            self.b_two = 2
        elif self.self_mode.source == "hard_mode.png":
            self.self_mode.source = "easy_mode.png"
            self.b_two = 0

    def change_switch_border(self):
        if self.a_two == "Yes":
            self.a_two = "No"
        else:
            self.a_two = "Yes"

    def change_switch_sounds(self):
        if self.e_two == "1":
            self.e_two = 0
        else:
            self.e_two = 1

    def change_switch_music(self):
        if self.f_two == "1":
            self.f_two = 0
        else:
            self.f_two = 1

    def change_color(self):
        while True:
            m = randint(0, 6)
            if m != self.n:
                self.n = m
                break
        if self.n == 0:
            self.c_two = "Purple"
            self.six_body.r = .58
            self.six_body.g = .44
            self.six_body.b = .84

            self.five_body.r = .58
            self.five_body.g = .44
            self.five_body.b = .84

            self.four_body.r = .58
            self.four_body.g = .44
            self.four_body.b = .84

            self.three_body.r = .58
            self.three_body.g = .44
            self.three_body.b = .84

            self.two_body.r = .58
            self.two_body.g = .44
            self.two_body.b = .84

            self.one_body.r = .35
            self.one_body.g = .2
            self.one_body.b = .56
        elif self.n == 1:
            self.c_two = "Green"
            self.six_body.r = 0
            self.six_body.g = .84
            self.six_body.b = .24

            self.five_body.r = 0
            self.five_body.g = .84
            self.five_body.b = .24

            self.four_body.r = 0
            self.four_body.g = .84
            self.four_body.b = .24

            self.three_body.r = 0
            self.three_body.g = .84
            self.three_body.b = .24

            self.two_body.r = 0
            self.two_body.g = .84
            self.two_body.b = .24

            self.one_body.r = 0
            self.one_body.g = .56
            self.one_body.b = .2
        elif self.n == 2:
            self.c_two = "Orange"
            self.six_body.r = 1
            self.six_body.g = .62
            self.six_body.b = .36

            self.five_body.r = 1
            self.five_body.g = .62
            self.five_body.b = .36

            self.four_body.r = 1
            self.four_body.g = .62
            self.four_body.b = .36

            self.three_body.r = 1
            self.three_body.g = .62
            self.three_body.b = .36

            self.two_body.r = 1
            self.two_body.g = .62
            self.two_body.b = .36

            self.one_body.r = 1
            self.one_body.g = .4
            self.one_body.b = 0
        elif self.n == 3:
            self.c_two = "Blue"
            self.six_body.r = .38
            self.six_body.g = .42
            self.six_body.b = .85

            self.five_body.r = .38
            self.five_body.g = .42
            self.five_body.b = .85

            self.four_body.r = .38
            self.four_body.g = .42
            self.four_body.b = .85

            self.three_body.r = .38
            self.three_body.g = .42
            self.three_body.b = .85

            self.two_body.r = .38
            self.two_body.g = .42
            self.two_body.b = .85

            self.one_body.r = 0
            self.one_body.g = .07
            self.one_body.b = .85
        elif self.n == 4:
            self.c_two = "Pink"
            self.six_body.r = 1
            self.six_body.g = .62
            self.six_body.b = .78

            self.five_body.r = 1
            self.five_body.g = .62
            self.five_body.b = .78

            self.four_body.r = 1
            self.four_body.g = .62
            self.four_body.b = .78

            self.three_body.r = 1
            self.three_body.g = .62
            self.three_body.b = .78

            self.two_body.r = 1
            self.two_body.g = .62
            self.two_body.b = .78

            self.one_body.r = 1
            self.one_body.g = .31
            self.one_body.b = .58
        elif self.n == 5:
            self.c_two = "Sea"
            self.six_body.r = .15
            self.six_body.g = .82
            self.six_body.b = .84

            self.five_body.r = .15
            self.five_body.g = .82
            self.five_body.b = .84

            self.four_body.r = .15
            self.four_body.g = .82
            self.four_body.b = .84

            self.three_body.r = .15
            self.three_body.g = .82
            self.three_body.b = .84

            self.two_body.r = .15
            self.two_body.g = .82
            self.two_body.b = .84

            self.one_body.r = .04
            self.one_body.g = .62
            self.one_body.b = .62
        elif self.n == 6:
            self.c_two = "Black"
            self.six_body.r = .1
            self.six_body.g = .73
            self.six_body.b = .6

            self.five_body.r = .1
            self.five_body.g = .73
            self.five_body.b = .6

            self.four_body.r = .1
            self.four_body.g = .73
            self.four_body.b = .6

            self.three_body.r = .1
            self.three_body.g = .73
            self.three_body.b = .6

            self.two_body.r = .1
            self.two_body.g = .73
            self.two_body.b = .6

            self.one_body.r = .17
            self.one_body.g = .24
            self.one_body.b = .31

    def des_canvas(self):
        self.parent.clear_widgets()
        self.a = 0

    def save_options(self):
        with open("game_configuration.txt", "w") as new_conf:
            new_conf.write("{} {} {} {} {} {}".format(str(self.a_two), str(self.b_two), str(self.c_two),
                           str(self.d_two), str(self.e_two), str(self.f_two)))


class SettingsButton(ButtonBehavior, Image):
    sett_show = ObjectProperty()

    def show_popup(self):
        self.sett_show.clear_widgets()
        self.sett_show.add_widget(ShowPopup())


class GridButton(ButtonBehavior, GridLayout):
    pass


class ScoreFirst(Image):
    first_num = ObjectProperty("number_zero.png")
    d = int(d_one) // 100
    if d == 0:
        first_num = "number_zero.png"
    elif d == 1:
        first_num = "number_one.png"
    elif d == 2:
        first_num = "number_two.png"
    elif d == 3:
        first_num = "number_three.png"
    elif d == 4:
        first_num = "number_four.png"
    elif d == 5:
        first_num = "number_five.png"
    elif d == 6:
        first_num = "number_six.png"
    elif d == 7:
        first_num = "number_seven.png"
    elif d == 8:
        first_num = "number_eight.png"
    elif d == 9:
        first_num = "number_nine.png"


class ScoreSecond(Image):
    second_num = ObjectProperty("number_zero.png")
    p = (int(d_one) // 10) % 10
    if p == 0:
        second_num = "number_zero.png"
    elif p == 1:
        second_num = "number_one.png"
    elif p == 2:
        second_num = "number_two.png"
    elif p == 3:
        second_num = "number_three.png"
    elif p == 4:
        second_num = "number_four.png"
    elif p == 5:
        second_num = "number_five.png"
    elif p == 6:
        second_num = "number_six.png"
    elif p == 7:
        second_num = "number_seven.png"
    elif p == 8:
        second_num = "number_eight.png"
    elif p == 9:
        second_num = "number_nine.png"


class ScoreThird(Image):
    third_num = ObjectProperty("number_zero.png")
    s = int(d_one) % 10
    if s == 0:
        third_num = "number_zero.png"
    elif s == 1:
        third_num = "number_one.png"
    elif s == 2:
        third_num = "number_two.png"
    elif s == 3:
        third_num = "number_three.png"
    elif s == 4:
        third_num = "number_four.png"
    elif s == 5:
        third_num = "number_five.png"
    elif s == 6:
        third_num = "number_six.png"
    elif s == 7:
        third_num = "number_seven.png"
    elif s == 8:
        third_num = "number_eight.png"
    elif s == 9:
        third_num = "number_nine.png"


class FieldPart(Widget):
    r = NumericProperty(1)
    g = NumericProperty(1)
    b = NumericProperty(1)


class ImageButton(ButtonBehavior, Image):
    pass


class ResultScreen(GridLayout):
    pass


class SnakeApp(App):
    icon = "snake.ico"


if __name__ == "__main__":
    SnakeApp().run()
