from app.models.Subject import SubjectCreate

class SubjectUtil:

    def format_subject(self, subject) -> SubjectCreate:
        return {
            "id": str(subject["_id"]),
            "name": subject["name"],
            "alias": subject["alias"],
            "description": subject["description"], 
            "time": str(subject['time']),
            "amount_question": str(subject["amount_question"]),
            "min_correct_question_to_pass": str(subject["min_correct_question_to_pass"]),
            "generate_exam_type": subject["generate_exam_type"]
        }



# class SubjectCreate(BaseModel):
#     id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
#     name: str
#     alias: str
#     description: Optional[str] = None
#     time: int
#     amount_question: int
#     min_correct_question_to_pass: int
#     generate_exam_type: str = GENERATE_EXAM_TYPE.ORDER
#     class Config:
#         allow_population_by_field_name = True
#         arbitrary_types_allowed = True
#         json_encoders = {ObjectId: str}
#         schema_extra = {
#             "example": {
#                 "name": "Toán cao cấp",
#                 "alias": 'TCC1',
#                 "description": "Công nghệ thông tin và truyền thông",
#                 "time": 20211,
#                 "amount_question": 30,
#                 "min_correct_question_to_pass": 15,
#                 "generate_exam_type": "RANDOM"

#             }
#         }

    