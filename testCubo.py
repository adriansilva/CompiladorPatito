import cuboSemantico as cs

cs.cubo('INT','FLOAT','*',1,1)
cs.cubo('BOOL','FLOAT','-',1,1)
cs.cubo('BOOL','INT','&&',1,1)
cs.cubo('CHAR','CHAR','-',2,0)
cs.cubo('CHAR','CHAR','/',0,2)
cs.cubo('INT','BOOL','>',1,1)
cs.cubo('INT','BOOL','<>',2,2)
cs.cubo('INT','BOOLa','*',1,1)
