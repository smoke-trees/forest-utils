import os
import json

CURR_DIR = os.getcwd()

def create_dir_tree():
    folder_name = input('Give the name of the model you want to choose : ')
    try:
        os.mkdir(folder_name)
    except:
        print("Folder cannot be created, try different name")
        return
    
    create_json(folder_name)
    create_docs_folder(folder_name)
    create_template_folder(folder_name)
    
def create_json(FOLDER):
    print('Creating config file!!')
    
    params = {}
    params['Title'] = 'Enter title here'
    params['Tags'] = []
    params['Architecture'] = 'Explain the architecture type'
    params['Publisher'] =  ['<name1>','<name2>']
    params['Links to Pub Tabs'] = []
    params['Problem Domain'] = 'Give problem domain Egs Image, Text'
    params['Model Format'] = 'Format of the model'
    params['Language'] = 'Language'
    params['Dataset'] = 'docs/dataset.md'
    params['Overview'] = 'docs/overview.md'
    params['Preprocessing'] = 'templates/<template_filename>'
    params['Link'] = '<link to pretrained model>'
    params['References'] = 'docs/references.md'
    params['Usage'] = 'templates/<usage_filename>'
    
    with open(os.path.join(CURR_DIR, FOLDER, 'result.json'), 'w') as file:
        json.dump(params, file, indent=2)
        
def create_docs_folder(FOLDER):
    print('Creating docs folder!!')
    os.mkdir(os.path.join(CURR_DIR, FOLDER, 'docs'))
    DOCS_FOLDER = os.path.join(CURR_DIR, FOLDER, 'docs')
    
    with open(os.path.join(DOCS_FOLDER, 'references.md'), 'w') as ref_file:
        ref_file.write("## References\n")
        ref_file.write("- [Add-Reference-Name](<Add-reference-link-here>)\n")
        ref_file.write("- ...\n")
        
    with open(os.path.join(DOCS_FOLDER, 'overview.md'), 'w') as desc_file:
        desc_file.write("## Model Overview\n")
        desc_file.write("Explain about your model with figures and maths.")                
        
    with open(os.path.join(DOCS_FOLDER, 'dataset.md'), 'w') as data_file:
        data_file.write("## About Dataset\n")
        data_file.write("Explain about the dataset used and give details about it.\n")
        data_file.write("### **Links to database**\n")
        data_file.write("- [Dataset-name](<Add-dataset-link-here>)\n")
        data_file.write("- ...")
        
      
def create_template_folder(FOLDER):
    print('Creating templates folder!!')
    os.mkdir(os.path.join(CURR_DIR, FOLDER, 'templates'))
