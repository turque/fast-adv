import typer
from rich import print, prompt
from sqlalchemy.orm import Session

from app import crud
from app.db.session import get_session
from app.schemas.athlete import AthleteCreate
from app.utils.secrets import generate_password

app = typer.Typer(rich_markup_mode='rich')


@app.command()
def create_athlete(
    super: bool = False,
):
    """
    Create new athlete.
    """
    name = prompt.Prompt.ask('[blue]Nome[/blue]')
    email = prompt.Prompt.ask('[blue]E-mail[/blue]')

    db: Session = next(get_session())

    athlete_in_db = crud.athlete.get_by_email(db=db, athlete_email=email)

    if athlete_in_db:
        print('[red]Athlete already registered[/red]')
        raise typer.Exit(code=1)

    athlete_in = AthleteCreate(name=name, email=email)
    athlete_in.password = generate_password()
    athlete = crud.athlete.create(db=db, obj_in=athlete_in)

    print(
        f"""Create athlete [green]{athlete.name}[/green] \n
        e-mail: [green]{athlete.email}[/green] \n
        password: [red]{athlete_in.password}[/red]"""
    )


if __name__ == '__main__':
    db = get_session()
    app()
