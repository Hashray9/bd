from kivy.uix.videoplayer import VideoPlayer
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen,ScreenManager

screen_helper='''
#: import NoTransition kivy.uix.screenmanager.NoTransition
ScreenManager:
    Namescreen:
    questionscreen:
    questionscreen1:
    questionscreen2:
    questionscreen3:
    questionscreen4:
    questionscreen5:
    questionscreen6:
    questionscreen7:
    ans:
    hashray:

<hashray>:
    name:"video"
    Video:
        id: video_player
        source: ''
        state: 'stop'         
<ans>:
    name:"vidbut"
    MDLabel:
        id:gname
        text:"Just Kidding :) , I made this for fun , Thank you very much for wishing "
        bold:True
        halign:"center"
    
    MDRaisedButton:
        text:"bug"
        pos_hint:{"center_x":0.35,"center_y":0.4}
        on_release: app.play_video()
    MDRaisedButton:
        text:"billi"
        pos_hint:{"center_x":0.64,"center_y":0.4}
        on_release: app.play_video1()
    MDLabel:
        id: display_text
        text: ""
        halign: "center"
        pos_hint: {"center_x": 0.5, "center_y": 0.6}
    
       
<Namescreen>:
    name:"Name"
    id:ns
    Image:
        source:"img.jpg"
        size_hint:None,None
        size:250,200
        pos_hint:{"center_x":0.5,"center_y":0.75}

    MDTextField:
        id:user
        
        hint_text:"Enter your name:"
        helper_text: "#--->"
        helper_text_mode: "on_focus"
        pos_hint:{"center_x":0.5,"center_y":0.5}
        size_hint_x:None
        width:300
    MDRaisedButton:
        text:"Go ahead"
        pos_hint:{"center_x":0.5,"center_y":0.4}
        on_press:
            root.manager.transition=NoTransition()
            root.manager.current="ques"
            app.root.current = "ques"; app.pass_data(root.ids.user.text)

              
        

<questionscreen>
    name:"ques"
    MDLabel:
        id:c
        text:"Are you DUMB?"
        bold:True
        halign:"center"
    MDRaisedButton:
        text:"No"
        pos_hint:{"center_x":0.35,"center_y":0.4}
        on_press:
            root.manager.transition=NoTransition()
            root.manager.current="ques1"
    MDRaisedButton:
        text:"yes"
        pos_hint:{"center_x":0.64,"center_y":0.4}
        on_press:
            root.manager.current="vidbut"
        on_release: app.play_video()
            
       
            

        
<questionscreen1>
    name:"ques1"
    MDLabel:
        text:"Are you DUMB?"
        bold:True
        halign:"center"
    MDRaisedButton:
        text:"No"
        pos_hint:{"center_x":0.12,"center_y":0.4}
        on_press: 
            root.manager.transition=NoTransition()
            root.manager.current="ques2"

    MDRaisedButton:
        text:"yes"
        pos_hint:{"center_x":0.64,"center_y":0.4}
        on_press:
            root.manager.current="vidbut"
          


<questionscreen2>
    name:"ques2"
    MDLabel:
        text:"Are you DUMB?"
        bold:True
        halign:"center"
    MDRaisedButton:
        text:"No"
        pos_hint:{"center_x":0.12,"center_y":0.8}
        on_press: 
            root.manager.transition=NoTransition()
            root.manager.current="ques3"

    MDRaisedButton:
        text:"yes"
        pos_hint:{"center_x":0.64,"center_y":0.4}
        on_press:
            root.manager.current="vidbut"

        
<questionscreen3>
    name:"ques3"
    MDLabel:
        text:"Are you DUMB?"
        bold:True
        halign:"center"
    MDRaisedButton:
        text:"No"
        pos_hint:{"center_x":0.85,"center_y":0.1}
        on_press: 
            root.manager.transition=NoTransition()
            root.manager.current="ques4"

    MDRaisedButton:
        text:"yes"
        pos_hint:{"center_x":0.64,"center_y":0.4}
        on_press: 
            root.manager.current="vidbut"

        
<questionscreen4>
    name:"ques4"
    MDLabel:
        text:"Are you DUMB?"
        bold:True
        halign:"center"
    MDRaisedButton:
        text:"No"
        pos_hint:{"center_x":0.3,"center_y":0.7}
        on_press: 
            root.manager.transition=NoTransition()
            root.manager.current="ques5"

    MDRaisedButton:
        text:"yes"
        pos_hint:{"center_x":0.64,"center_y":0.4}
        on_press:
            root.manager.current="vidbut"

        
<questionscreen5>
    name:"ques5"
    MDLabel:
        text:"Are you DUMB?"
        bold:True
        halign:"center"
    MDRaisedButton:
        text:"No"
        pos_hint:{"center_x":0.1,"center_y":0.1}
        on_press:
            root.manager.transition=NoTransition() 
            root.manager.current="ques6"

    MDRaisedButton:
        text:"yes"
        pos_hint:{"center_x":0.64,"center_y":0.4}
        on_press:
            root.manager.current="vidbut"

        
<questionscreen6>
    name:"ques6"
    MDLabel:
        text:"Are you DUMB?"
        bold:True
        halign:"center"
    MDRaisedButton:
        text:"No"
        pos_hint:{"center_x":0.64,"center_y":0.23}
        on_press: 
            root.manager.transition=NoTransition()
            root.manager.current="ques7"

    MDRaisedButton:
        text:"yes"
        pos_hint:{"center_x":0.64,"center_y":0.4}
        on_press:
            root.manager.current="vidbut"

        
<questionscreen7>
    name:"ques7"
    MDLabel:
        text:"Are you DUMB?"
        bold:True
        halign:"center"
    MDRaisedButton:
        text:"No"
        pos_hint:{"center_x":0.32,"center_y":0.4}
        on_press: 
            root.manager.transition=NoTransition()
            root.manager.current="ques"

    MDRaisedButton:
        text:"yes"
        pos_hint:{"center_x":0.64,"center_y":0.4}
        on_press:
            root.manager.current="vidbut"
    
'''


