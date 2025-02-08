from manim import *
import xgj
class 凸透镜(Scene):
    def construct(self):
        self.always_update_mobjects=True
        ax=Axes(x_range=[-7,7],y_range=[-7,7],x_length=7,y_length=7).move_to([-0,0,0])
        ConvexLens=Intersection(Circle(radius=ax.c2p(np.sqrt(281))[0]).move_to(ax.c2p(-16,0)),Circle(radius=ax.c2p(np.sqrt(281))[0]).move_to(ax.c2p(16,0)),fill_opacity=0.5,color=RED).move_to(ax.c2p(0,0))
        ConvexLens.add_updater(lambda ConvexLens:ConvexLens.move_to(ax.c2p(0,0)))
        DotO=xgj.xgj.DotWithText(self,"O",DOWN)
        DotO[0].add_updater(lambda DotO:DotO[0].move_to(ax.c2p(0,0)))
        focal=ValueTracker(2)
        DotFL=xgj.xgj.DotWithText(self,"F",DOWN)
        DotFL[0].add_updater(lambda DotFL:DotFL[0].move_to(ax.c2p(-focal.get_value(),0)))
        DotFR=xgj.xgj.DotWithText(self,"F",DOWN)
        DotFR[0].add_updater(lambda DotFR:DotFR[0].move_to(ax.c2p(focal.get_value(),0)))
        ObjectX=ValueTracker(-4)
        ObjectY=ValueTracker(4)
        DotA=xgj.xgj.DotWithText(self,"A",UP+LEFT)
        DotA[0].add_updater(lambda DotA:DotA[0].move_to(ax.c2p(ObjectX.get_value(),0)))
        DotB=xgj.xgj.DotWithText(self,"B",LEFT)
        DotB[0].add_updater(lambda DotB:DotB[0].move_to(ax.c2p(ObjectX.get_value(),ObjectY.get_value())))
        ArrowAB=Arrow()
        ArrowAB.add_updater(lambda ArrowAB:ArrowAB.put_start_and_end_on(DotA[0].get_center(),DotB[0].get_center()))
        DotC=xgj.xgj.DotWithText(self,"C",RIGHT)
        DotC[0].add_updater(lambda DotC:DotC[0].move_to(ax.c2p(0,ObjectY.get_value())))
        DLineBC=DashedLine()
        DLineBC.add_updater(lambda DLineBC:DLineBC.put_start_and_end_on(DotB[0].get_center(),DotC[0].get_center()))
        def GetImage():
            if np.absolute(ObjectX.get_value()+2)<0.001:
                if ObjectX.get_value()<-2:
                    ImageX=100
                    ImageY=100
                else:
                    ImageX=-100
                    ImageY=-100
            else:
                CFk=xgj.xgj.ObliquePoint(self,0,ObjectY.get_value(),focal.get_value(),0)[0]
                CFb=xgj.xgj.ObliquePoint(self,0,ObjectY.get_value(),focal.get_value(),0)[1]
                BOk=xgj.xgj.ObliquePoint(self,ObjectX.get_value(),ObjectY.get_value(),0,0)[0]
                BOb=0
                ImageX=xgj.xgj.LineAndLine(self,CFk,CFb,BOk,BOb)[0]
                ImageY=xgj.xgj.LineAndLine(self,CFk,CFb,BOk,BOb)[1]
            return [ImageX,ImageY]
        DotD=xgj.xgj.DotWithText(self,"D",DOWN)
        DotD[0].add_updater(lambda DotD:DotD[0].move_to(ax.c2p(GetImage()[0],GetImage()[1])))
        DLineBD=DashedLine()
        DLineBD.add_updater(lambda DLineBD:DLineBD.put_start_and_end_on(DotB[0].get_center(),DotD[0].get_center()))
        DLineDC=DashedLine()
        DLineDC.add_updater(lambda DLineDC:DLineDC.put_start_and_end_on(DotD[0].get_center(),DotC[0].get_center()))
        DotE=xgj.xgj.DotWithText(self,"E",UP)
        DotE[0].add_updater(lambda DotE:DotE[0].move_to(ax.c2p(ax.p2c(DotD[0].get_center())[0],0)))
        ArrowED=Arrow()
        ArrowED.add_updater(lambda ArrowED:ArrowED.put_start_and_end_on(DotE[0].get_center(),DotD[0].get_center()))
        TABO=Polygon(DotA[0].get_center(),DotB[0].get_center(),DotO[0].get_center())
        TABO.add_updater(lambda TABO:TABO.become(Polygon(DotA[0].get_center(),DotB[0].get_center(),DotO[0].get_center(),color=BLUE,fill_opacity=0.5)))
        TEDO=Polygon(DotE[0].get_center(),DotD[0].get_center(),DotO[0].get_center())
        TEDO.add_updater(lambda TEDO:TEDO.become(Polygon(DotE[0].get_center(),DotD[0].get_center(),DotO[0].get_center(),color=BLUE,fill_opacity=0.5)))
        TCOF=Polygon(DotC[0].get_center(),DotO[0].get_center(),DotFR[0].get_center())
        TCOF.add_updater(lambda TCOF:TCOF.become(Polygon(DotC[0].get_center(),DotO[0].get_center(),DotFR[0].get_center(),color=GREEN,fill_opacity=0.5)))
        TDEF=Polygon(DotD[0].get_center(),DotE[0].get_center(),DotFR[0].get_center())
        TDEF.add_updater(lambda TDEF:TDEF.become(Polygon(DotD[0].get_center(),DotE[0].get_center(),DotFR[0].get_center(),color=GREEN,fill_opacity=0.5)))
        self.play(Create(ax))
        self.play(DrawBorderThenFill(ConvexLens),DrawBorderThenFill(VGroup(DotFL[0],DotFR[0],DotO[0])))
        self.play(Write(VGroup(DotFL[1],DotFR[1],DotO[1])))
        self.wait(2)
        self.play(DrawBorderThenFill(VGroup(DotA[0],DotB[0])))
        self.play(Write(VGroup(DotA[1],DotB[1])),DrawBorderThenFill(ArrowAB))
        self.wait(2)
        self.play(FadeIn(VGroup(DotD[2],DotC[2])))
        self.play(Create(VGroup(DLineBC,DLineBD,DLineDC)))
        self.play(DrawBorderThenFill(DotE[0]))
        self.play(Write(DotE[1]),DrawBorderThenFill(ArrowED))
        self.wait(2)
        self.play(ax.animate.move_to([-3,0,0]))
        self.wait(2)
        Text1=xgj.xgj.MakeVoiceProcess(self,captions=["过心不变","平行过焦"],Math=[False,False],first_localtion=[3,3,0],color=WHITE,size=40)
        self.wait(2)
        self.play(DLineBC.animate.set_color(YELLOW),DLineDC.animate.set_color(YELLOW))
        self.wait(2)
        self.play(DLineBD.animate.set_color(GREEN))
        self.wait(2)
        self.play(DLineBC.animate.set_color(WHITE),DLineDC.animate.set_color(WHITE),DLineBD.animate.set_color(WHITE),Unwrite(Text1))
        self.wait(2)
        self.play(ObjectX.animate.set_value(-6))
        self.wait(2)
        Text2=Text("当物距大于二倍焦距时，成倒立缩小的实像，像距在一倍到二倍焦距之间").move_to([2,3,0])
        Text2.font_size=20
        self.play(Write(Text2))
        self.wait(2)
        self.play(ObjectX.animate.set_value(-4))
        self.wait(2)
        Text3=Text("当物距等于两倍焦距时，成倒立等大的实像,像距等于二倍焦距").next_to(Text2,DOWN)
        Text3.font_size=20
        self.play(Write(Text3))
        self.wait(2)
        self.play(ObjectX.animate.set_value(-3))
        self.wait(2)
        Text4=Text("当物距在一倍到两倍焦距之间时，成倒立放大的实像，像距大于二倍焦距").next_to(Text3,DOWN)
        Text4.font_size=20
        self.play(Write(Text4))
        self.wait(2)
        self.play(ObjectX.animate.set_value(-1))
        self.wait(2)
        Text5=Text("当物距小于一倍焦距时，成正立放大的虚像，像距为负").next_to(Text4,DOWN)
        Text5.font_size=20
        self.play(Write(Text5))
        self.wait(2)
        self.play(Unwrite(VGroup(Text2,Text3,Text4,Text5)),ObjectX.animate.set_value(-5))
        self.wait(2)
        self.play(Create(VGroup(TABO,TEDO)))
        self.wait(2)
        TextTABO=MathTex(r"\triangle ABO").move_to([3,3,0])
        TextTABO.scale(2/3)
        TextSim1=MathTex(r"\sim ").next_to(TextTABO,RIGHT)
        TextSim1.scale(2/3)
        TextTEDO=MathTex(r"\triangle EDO").next_to(TextSim1,RIGHT)
        TextTEDO.scale(2/3)
        TABO.clear_updaters()
        TEDO.clear_updaters()
        self.play(TransformFromCopy(TABO,TextTABO),TransformFromCopy(TEDO,TextTEDO),Write(TextSim1))
        self.wait(2)
        Text6=xgj.xgj.MakeVoiceProcess(self=self,captions=[r"\frac{OA}{OE} =\frac{BA}{DE} ",r"\text{又}\because BA=CO",r"\frac{OA}{OE} =\frac{CO}{DE} "],Math=[True,True,True],color=WHITE,first_localtion=[TextSim1.get_x(),TextSim1.get_y()-0.5,0])
        self.wait(2)
        TCOF=Polygon(DotC[0].get_center(),DotO[0].get_center(),DotFR[0].get_center(),color=GREEN,fill_opacity=0.5)
        TDEF=Polygon(DotD[0].get_center(),DotE[0].get_center(),DotFR[0].get_center(),color=GREEN,fill_opacity=0.5)
        self.wait(2)
        self.play(Create(VGroup(TCOF,TDEF)))
        self.wait(2)
        TextSim2=MathTex(r"\sim ").next_to(Text6[2],DOWN)
        TextSim2.scale(2/3)
        TextTCOF=MathTex(r"\triangle COF").next_to(TextSim2,LEFT)
        TextTCOF.scale(2/3)
        TextTDEF=MathTex(r"\triangle DEF").next_to(TextSim2,RIGHT)
        TextTDEF.scale(2/3)
        self.play(TransformFromCopy(TCOF,TextTCOF),TransformFromCopy(TDEF,TextTDEF),Write(TextSim2))
        self.wait(2)
        Text7=xgj.xgj.MakeVoiceProcess(self,captions=[r"\frac{CO}{DE} =\frac{OF}{EF} ",r"\frac{OA}{OE} =\frac{OF}{EF} ",r"\text{设}OA=u,OE=v,OF=f",r"\therefore \frac{u}{v}=\frac{f}{v-f}  ",r"uv-uf=vf",r"\frac{1}{f} -\frac{1}{v} =\frac{1}{u} ",r"\frac{1}{f}  =\frac{1}{v}+\frac{1}{u} "],Math=[True,True,True,True,True,True,True],first_localtion=[TextSim2.get_x(),TextSim2.get_y()-0.5,0],size=20)
        self.wait(2)
        Gauss=Text7[6].copy()
        self.add(Gauss)
        self.play(FadeOut(VGroup(TABO,TextTABO,TEDO,TextTEDO,TCOF,TextTCOF,TDEF,TextTDEF,TextSim1,TextSim2,Text6,Text7)),Gauss.animate.move_to([3,3,0]))
        self.play(Gauss.animate.scale(1.5))
        self.wait(2)
        self.play(Unwrite(Gauss))
        self.wait(2)
        Text8=xgj.xgj.MakeVoiceProcess(self,captions=[r"\text{设物距为}u\text{，像距为}v\text{，焦距为}f\text{，物体高}h",r"\text{依据物理含义，可得}A(-u,0),B(-u,h),C(0,h),F_{\text{右}}(f,0)",r"CF:y=-\frac{h}{f} x+h",r"BO:y=-\frac{h}{u} x",r"-\frac{h}{f}x+h=-\frac{h}{u}  x",r"x=\frac{uf}{u-f} ",r"OE=v=\frac{uf}{u-f} ",r"\frac{1}{f}  =\frac{1}{v}+\frac{1}{u}"],Math=[True,True,True,True,True,True,True,True],first_localtion=[3,3,0],color=WHITE)
        self.wait(2)
        self.play(ObjectY.animate.set_value(6))
        self.wait(2)
        self.play(ObjectY.animate.set_value(2))
        self.wait(2)
        self.play(ObjectY.animate.set_value(4))
        self.wait(2)
        Gauss=Text8[7].copy()
        self.add(Gauss)
        self.play(FadeOut(Text8),Gauss.animate.move_to([3,3,0]))
        self.wait(2)
        Text9=xgj.xgj.MakeVoiceProcess(self,captions=[r"uv=uf+vf",r"(u-f)v=uf",r"v=\frac{uf}{u-f} "],Math=[True,True,True],first_localtion=[3,2.5,0])
        self.play(Text9[2].animate.set_color(RED))
        UAVR=Text9[2].copy()
        self.wait(2)
        self.add(UAVR)
        self.play(FadeOut(VGroup(Text9,Gauss)),UAVR.animate.to_edge(UL))
        self.wait(2)
        Text10=xgj.xgj.MakeVoiceProcess(self,captions=[r"\text{设AB}=h_{\text{物}},DE=h_{\text{像}}",r"\frac{OA}{OE} =\frac{BA}{DE} ",r"\frac{u}{v} = \frac{h_{\text{物}}}{h_{\text{像}}} ",r"=\frac{u}{\frac{uf}{u-f} } =\frac{u-f}{f} ",r"\text{当}u=2f\text{时},\frac{u-f}{f}=1,u=v,h_{\text{物}}=h_{\text{像}}",r"\text{当}f<u<2f\text{时},\frac{u-f}{f}<1,u<v,h_{\text{物}}<h_{\text{像}}",r"\text{当}u>2f\text{时},\frac{u-f}{f}>1,u>v,h_{\text{物}}>h_{\text{像}}",r"\text{当}u=f\text{时},v=\infty ",r"\text{当}0<u<f\text{时},\frac{\vert u-f \vert}{f} <1,u<v,h_{\text{物}}<h_{\text{像}}"],Math=[True,True,True,True,True,True,True,True,True],first_localtion=[3,3,0])


