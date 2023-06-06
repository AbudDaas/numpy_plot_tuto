#/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

class geom:
    def __init__(self, x0=0, y0=0):
        """
        """
        self.x0 = x0
        self.y0 = y0
        self.x = np.arange(-10, 11, 0.01)

    def line(self, m):
        """ 
        """
        return  m * (self.x - self.x0) + self.y0

    def ellipse(self, a, b):
        """ 
        """
        return self.y0 + np.sqrt(b**2 * (1 - ((self.x - self.x0)**2 / a**2)))
    
    def circle(self, r):
        """
        """
        return self.ellipse(r, r)
    
    def parabola(self, a, b):
        """
        """
        c = a * self.x0**2 + self.y0  # constant term
        return np.sqrt(-4*a*(self.x - self.x0)) + self.y0
    
    def parabola2(self, a, flag=0):
        """
        """
        y_pos_1 = self.y0 + np.sqrt(4*a*(self.x-self.x0))
        y_pos_2 = self.y0 + np.sqrt(-4*a*(self.x-self.x0))
            
        if flag==1:
            return y_pos_1
        elif flag==2:
            return y_pos_2
        else:
            return np.concatenate((y_pos_1, y_pos_2))
        
    def hyperpola(self, a, b):
        """ 
        """
        return self.y0 + np.sqrt((1+(self.x-self.x0)**2/b**2)*a**2)
         
    def visualize(self, shape="circle", **kwargs):
        """
        """
        if(shape=="circle"):
            ## TODO: 5 ---> kwrgs[0]
            r = 5
            y_pos  = self.circle(r)
            ## 5 ---> kwrgs[0]
            plt.legend(["p0 = (x0 ={}, y0 = {})".format(self.x0, self.y0), "radius={}".format(r)], loc="lower right")

        elif(shape=="line"):
            y_pos = self.line(1)
            ## TODO
            plt.legend(["p0 = (x0 ={}, y0 = {})".format(self.x0, self.y0), "slope={}".format(1)])
            

        elif(shape=="ellipse"):
            y_pos = self.ellipse(6, 14)
            ## TODO
            plt.legend(["p0= (x0 ={}, y0 = {})".format(self.x0, self.y0), "slope={}".format(6, 14)])
            

        elif(shape=="parabola"):
            y_pos = self.parabola(1, 3)
            ## TODO
            plt.legend(["p0 = (x0 = {}, y0 = {})".format(self.x0, self.y0), "slope ={}".format(1, 3)])
            
        elif(shape == "parabola2"):
            y_pos =self.parabola2(2, 1)
            plt.legend(["p0 = (x0 = {}, y0 = {})".format(self.x0, self.y0), "slope = {}".format(2, 1)])
        elif(shape=="hyperpola"):
            y_pos = self.hyperpola(1, 2)
            ## TODO
            plt.legend(["p0 = (x0 ={}, y0 = {})".format(self.x0, self.y0), "slope = {}".format(1, 2)])

        else:
            print("shape {} is not defined!!".format(shape))
        
       
        y_neg = - y_pos

        plt.xlabel("X-Axis")
        plt.ylabel("Y-Axis")

        plt.xlim(-20, 20)
        plt.ylim(-20, 20)

        plt.plot(self.x, y_pos, color='g')
        if(shape!='line'):
            plt.plot(self.x, y_neg, color='g')
        elif(shape!='parabola'):
            plt.plot(self.x, y_neg, color='g')

        plt.scatter(self.x0, self.y0)
        plt.grid()

if __name__=="__main__":
    try:
        geom_ = geom(x0=0, y0=0)
        geom_.visualize(shape='hyperpola')
        plt.show()

    except Exception as e: 
        print(e)

    finally:
        pass