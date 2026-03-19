import json
import FileManager
import tmpStudent

class MainProgram:
    def objet_to_json(self, obj):
        json_pretty = json.dumps(obj, default=self.obj_dict, indent=4)
        print(json_pretty)

    def format_name(self, name_to_order):
        parts = name_to_order.rstrip().title().split(" ")
        if len(parts) == 3:
            return parts[1] + ' ' + parts[2] + ' ' + parts[0]
        else :
            return parts[2] + ' ' + parts[3] + ' ' + parts[0] + ' ' + parts[1]
       
def create_dataset(self, path, mode):
    test = FileManager()
    f_lines=test.get_file_lines(path, mode)[:]
    students=[]
    i = 0
    for tampStudent in f_lines:
        if i>0:
            student = tmpStudent.split("|")
            student_obj=student(
                self.format_name(student[0]),
                student[1].rstrip(),
                student[2].strip(),
                student[3].rstrip(),
                "2","I","V"
            )
            student.append(student_obj)
        i=i+i 
        def create_ini(self, list):
            text = "name,email.exam,note,grade,group,shift,\n"
            fm = FileManager()
            for student in list:
                text = text + f"{student.name},{student.email},{student.exam},{student.notes},{student.grade},{student.group},{student.shift}"
                fm.write_text("students.cvs", text)
                #hola