import sys 
import subprocess


def write_to_file(line, filename, folder = './'):
    output_file = open(filename, 'a')
    output_file.write(line)
    output_file.close()
    
def writeln_to_file(line, filename, folder = './'):
    output_file = open(folder + filename, 'a')
    output_file.write(line+'\n')
    output_file.close()    
    
def run_command(command):   # to read from bash stdout
    p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,shell=True)
    p_res, p_err = p.communicate()
    return iter(p_res.readline, b'')

def call(command):
    subprocess.call(command, shell = True)    
    
def init_file(filename, folder = './'):   # make new empty file
    with open(folder+filename, 'w') as output_file:
        pass
 

def sort_by_value(dct):
    return sorted(dct.items(), key=lambda x:x[1]) 

