import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.properties import NumericProperty
from kivy.config import Config
from kivy.lang import Builder
Builder.load_file("Calculator.kv")
Config.set('kivy','window_icon',os.getcwd()+"/data/icon.png")
Config.set('graphics', 'resizable', '1')


class calculatorGUI(GridLayout):
    count=0
    inputText=''
    result=''
    operators=('+','-','*','/','^','=')


    def calculate(self):
        pass
        if not self.input.text[-1].isdigit():
            self.inputText=self.input.text[:-1]
        if '^' in self.inputText:
            i=self.inputText.index('^')
            # print("present at "+str(i)+self.inputText[:i-1]+self.inputText[i:])
            self.inputText=self.inputText[:i]+"**"+self.inputText[i+1:]
            
        # print(self.inputText)
        self.result=str(eval(self.inputText))

        
        


    def inputDisplay(self,value):
        pass
        if(value=='AC'):
            pass
            self.display.text=''
            self.input.text=''
            return
        
        if(value=='C'):
            pass
            if len(self.input.text)>1:
                self.input.text=self.input.text[:-1]
                self.inputText=self.input.text
                self.calculate()
                self.display.text=self.result
            else:
                self.display.text=''
                self.input.text=''
            return
        if value=='=':
            pass
            self.display.text=''
            self.input.text=self.result
            return

        if self.input.text=='' and not value.isdigit():
            self.input.text='0'
        if self.input.text=='0' and value.isdigit():
            self.input.text=''
        if(value in self.operators and self.input.text[-1] in self.operators):
            self.input.text=self.input.text[:-1]
        self.input.text+=value
        self.inputText=self.input.text
        self.calculate()
        self.display.text=self.result



class CalculatorApp(App):
    def build(self):
        # Config.write()
        return calculatorGUI()

if __name__ == '__main__':
    CalculatorApp().run()