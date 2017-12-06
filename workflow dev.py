#coding=utf-8
import xml.etree.ElementTree as ET
input_file = []
output_file= []
arguments = []
executable = []
should_transfer_files = []
log = []
error = []
output = []
universe = []
when_to_transfer_output = []
a = []
id = []
tree = ET.parse('C:/Users/sunta/Desktop/ZZXNOVA2.0/fofofo.xml')
work=tree.getroot()
first = work.findall('phase/node')
pre = []
post = []
for one in first:
    id.append(one.get('id'))
    for child in list(one):
        if(child.tag == 'input_file'):
            input_file.append(child.text)
        elif(child.tag == 'output_file'):
            output_file.append(child.text)
        elif(child.tag == 'arguments'):
            arguments.append(child.text)
        elif(child.tag == 'executable'):
            executable.append(child.text)
        else:
            pass

two = work.findall('phase/node/other')
for t in two:
    for child in list(t):
        if(child.tag == 'Universe'):
            universe.append(child.text)
        elif(child.tag == 'should_transfer_files'):
            should_transfer_files.append(child.text)
        elif(child.tag == 'when_to_transfer_output'):
            when_to_transfer_output.append(child.text)
        elif(child.tag == 'Log'):
            log.append(child.text)
        elif(child.tag == 'error'):
            error.append(child.text)
        elif(child.tag == 'output'):
            output.append(child.text)
        elif(child.tag == 'a'):
            a.append(child.text)
        else:
            pass
			


s = 'C:/Users/sunta/Desktop/ZZXNOVA2.0'
l = [executable,universe,a]
ss = ['executable = ','universe = ','']

#generate sub file
for i in range(len(id)):
    f = open(s+'/node_'+id[i]+'.sub',"w")
    f.write('requirements=(Target.OpSys == "WINDOWS")&&(Target.name == "slot1@SHAOHAN-PC")\n')
    for j in range(3):
        f.write(ss[j])
        f.write(l[j][i])
        f.write('\n')
    
    f.close()
#print(id)
#generate dag file
three = work.findall('phase/parent')
ff = open('C:/Users/sunta/Desktop/ZZXNOVA2.0/workflow.dag',"w")
s = 'job'
s0 = 'parent'
s1 = 'child'
for i in range(len(id)):
    ff.write(s+' node_'+id[i]+' node_'+id[i]+'.sub'+'\n')
for thr in three:
    ff.write(s0+' node_'+thr.get('ref')+' '+s1)
    for child in list(thr):
        ff.write(' node_'+child.get('ref'))
    ff.write('\n')
ff.close()
'''
#add pre/post script
s2 = 'script'
s3 = 'pre'
s4 = 'post'
four = work.findall('phase/script')
for m in four:
    print(m.tag+m.text)
    for child in list(m):
        print(child.tag+':'+child.text)
        if(child.tag == 'pre'):
            pre.append(child.text)
        else:
            post.append(child.text)
for i in range(len(id)):
    ff.write(s2+' '+s3+' node_'+str(i+1)+' '+pre[0]+' node_'+str(i+1)+'.sub'+'\n')
    ff.write(s2+' '+s4+' node_'+str(i+1)+' '+post[0]+' node_'+str(i+1)+'.sub'+'\n')
print(pre)
print(post)
'''
lo = work.findall('phase/loop')
for l in lo:
    loop = l.text
print(loop)
ff.close()