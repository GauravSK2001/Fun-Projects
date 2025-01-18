class Rectangle():
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'


    def set_width(self,width):
        self.width=width
    def set_height(self,height):
        self.height=height
    def get_area(self):
        return self.height*self.width
    def get_perimeter(self):
        return 2*self.height+2*self.width
    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)
    def get_picture(self):
        image=''
        if self.height>=50 or self.width>=50:
            return 'Too big for picture.'
        for i in range(self.height):
            image+= '*'*self.width+'\n'
        return image
    def get_amount_inside(self,other):
        H =(self.height//other.height)
        W =(self.width//other.width)

        return int(H*W)

class Square(Rectangle):
    def __init__(self,side):
        super().__init__(width=side,height=side)
    def __str__(self):
        return f'Square(side={self.width})'
    def set_side(self,side):
        self.width = side
        self.height = side
    
    def set_width(self, width):
        self.set_side(width)
    
    def set_height(self, height):
        self.set_side(height)


