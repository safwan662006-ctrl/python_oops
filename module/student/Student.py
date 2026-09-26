class StudentClass:
    def __init__(
        self,
        full_name=None,
        date_of_birth=None,
        age=None,
        gender=None,
        mobile_number=None,
        email_address=None,
        preferred_language=None,
        school_college_name=None,
        class_grade=None,
        board_curriculum=None,
        academic_year=None,
        subjects=None,
        current_level=None,
        areas_of_help=None,
        parent_guardian_name=None,
        relationship_with_student=None,
        parent_mobile_number=None,
        parent_email_address=None,
        preferred_communication_method=None,
    ):
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
        self.subjects = subjects or {}
        self.current_level = current_level or {}
        self.areas_of_help = areas_of_help or []

        self.parent_guardian_name = parent_guardian_name
        self.relationship_with_student = relationship_with_student
        self.parent_mobile_number = parent_mobile_number
        self.parent_email_address = parent_email_address
        self.preferred_communication_method = preferred_communication_method

        self.parent_guardian_details = {
            "name": self.parent_guardian_name,
            "relationship_with_student": self.relationship_with_student,
            "mobile_number": self.parent_mobile_number,
            "email_address": self.parent_email_address,
            "preferred_communication_method": self.preferred_communication_method,
        }

