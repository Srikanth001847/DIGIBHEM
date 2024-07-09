import turtle
import time
import random

delay=0.1

#score
score=0
high_score=0

#setting up the screen
sc = turtle.Screen()
sc.title("Snake Game made by @Srikanth")
sc.bgcolor("black")
sc.setup(width=600, height=600)
sc.tracer(0)        #turns off the animation of the screen

#making snake head
head=turtle.Turtle()
head.speed(0)      #animation speed of the turtle.0 means fastest animation speed
head.shape("square")
head.color("dark blue")
head.penup()       #it does not draw anything
head.goto(0,0)     #head should be in the centre of the screen
head.direction="stop"

#Snake Food
food=turtle.Turtle()
food.speed(0)      #animation speed of the turtle.0 means fastest animation speed
food.shape("circle")
food.color("red")
food.penup()       #it does not draw anything
food.goto(0,100)     #head should be in the centre of the screen

#Snake Body
body=[]

#Pen
pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0 High Score: 0",align="center",font=("Courier",24,"normal"))
#Functions for game
def go_up():
    if head.direction!="down":
        head.direction="up"
def go_down():
     if head.direction!="up":
        head.direction="down" 
def go_left():
    if head.direction!="right":
        head.direction="left"
def go_right():
    if head.direction!="left":
        head.direction="right"           
def move():
    if head.direction == "up":
        y=head.ycor()     #y coordinate
        head.sety(y+20)
        
    if head.direction == "down":
        y=head.ycor()     
        head.sety(y-20)
    if head.direction == "left":
        x=head.xcor()     
        head.setx(x-20)
    if head.direction == "right":
        x=head.xcor()     
        head.setx(x+20) 

#Arrow keys
sc.listen()
sc.onkeypress(go_up,"w")
sc.onkeypress(go_down,"s") 
sc.onkeypress(go_left,"a") 
sc.onkeypress(go_right,"d")
                            
#Main Game loop
while True:       #repeat over and over
    sc.update()
    #collision with border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction="stop"
        
        #hide body
        for bodies in body:
            bodies.goto(1000,1000)
            
        #clear the body
        body.clear()   
        
        #Reset the score
        score=0 
        
        #reset the delay
        delay=0.1
        
        #update the score
        pen.clear()    
        pen.write("Score: {} High Score: {}".format(score,high_score),align="center",font=("Courier",24,"normal")) 
            
    #collision for food evaluation
    if head.distance(food) < 20:
        #move food at random position
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)
        
        #Add a body
        new_body=turtle.Turtle()
        new_body.speed(0)
        new_body.shape("square")
        new_body.color("green")
        new_body.penup()
        body.append(new_body)
        
        #shorten the delay
        delay-=0.001
        
       #increase score 
        score+=10
        
        if score>high_score:
            high_score=score
        pen.clear()    
        pen.write("Score: {} High Score: {}".format(score,high_score),align="center",font=("Courier",24,"normal"))    
    #move the body in reverse order
    
    for index in range(len(body)-1,0,-1):
        x=body[index-1].xcor()
        y=body[index-1].ycor()
        body[index].goto(x,y)
        
    #move body 0 to where the head is
    if len(body)>0:
        x=head.xcor()  
        y=head.ycor()
        body[0].goto(x,y)  
    move()                     
    #body collision evaluation
    for bodies in body:
        if bodies.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop" 
            
            #hide body
            for bodies in body:
                bodies.goto(1000,1000)
            
             #clear the body
            body.clear() 
            
            #Reset the score
            score=0 
            
            #reset the delay
            delay=0.1
        
            #update the score
            pen.clear()    
            pen.write("Score: {} High Score: {}".format(score,high_score),align="center",font=("Courier",24,"normal")) 
                    
             
    time.sleep(delay)
    
sc.mainloop()      #keep the window open for us