class ans(Screen):
    pass
class hashray(Screen):
    pass
class Namescreen(Screen):
    pass
class questionscreen(Screen):
    pass
class questionscreen1(Screen):
    pass
class questionscreen2(Screen):
    pass
class questionscreen3(Screen):
    pass
class questionscreen4(Screen):
    pass
class questionscreen5(Screen):
    pass
class questionscreen6(Screen):
    pass
class questionscreen7(Screen):
    pass

sm=ScreenManager()
sm.add_widget(Namescreen(name="Name"))
sm.add_widget(ans(name="vidbut"))
sm.add_widget(hashray(name="video"))
sm.add_widget(questionscreen(name="ques"))
sm.add_widget(questionscreen1(name="ques1"))
sm.add_widget(questionscreen2(name="ques2"))
sm.add_widget(questionscreen3(name="ques3"))
sm.add_widget(questionscreen4(name="ques4"))
sm.add_widget(questionscreen5(name="ques5"))
sm.add_widget(questionscreen6(name="ques6"))
sm.add_widget(questionscreen7(name="ques7"))

class fun(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        screen = Builder.load_string(screen_helper)
        return screen

    def play_video(self):
        video_path = 'bug.mp4'  # Replace with your video file path
        video_player = self.root.get_screen("video").ids.video_player

        if video_path:
            video_player.source = video_path
            video_player.state = 'play'

    def play_video1(self):
        video_path = 'VID_20230817122542.mp4'  # Replace with your video file path
        video_player = self.root.get_screen("video").ids.video_player

        if video_path:
            video_player.source = video_path
            video_player.state = 'play'

    def pass_data(self, text):
        ans = self.root.get_screen("vidbut")
        ans.ids.display_text.text = text
fun().run()