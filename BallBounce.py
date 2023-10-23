import math
class BallBounce:

    #Creating the ball
    def __init__(self, velo, angle):
        self.initialVelo = velo
        self.iYVelo = self.initialVelo*math.sin(math.radians(angle))
        self.xVelo = self.initialVelo*math.cos(math.radians(angle))
        self.yVelo = self.iYVelo
        
        self.yPos = 580
        self.iYPos = self.yPos
        self.xPos = 20
        
        self.fps = 60.0
        self.frame = 0
        
    #Uses kinematic equations to determine the balls position       
    def fall(self):
        #Frames is used to see how many seconds it has been once 60 frames pass 1 second has passed
        self.frame = self.frame +1
        self.yPos = self.iYPos - self.iYVelo * (self.frame / self.fps) + 0.5 * 9.8 * (self.frame/self.fps)*(self.frame/self.fps)
        self.xPos = self.xPos + self.xVelo*(1 / self.fps)
        self.yVelo = self.yVelo - 9.8*(1/self.fps)
        
        
    #Wall Collision
    ##Bounds are (800, 600) radius = 20
    #If ball passes a barrier by going through it reverse the direction and reset the equation to preserve momentum
    def Collision(self):
        if (self.yPos > 580 and self.yVelo < 0) or (self.yPos < 20 and self.yVelo < 0 ):
            #Reset equation by making a new trajectory for ball
            self.frame = 0
            #save ypos
            self.iYPos = self.yPos
            #Update velocities
            self.iYVelo = -1*self.yVelo
            self.yVelo = self.iYVelo
            
        if (self.xPos > 780 and self.xVelo > 0) or (self.xPos < 20 and self.xVelo < 0 ):
            #reset equation for new trajectory
            self.frame = 0
            #save ypos
            self.iYPos = self.yPos
            #Updating velocities, conserving energy
            self.xVelo = -1*self.xVelo
            self.iYVelo = self.yVelo
            
    #Getter Methods to return position values back to drawBall
    def returnXPos(self):
        return self.xPos
        
    def returnYPos(self):
        return self.yPos
        
    
    
    