class UVFunction(Scene):
    def construct(self):
        self.always_update_mobjects=True
        ax=Axes(x_range=[0,10],y_range=[0,10],x_length=5,y_length=5).move_to([-4,0,0])
        func=ax.plot(lambda x:(x*2)/(x-2),x_range=[5/2,10])
        funcF=ax.plot(lambda x:4/x,x_range=[2/5,10])
        yf=ax.plot(lambda x:x**0+1,color=RED)
        Textyf=MathTex(r"y=f",color=yf.color).next_to(yf,RIGHT)
        y2f=ax.plot(lambda x:x**0+3,color=YELLOW)
        Texty2f=MathTex(r"y=2f",color=y2f.color).next_to(y2f,RIGHT)
        xf=Line(ax.c2p(2,0),ax.c2p(2,10),color=BLUE)
        Textxf=MathTex(r"x=f",color=xf.color).next_to(xf,UP).scale(2/3)
        x2f=Line(ax.c2p(4,0),ax.c2p(4,10),color=GREEN)
        Textx2f=MathTex(r"x=2f",color=x2f.color).next_to(x2f,UP).scale(2/3)
        ObjectX=ValueTracker(4)
        DotA=xgj.xgj.DotWithText(self,"A",UR)
        def GetDotA():
            x=ObjectX.get_value()
            y=(x*2)/(x-2)
            return [x,y]
        DotA[0].add_updater(lambda DotA:DotA[0].move_to(ax.c2p(GetDotA()[0],GetDotA()[1])))
        DotB=xgj.xgj.DotWithText(self,"B",UL)
        def GetDotB():
            DotAX=ObjectX.get_value()
            DotBX=0
            DotBY=0
            if DotAX<4:
                DotBX=2
                DotBY=ax.p2c(DotA[0].get_center())[1]
            elif DotAX==4:
                DotBX=100
                DotBY=100
            elif DotAX>4:
                DotBX=4
                DotBY=DotBY=ax.p2c(DotA[0].get_center())[1]
            return [DotBX,DotBY]
        DotB[0].add_updater(lambda DotB:DotB[0].move_to(ax.c2p(GetDotB()[0],GetDotB()[1])))
        DLineAB=DashedLine()
        def GetDLineAB():
            DotAcenter=DotA[0].get_center()
            DotBcenter=DotB[0].get_center()
            DotBX=ax.p2c(DotBcenter)[1]
            if DotBX>50:
                DLineAB.set_opacity(0)
            else:
                DLineAB.set_opacity(1)
            return [DotAcenter,DotBcenter]
        DLineAB.add_updater(lambda DLineAB:DLineAB.put_start_and_end_on(GetDLineAB()[0],GetDLineAB()[1]))



        DotC=xgj.xgj.DotWithText(self,"C",DOWN)
        def GetDotC():
            DotAX=ObjectX.get_value()
            DotCX=0
            DotCY=0
            if DotAX<4:
                DotCX=DotAX
                DotCY=4
            elif DotAX==4:
                DotCX=100
                DotCY=100
            elif DotAX>4:
                DotCX=DotAX
                DotCY=2
            return [DotCX,DotCY]
        DotC[0].add_updater(lambda DotC:DotC[0].move_to(ax.c2p(GetDotC()[0],GetDotC()[1])))
        DLineAC=DashedLine()
        def GetDLineAC():
            DotAcenter=DotA[0].get_center()
            DotCcenter=DotC[0].get_center()
            DotCX=ax.p2c(DotCcenter)[1]
            if DotCX>50:
                DLineAC.set_opacity(0)
            else:
                DLineAC.set_opacity(1)
            return [DotAcenter,DotCcenter]
        DLineAC.add_updater(lambda DLineAC:DLineAC.put_start_and_end_on(GetDLineAC()[0],GetDLineAC()[1]))
        self.wait(2)
        Text1=xgj.xgj.MakeVoiceProcess(self,captions=[r"v=\frac{uf}{u-f} ",r"v=\frac{uf+f^{2}-f^{2}  }{u-f} ",r"v=\frac{(u-f)f+f^{2}  }{u-f} ",r"v=f+\frac{f^{2}  }{u-f} "],Math=[True,True,True,True],first_localtion=[3,3,0])
        self.wait(2)
        self.play(Create(ax))
        self.play(Create(funcF))
        self.wait(2)
        self.play(Transform(funcF,func))
        self.wait(2)
        self.play(DrawBorderThenFill(DotA[0]),Write(DotA[1]))
        self.add(DotB[2],DotC[2],DLineAB,DLineAC)
        self.wait(2)
        self.play(Create(VGroup(x2f,y2f)),Write(VGroup(Textx2f,Texty2f)))
        self.wait(2)
        self.play(Create(VGroup(xf,yf)),Write(VGroup(Textxf,Textyf)))
        self.wait(2)
        funcText=Text1[3].copy()
        self.play(Unwrite(Text1),funcText.animate.move_to([3,3,0]))
        self.wait(2)
        self.play(ObjectX.animate.set_value(3))
        self.wait(2)
        Text2=MathTex(r"\text{当}f<u<2f\text{时，}v>2f\text{，而}x=f\text{是此函数渐近线，则此时}v>2f").next_to(funcText,DOWN)
        Text2.font_size=20
        self.play(Write(Text2))
        self.wait(2)
        self.play(ObjectX.animate.set_value(4))
        self.wait(2)
        Text3=MathTex(r"\text{当}f=2f\text{时，}v=2f").next_to(Text2,DOWN)
        Text3.font_size=20
        self.play(Write(Text3))
        self.wait(2)
        self.play(ObjectX.animate.set_value(7))
        self.wait(2)
        Text4=MathTex(r"\text{当}f>2f\text{时，}v<2f\text{，而}y=f\text{是此函数渐近线，则此时}f<v<2f").next_to(Text3,DOWN)
        Text4.font_size=20
        self.play(Write(Text4))
        self.wait(5)
        

