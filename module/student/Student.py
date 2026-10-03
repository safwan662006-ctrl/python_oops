class StudentClass:
    def __init__(self):
        self.full_name = None
        self.date_of_birth = None
        self.age = None
        self.gender = None
        self.mobile_number = None
        self.email_address = None
        self.preferred_language = None
        self.school_college_name = None
        self.class_grade = None
        self.board_curriculum = None
        self.academic_year = None


        self.subjects = None
        self.current_level = None
        self.areas_of_help = None
        self.parent_guardian_name = None
        self.relationship_with_student = None
        self.parent_mobile_number = None
        self.parent_email_address = None
        self.preferred_communication_method = None
        self.email = None
        self.password = None

    def SetUserName(self, email, password):
        self.email = email
        self.password = password

    def setStudentDetails(self, full_name, date_of_birth, age, gender, mobile_number, email_address, preferred_language, school_college_name, class_grade, board_curriculum, academic_year):
        self.full_name = full_name
        self.date_of_birth = date_of_birth
        self.age = age
        self.gender = gender
        self.mobile_number = mobile_number
        self.email_address = email_address
        self.preferred_language = preferred_language
        self.school_college_name = school_college_name
        self.class_grade = class_grade
        self.board_curriculum = board_curriculum
        self.academic_year = academic_year
        



    def savetoDB(self):
        import sqlite3
        connection =sqlite3.connect("tution.db")
        cursor =connection.cursor()                
        cursor.execute(
                    """
                    INSERT INTO Student(
                    name,
                    full_name,
                    age,
                    mobile_number,
                    email_address,
                    password,
                    date_of_birth,
                    gender,
                    preffered_language,
                    school_college_name,
                    class_grade,
                    board_curriculum,
                    academic_year
                    ) valuesz(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                   """ (
                    self.name,
                    self.fullname,
                    self.age,
                    self.mobile_number,
                    self.email_address,
                    self.password,
                    self.date_of_birth,
                    self.gender,
                    self.preferred_language,
                    self.school_college_name,
                    self.class_grade,
                    self.board_curriculum,
                    self.academic_year
                ))

                    

                #save changes and close connection
        connection.commit()
        connection.close()
