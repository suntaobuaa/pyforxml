#coding=utf-8
import xml.etree.ElementTree as ET
import os

tree = ET.parse('C:/Users/sunta/Desktop/test_3')
root = tree.getroot()


def mkbat():
	for x in root:
		for y in x:
			for z in y:
				for child in z:
				   if child.attrib.get('property'):
					   if child.attrib['property']=='attributes':
						   node_cmd =child[4][1].text
						   node_name = z[2][0].text
						   fp= open('%s.bat'%(node_name),"w")
						   fp.write(node_cmd)
						   fp.close()
						   print(node_name,node_cmd)
if __name__=='__main__':
    mkbat()




def findchild(nodename):
    childlist =[]
    for evelement in root.iter():
        if evelement.attrib.get('class'):
            if evelement.attrib['class']=='org.jgraph.graph.DefaultEdge':
               if evelement[0][3][1].text==nodename:                
                   childlist.append(evelement[0][2][1].text)

     
    return childlist








            
            

        


            