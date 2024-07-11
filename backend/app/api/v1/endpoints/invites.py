from typing import Annotated, Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.core.security import get_current_athlete
from app.db.session import get_session

# from app.utils.invite import send_invite

router = APIRouter()
Session = Annotated[Session, Depends(get_session)]
CurrentAthlete = Annotated[models.Athlete, Depends(get_current_athlete)]


@router.post('/create', response_model=schemas.Invite, status_code=201)
def create_invite(
    db: Session,
    current_athlete: CurrentAthlete,
    invite_in: schemas.InviteCreate,
) -> Any:

    # valida se o time está cadastrado
    team = crud.team.get_by_id_and_owner(
        db=db, team_id=invite_in.team_id, athlete_id=current_athlete.id
    )
    if not team:
        raise HTTPException(
            status_code=404, detail='Invalid or nonexistent team'
        )

    # valida se a corrida está cadastrada
    race = crud.race.get_by_id_and_onwer(
        db=db, race_id=invite_in.race_id, athlete_id=current_athlete.id
    )

    if not race:
        raise HTTPException(
            status_code=404, detail='Invalid or nonexistent race'
        )

    invite = crud.invite.create(
        db=db, invite_in=invite_in, athlete_id=current_athlete.id
    )

    # send_invite(
    #     db=db,
    #     invite=invite,
    #     sender=current_athlete.name,
    #     race_name=race.name,
    #     team_name=team.name,
    # )

    return invite

    # TODO cadastrar convidado como atleta do time
