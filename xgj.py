from manim import *
import edge_tts
import asyncio
from pydub import AudioSegment
async def speaking(text="你好"):
    tts=edge_tts.Communicate(text=text,voice="zh-CN-XiaoxiaoNeural")
    await tts.save("E:\\你的路径\\speakingsound\\"+text+".mp3")
    return "E:\\你的路径\\speakingsound\\"+text+".mp3"
def GetLength(path="hallo"):
    return len(AudioSegment.from_file(path))/1000
class xgj(Scene):
    def DotWithText(self,text="A",L=DOWN):
        CDOT=Dot()
        CDOTTEXT=Text(text=text,font_size=30)
        CDOTTEXT.add_updater(lambda CDOTTEXT:CDOTTEXT.next_to(CDOT,L))
        G=VGroup(CDOT,CDOTTEXT)
        return [CDOT,CDOTTEXT,G]
    def ObliquePoint(self,ax=1,ay=1,bx=2,by=2):
        k=(ay-by)/(ax-bx)
        b=ay-k*ax
        return [k,b]
    def 定长(self,k=1,b=1,x=1,r=1):
        dx=[((2*x+2*k**2*x)-np.sqrt((2*x+2*k**2*x)**2-4*(k**2+1)*(x**2+k**2*x**2-r**2)))/(2*(k**2+1)),((2*x+2*k**2*x)+np.sqrt((2*x+2*k**2*x)**2-4*(k**2+1)*(x**2+k**2*x**2-r**2)))/(2*(k**2+1))]
        dy=[dx[0]*k+b,dx[1]*k+b]
        return [dx[0],dy[0],dx[1],dy[1]]
    def TangentOfQuadraticFunction(self,a,b,c,e,f,In=False):
        if In == False:
            lam=np.sqrt(a*e*b+a**2*e**2+a*c-a*f)
            k1=b+2*a*e+2*lam
            b1=f-b*e-2*a*e**2-2*e*lam
            k2=b+2*a*e-2*lam
            b2=f-b*e-2*a*e**2+2*e*lam
            x1=(k1-b)/(2*a)
            x2=(k2-b)/(2*a)
            y1=a*x1**2+b*x1+c
            y2=a*x2**2+b*x2+c
        else:
            k1=2*a*e+b
            b1=f-e*k1
            k2=k1
            b2=b1
            x1=e
            y1=f
            x2=x1
            y2=y1
        return [k1,b1,k2,b2,x1,y1,x2,y2]
    def UpdaterLine(self,line=Line(),DotA=Dot(),DotB=Dot()):
        line.add_updater(lambda line:line.put_start_and_end_on(DotA.get_center(),DotB.get_center()))
    def MakeProcess(self,captions=["a"],saying=["same","你好"],Math=[True],first_localtion=[0,0,0],color=WHITE):
        index=-1
        TextArray=[]
        for cap in captions:
            index=index+1
            if Math[index] == True:
                a=MathTex(captions[index])
                a.set_color(color=color)
            else:
                a=Text(captions[index])
                a.set_color(color=color)
            a.font_size=20
            if index == 0:
                a.move_to(first_localtion)
            else:
                a.next_to(TextArray[index-1],DOWN)
            if saying[index] == "same":
                b=asyncio.run(speaking(text=cap))
            else:
                b=asyncio.run(speaking(text=saying[index]))
            self.add_sound(b)
            self.play(FadeIn(a))
            self.wait(len(AudioSegment.from_file(b))/1000)
            TextArray.append(a)
        TextVGroup=VGroup()
        for textcontent in TextArray:
            TextVGroup.add(textcontent)
        return TextVGroup
    def GetLine(self,Line=Line(),isax=False,ax=Axes()):
        if isax == True:
            x1=ax.p2c(Line.get_start())[0]
            y1=ax.p2c(Line.get_start())[1]
            x2=ax.p2c(Line.get_end())[0]
            y2=ax.p2c(Line.get_end())[1]
        else:
            x1=Line.get_start()[0]
            y1=Line.get_start()[1]
            x2=Line.get_end()[0]
            y2=Line.get_end()[1]
        return xgj.ObliquePoint(self=self,ax=x1,ay=y1,bx=x2,by=y2)
    def ronate(self,x,y,a,b,angel):
        ronatex=((x-a)*np.cos(angel))+((y-b)*np.sin(angel)+a)
        ronatey=(-(x-a)*np.sin(angel))+((y-b)*np.cos(angel)+b)
        return [ronatex,ronatey]
    def QFLine(self,a=1,b=1,c=1,k=1,bL=1):
        Deerta=(b-k)**2-4*a*(c-bL)
        x1=(k-b-np.sqrt(Deerta))/(2*a)
        y1=a*x1**2+b*x1+c
        x2=(k-b+np.sqrt(Deerta))/(2*a)
        y2=a*x2**2+b*x2+c
        return [x1,y1,x2,y2]
    def LineAndLine(self,k1=1,b1=1,k2=1,b2=1):
        x=(b2-b1)/(k1-k2)
        y=k1*x+b1
        return [x,y]
    def ParabolaAndLine(self,a=1,b=1,c=1,k=1,v=1):
        x1=(k-b-np.sqrt(b**2-2*b*k+k**2+4*a*v-4*a*c))/(2*a)
        y1=k*x1+v
        x2=(k-b+np.sqrt(b**2-2*b*k+k**2+4*a*v-4*a*c))/(2*a)
        y2=k*x2+v
        return [x1,y1,x2,y2]
    def captions(self,text="请输入文本",localtion="center",iscoordinate=False,coordinatelocaltion=[0,0,0],time=3.0,deleteafterrunning=True,color=WHITE,islatex=False,scale=40,isspeaking=False,isdifferenttext=False,differenttext="你好"):
        if islatex == True:
            captext=MathTex(text,color=color)
            captext.font_size=scale
        else:
            captext=Text(text,color=color)
            captext.font_size=scale
        if iscoordinate == True:
            captext.move_to(coordinatelocaltion)
        elif localtion == "center":
            captext.move_to([0,0,0])
        elif localtion == "edgedown":
            captext.to_edge(DOWN)
        elif localtion == "edgeup":
            captext.to_edge(UP)
        if isspeaking == True:
            if isdifferenttext == True:
                a=asyncio.run(speaking(text=differenttext))
            else:
                a=asyncio.run(speaking(text=text))
            self.add_sound(a)
            self.play(Write(captext),run_time=GetLength(a))
        else:
            self.play(Write(captext))
        if deleteafterrunning == True:
            if time == 0:
                self.play(Unwrite(captext))
            else:
                self.wait(time)
                self.play(Unwrite(captext))
        return captext
    def DoVertical(self,m=1,n=1,k=1,b=1):
        dotx=(k*n-k*b+m)/(k**2+1)
        doty=(k**2*n+k*m+b)/(k**2+1)
        return [dotx,doty]
    def beginning(self):
        TBOM=ImageMobject("TBOM.png")
        XGJ=ImageMobject("XGJ.png")
        XGJ.scale(0.5)
        self.wait()
        self.play(FadeIn(TBOM))
        xgj.captions(self=self,text="大家好，这里是数学之美",time=0,isspeaking=True,localtion="edgedown")
        self.play(FadeOut(TBOM),FadeIn(XGJ))
        xgj.captions(self=self,text="同时我也是B站的修改君",time=0,isspeaking=True,localtion="edgedown")
        return XGJ
    def circleY(self,center=[1,1,0],radius=1,x=1,IsUp=True):
        a=center[0]
        b=center[1]
        r=radius
        if IsUp == True:
            return b+np.sqrt(-1*x**2+2*a*x-a**2+r**2)
        else:
            return b-np.sqrt(-1*x**2+2*a*x-a**2+r**2)
    def IntersectionCircleAndLine(self,a=1,b=1,r=1,k=1,m=1):
        FuncA=1+k**2
        FuncB=2*k*m-2*k*b-2*a
        FuncC=a**2+b**2+m**2-2*m*b-r**2
        x1=(-FuncB-np.sqrt(FuncB**2-4*FuncA*FuncC))/(2*FuncA)
        y1=k*x1+m
        x2=(-FuncB+np.sqrt(FuncB**2-4*FuncA*FuncC))/(2*FuncA)
        y2=k*x2+m
        return [x1,y1,x2,y2]
    def MakeVoiceProcess(self,captions=["a"],Math=[True],first_localtion=[0,0,0],color=WHITE,size=20):
        index=-1
        TextArray=[]
        for cap in captions:
            index=index+1
            if Math[index] == True:
                a=MathTex(captions[index])
                a.set_color(color=color)
            else:
                a=Text(captions[index])
                a.set_color(color=color)
            a.font_size=size
            if index == 0:
                a.move_to(first_localtion)
            else:
                a.next_to(TextArray[index-1],DOWN)
            self.play(FadeIn(a))
            TextArray.append(a)
            self.wait(2)
        TextVGroup=VGroup()
        for textcontent in TextArray:
            TextVGroup.add(textcontent)
        return TextVGroup

