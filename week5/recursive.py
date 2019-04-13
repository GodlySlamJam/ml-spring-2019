 # Dom(tag, id, tagAttributes, text, children)
class Dom:
    def __init__(self, tag, id="", tagAttributes="", text="", children=""):
        self.tag = tag
        self.children = children
        self.text = text
        self.all = tag + ":" + text
        # if(children == True):
        #     self.all = tag + ":" + children
        #     print(children)
        # if(text == True):
        #     self.text = text
        print(self)
all = None
def recurs(page, level=0):
    all = all + "\n" + page.tag
    if(isinstance(page.children, list)):
        for x in page.children:
            all = all + "\n"+"   "  + x.all
            if(isinstance(x.children, list)):
                for y in x.children:
                    recurs(y, level)
                #     if(isinstance(y.children, list)):
                #         for z in y.children:
                #             all = all + "\n" + "         " + z.all



webpage = Dom("html", children=[
     Dom("head", children=[
         Dom("title", text="deep learning for dummies")
     ]),
     Dom("body", children=[
         Dom("h1", text="The four noble truths"),
         Dom("ul", children=[
             Dom("li", text="What's suffering?"),
             Dom("li", text="The cause of suffering"),
             Dom("li", text="The end of suffering"),
             Dom("li", text="A path to the end of suffering"),
         ]),
         Dom("p", id="last_mark", text="This is the end, my only friend.")
     ])
 ])
saying = recurs(webpage)
print(all)
