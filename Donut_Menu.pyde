def setup():
    global donut
    size(1000, 1000)
    background(204, 241, 255)
    donut = loadImage("donut.png")
def draw():
    global donut
    image(donut,0,0,1000,1000)
    fill(0)
    textAlign(CENTER)
    textSize(100)
    text("Title", 500, 200)
    textSize(30)
    text("Game Start", 500, 400)
    text("Options", 500, 500)
    text("Credits", 500, 600)
    
    if((mouseX > 390) and (mouseX < 580) and (mouseY > 380) and (mouseY < 400)):
        ellipseMode(CENTER)
        stroke(0)
        fill(0)
        ellipse(400, 390, 10, 10)
        stroke(204, 241, 255)
        fill(204, 241, 255)
        rect(370, 450, 60, 160)
    if((mouseX > 390) and (mouseX < 580) and (mouseY > 380) and (mouseY < 400) and (mousePressed == True)):
        print("yeet")
        #start game
                        
    if((mouseX > 390) and (mouseX < 580) and (mouseY > 480) and (mouseY < 500)):
        ellipseMode(CENTER)
        stroke(0)
        fill(0)
        ellipse(400, 490, 10, 10)
        stroke(204, 241, 255)
        fill(204, 241, 255)
        rect(380, 380, 30, 30)
        rect(380, 580, 30, 30)
    if((mouseX > 390) and (mouseX < 580) and (mouseY > 480) and (mouseY < 500) and (mousePressed == True)):
        print("yeet")
        #go to options
        
    if((mouseX > 390) and (mouseX < 580) and (mouseY > 580) and (mouseY < 600)):
        ellipseMode(CENTER)
        stroke(0)
        fill(0)
        ellipse(400, 590, 10, 10)
        stroke(204, 241, 255)
        fill(204, 241, 255)
        rect(370, 380, 40, 160)
    if((mouseX > 390) and (mouseX < 580) and (mouseY > 580) and (mouseY < 600) and (mousePressed == True)):
        print("yeet")
        #go to credits
