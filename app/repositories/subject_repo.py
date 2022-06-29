
from app.utils.subject_util import SubjectUtil
from app.models.Subject import SubjectCreate, UpdateSubjectModel
from fastapi import Body, status, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from . import *


class SubjectRepo(BaseRepo):

    def __init__(self, collection: str="subjects") -> None:
        super().__init__()
        self.collection = self.mydb[collection]

    def get_all_subject(self):
        res = list(self.collection.find({}))
        # print(res)
        list1 = []
        for response in res:
            # print(response)
            # print(SubjectUtil().format_subject(response))
            list1.append(SubjectUtil().format_subject(response))
        # list1 = [SubjectUtil().format_subject(response) for response in res]
        # print(list1)
        return list1

    def get_subject(self, id: str):
        subject = self.collection.find_one({"_id": id})
        return JSONResponse(status_code=status.HTTP_200_OK, content=subject)
        # count = 0
        # for record in subjects:
        #     count += 1
        # if count < 1:
        #     return None
        # else:
        #     return SubjectUtil.format_subject(subjects[0])

    def create_subject(self, new_subject: SubjectCreate = Body(...)):
        subject = jsonable_encoder(new_subject)
        new_subj = self.collection.insert_one(subject)
        created_subj = self.collection.find_one({"_id": new_subj.inserted_id})
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_subj)

    def delete_subject(self, id: str):
        delete_result = self.collection.delete_one({"_id": id})

        if delete_result.deleted_count == 1:
            return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)

        raise HTTPException(status_code=404, detail=f"Subject {id} not found")

    def update_subject(self, id: str, subj: UpdateSubjectModel = Body(...)):
        subject = {k: v for k, v in subj.dict().items() if v is not None}
        if len(subject) >=1:
            update_result = self.collection.update_one({"_id": id}, {"$set": subject})
            if update_result.modified_count == 1:
                if (
                    updated_subj := self.collection.find_one({"_id": id})
                ) is not None:
                    return updated_subj

        if (existing_subj := self.collection.find_one({"_id": id})) is not None:
            return existing_subj
        
        raise HTTPException(status_code=404, detail=f"Subject {id} not found")
