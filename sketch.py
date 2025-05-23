from p5 import *


def setup():
  createCanvas(400, 400)
  global redSlider, greenSlider, blueSlider
  redSlider = createSlider(0,255, 200)
  greenSlider = createSlider(0,255,200)
  blueSlider = createSlider(0,255,200)


def draw():
  global redSlider,greenSlider, blueSlider
  #          R  G  B
  background(redSlider.value(), greenSlider.value(), blueSlider.value())
  #drawTickAxes()

  # stars
  fill('gold')
  circle (100,100,100)

  # rocket body
  fill("blue")
  rect(mouseX,mouseY,100,200)
  
  fill("red")
  # top triangle
  triangle(mouseX+50,mouseY+300, mouseX, mouseY+200, mouseX+100, mouseY+200)
  # left triangle
  triangle(mouseX,mouseY+100,mouseX-50,mouseY,mouseX,mouseY)
  # right triangle
  triangle(mouseX+100,mouseY+100,mouseX+150,mouseY,mouseX+100,mouseY)

  #windows
  fill("black")
  circle(mouseX+50,mouseY+150,50)
  fill("black")
  circle(mouseX+50,mouseY+50,50)

  

 
