# # context manager

# class FileManager():
#     def __init__(self,file_name,mode):
#         self.file_name=file_name
#         self.mode=mode
#         self.file=None

# def __enter__(self):
#     self.file=open(self.file_name,self.mode)
#     return self.file
   

# def __exit__(self, exc_type, exc_value, exc_traceback):
#         self.file.close()

# with FileManager('test1.txt', 'w') as f:
#     f.write('helloooolllllllllllll')
 