class Ending(Scene):
    def construct(self):
        self.always_update_mobjects=True
        ax=Axes(x_range=[-7,7],y_range=[-7,7],x_length=7,y_length=7).move_to([-0,0,0])
        ConvexLens=Intersection(Circle(radius=ax.c2p(np.sqrt(281))[0]).move_to(ax.c2p(-16,0)),Circle(radius=ax.c2p(np.sqrt(281))[0]).move_to(ax.c2p(16,0)),fill_opacity=0.5,color=RED).move_to(ax.c2p(0,0))
        ConvexLens.add_updater(lambda ConvexLens:ConvexLens.move_to(ax.c2p(0,0)))
        DotO=xgj.xgj.DotWithText(self,"O",DOWN)
        DotO[0].add_updater(lambda DotO:DotO[0].move_to(ax.c2p(0,0)))
        focal=ValueTracker(2)
        DotFL=xgj.xgj.DotWithText(self,"F",DOWN)
        DotFL[0].add_updater(lambda DotFL:DotFL[0].move_to(ax.c2p(-focal.get_value(),0)))
        DotFR=xgj.xgj.DotWithText(self,"F",DOWN)
        DotFR[0].add_updater(lambda DotFR:DotFR[0].move_to(ax.c2p(focal.get_value(),0)))
        ObjectX=ValueTracker(-7)
        ObjectY=ValueTracker(4)
        DotA=xgj.xgj.DotWithText(self,"A",UP+LEFT)
        DotA[0].add_updater(lambda DotA:DotA[0].move_to(ax.c2p(ObjectX.get_value(),0)))
        DotB=xgj.xgj.DotWithText(self,"B",LEFT)
        DotB[0].add_updater(lambda DotB:DotB[0].move_to(ax.c2p(ObjectX.get_value(),ObjectY.get_value())))
        ArrowAB=Arrow()
        ArrowAB.add_updater(lambda ArrowAB:ArrowAB.put_start_and_end_on(DotA[0].get_center(),DotB[0].get_center()))
        DotC=xgj.xgj.DotWithText(self,"C",RIGHT)
        DotC[0].add_updater(lambda DotC:DotC[0].move_to(ax.c2p(0,ObjectY.get_value())))
        DLineBC=DashedLine()
        DLineBC.add_updater(lambda DLineBC:DLineBC.put_start_and_end_on(DotB[0].get_center(),DotC[0].get_center()))
        def GetImage():
            if np.absolute(ObjectX.get_value()+2)<0.001:
                if ObjectX.get_value()<-2:
                    ImageX=100
                    ImageY=100
                else:
                    ImageX=-100
                    ImageY=-100
            else:
                CFk=xgj.xgj.ObliquePoint(self,0,ObjectY.get_value(),focal.get_value(),0)[0]
                CFb=xgj.xgj.ObliquePoint(self,0,ObjectY.get_value(),focal.get_value(),0)[1]
                BOk=xgj.xgj.ObliquePoint(self,ObjectX.get_value(),ObjectY.get_value(),0,0)[0]
                BOb=0
                ImageX=xgj.xgj.LineAndLine(self,CFk,CFb,BOk,BOb)[0]
                ImageY=xgj.xgj.LineAndLine(self,CFk,CFb,BOk,BOb)[1]
            return [ImageX,ImageY]
        DotD=xgj.xgj.DotWithText(self,"D",DOWN)
        DotD[0].add_updater(lambda DotD:DotD[0].move_to(ax.c2p(GetImage()[0],GetImage()[1])))
        DLineBD=DashedLine()
        DLineBD.add_updater(lambda DLineBD:DLineBD.put_start_and_end_on(DotB[0].get_center(),DotD[0].get_center()))
        DLineDC=DashedLine()
        DLineDC.add_updater(lambda DLineDC:DLineDC.put_start_and_end_on(DotD[0].get_center(),DotC[0].get_center()))
        DotE=xgj.xgj.DotWithText(self,"E",UP)
        DotE[0].add_updater(lambda DotE:DotE[0].move_to(ax.c2p(ax.p2c(DotD[0].get_center())[0],0)))
        ArrowED=Arrow()
        ArrowED.add_updater(lambda ArrowED:ArrowED.put_start_and_end_on(DotE[0].get_center(),DotD[0].get_center()))
        TABO=Polygon(DotA[0].get_center(),DotB[0].get_center(),DotO[0].get_center())
        TABO.add_updater(lambda TABO:TABO.become(Polygon(DotA[0].get_center(),DotB[0].get_center(),DotO[0].get_center(),color=BLUE,fill_opacity=0.5)))
        TEDO=Polygon(DotE[0].get_center(),DotD[0].get_center(),DotO[0].get_center())
        TEDO.add_updater(lambda TEDO:TEDO.become(Polygon(DotE[0].get_center(),DotD[0].get_center(),DotO[0].get_center(),color=BLUE,fill_opacity=0.5)))
        TCOF=Polygon(DotC[0].get_center(),DotO[0].get_center(),DotFR[0].get_center())
        TCOF.add_updater(lambda TCOF:TCOF.become(Polygon(DotC[0].get_center(),DotO[0].get_center(),DotFR[0].get_center(),color=GREEN,fill_opacity=0.5)))
        TDEF=Polygon(DotD[0].get_center(),DotE[0].get_center(),DotFR[0].get_center())
        TDEF.add_updater(lambda TDEF:TDEF.become(Polygon(DotD[0].get_center(),DotE[0].get_center(),DotFR[0].get_center(),color=GREEN,fill_opacity=0.5)))
        self.add(ax,ConvexLens,DotO[2],DotA[2],DotB[2],DotC[2],DotD[2],DotE[2],DotFL[2],DotFR[2],ArrowAB,ArrowED,DLineBC,DLineBD,DLineDC)
        times=0
        while times<=10:
            times=times+1
            if times%2==0:
                self.play(ObjectX.animate.set_value(-0.7),time=4)
            else:
                self.play(ObjectX.animate.set_value(-7),time=4)




        
        
        

        
        
        

        


