from django.utils import timezone
from ..dto.competition_dto import CompetitionDTO
from ..models import Competition


class CompetitionHandle:

    @classmethod
    def create(cls,competition_dto: CompetitionDTO):
        ## 构建比赛实体
        competition = Competition(
            name = competition_dto.name,
            turn = competition_dto.turn,
            victor_name = competition_dto.victor_name,
            start_date = timezone.now(),
        )
        competition.save();
        return {'id':competition.id,'name':competition.name}
    
    @classmethod
    def update(cls,competition_dto: CompetitionDTO):
        ## 构建比赛实体
        competition = Competition(
            id = competition_dto.id,
            turn = competition_dto.turn,
            victor_name = competition_dto.victor_name,
            end_date = competition_dto.end_date
        )
        competition.save(update_fields=["turn","victor_name","end_date"]);
        return {'id':competition.id,'name':competition.name}
    

class CompetitionQuery:

    @classmethod
    def get(cls,id:int):
       return Competition.objects.get(id=id)