Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> tao = turtle.Pen()
>>> tao.shape('turtle')
>>> tao1={'color':'green','dis':100}
>>> tao.color(tao1['color'])
>>> def rect(tao_object,tdict):
...     for i in range(4):
...         tao_object.forward(tdict['dis'])
...         tao_object.left(90)
... 
...         
>>> 
>>> rect(tao,tao1)
>>> tao2=turtle.Pen()
>>> tao2dict={'color':'green','dis':50}
>>> tao.color(tao2dict['color'])
>>> rect(tao2,tao2dict)
>>> tao2dict={'color':'green','dis':50}
>>> 
>>> tao2dict={'color':'red','dis':50}
>>> tao.color(tao2dict['color'])
>>> rect(tao2,tao2dict)
