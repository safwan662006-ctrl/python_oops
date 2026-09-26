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

  def studentdetails(self, full_name, date_of_birth, gender, mobile_number, email, password):
        self.full_name = full_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.mobile_number = mobile_number
        self.email = email
        self.password = password
         if len(mobile_number) != 10:
            self.mobile_number = ("Mobile number must be 10 digits long.")