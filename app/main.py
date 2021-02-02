from typing import Any, List

from fastapi import Depends, FastAPI, HTTPException
from pydantic import UUID4
from sqlalchemy.orm import Session
from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND

from . import actions, models, schemas
from .db import SessionLocal, engine

# Create all tables in the database.
# Comment this out if you using migrations.
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency to get DB session.
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/")
def index():
    return {"message": "Tamatara Landing Backend"}


# --------------------------------- #
#       NEWSLETTER                  #
# --------------------------------- #

@app.get("/newsletters", response_model=List[schemas.Newsletter], tags=["newsletters"])
def list_newsletters(
    db: Session = Depends(get_db), skip: int = 0, limit: int = 100
) -> Any:
    newsletters = actions.newsletter.get_all(db=db, skip=skip, limit=limit)
    return newsletters


@app.post(
    "/newsletters",
    response_model=schemas.Newsletter,
    status_code=HTTP_201_CREATED,
    tags=["newsletters"],
)
def create_newsletter(
    *, db: Session = Depends(get_db), newsletter_in: schemas.NewsletterCreate
) -> Any:
    newsletter = actions.newsletter.create(db=db, obj_in=newsletter_in)
    return newsletter


# @app.put(
#     "/newsletter/{id}",
#     response_model=schemas.Newsletter,
#     responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
#     tags=["newsletters"],
# )
# def update_newsletter(
#     *, db: Session = Depends(get_db), id: UUID4, newsletter_in: schemas.NewsletterUpdate,
# ) -> Any:
#     newsletter = actions.newsletter.get(db=db, id=id)
#     if not newsletter:
#         raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Newsletter not found")
#     newsletter = actions.newsletter.update(db=db, db_obj=newsletter, obj_in=newsletter_in)
#     return newsletter


@app.get(
    "/newsletters/{id}",
    response_model=schemas.Newsletter,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["newsletters"],
)
def get_newsletter(*, db: Session = Depends(get_db), id: UUID4) -> Any:
    newsletter = actions.newsletter.get(db=db, id=id)
    if not newsletter:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND, detail="Newsletter not found"
        )
    return newsletter


# @app.delete(
#     "/newsletter/{id}",
#     response_model=schemas.Newsletter,
#     responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
#     tags=["newsletters"],
# )
# def delete_newsletter(*, db: Session = Depends(get_db), id: UUID4) -> Any:
#     newsletter = actions.newsletter.get(db=db, id=id)
#     if not newsletter:
#         raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Newsletter not found")
#     newsletter = actions.newsletter.remove(db=db, id=id)
#     return newsletter


@app.put(
    "/newsletters/{id}/optoup",
    response_model=schemas.Newsletter,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["newsletters"],
)
def optout_newsletter(*, db: Session = Depends(get_db), id: UUID4) -> Any:
    return actions.newsletter.optout(db=db, id=id)


# --------------------------------- #
#       MAILING LIST                #
# --------------------------------- #

@app.get("/mailing_lists", response_model=List[schemas.MailingList], tags=["mailing_lists"])
def list_mailing_lists(
    db: Session = Depends(get_db), skip: int = 0, limit: int = 100
) -> Any:
    mailing_lists = actions.mailing_list.get_all(db=db, skip=skip, limit=limit)
    return mailing_lists


@app.post(
    "/mailing_lists",
    response_model=schemas.MailingList,
    status_code=HTTP_201_CREATED,
    tags=["mailing_lists"],
)
def create_mailing_list(
    *, db: Session = Depends(get_db), mailing_list_in: schemas.MailingListCreate
) -> Any:
    mailing_list = actions.mailing_list.create(db=db, obj_in=mailing_list_in)
    return mailing_list


# @app.put(
#     "/mailing_list/{id}",
#     response_model=schemas.MailingList,
#     responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
#     tags=["mailing_lists"],
# )
# def update_mailing_list(
#     *, db: Session = Depends(get_db), id: UUID4, mailing_list_in: schemas.MailingListUpdate,
# ) -> Any:
#     mailing_list = actions.mailing_list.get(db=db, id=id)
#     if not mailing_list:
#         raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="MailingList not found")
#     mailing_list = actions.mailing_list.update(db=db, db_obj=mailing_list, obj_in=mailing_list_in)
#     return mailing_list


@app.get(
    "/mailing_lists/{id}",
    response_model=schemas.MailingList,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["mailing_lists"],
)
def get_mailing_list(*, db: Session = Depends(get_db), id: UUID4) -> Any:
    mailing_list = actions.mailing_list.get(db=db, id=id)
    if not mailing_list:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND, detail="MailingList not found"
        )
    return mailing_list


# @app.delete(
#     "/mailing_list/{id}",
#     response_model=schemas.MailingList,
#     responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
#     tags=["mailing_lists"],
# )
# def delete_mailing_list(*, db: Session = Depends(get_db), id: UUID4) -> Any:
#     mailing_list = actions.mailing_list.get(db=db, id=id)
#     if not mailing_list:
#         raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="MailingList not found")
#     mailing_list = actions.mailing_list.remove(db=db, id=id)
#     return mailing_list


@app.put(
    "/mailing_lists/{id}/optoup",
    response_model=schemas.MailingList,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["mailing_lists"],
)
def optout_mailing_list(*, db: Session = Depends(get_db), id: UUID4) -> Any:
    return actions.mailing_list.optout(db=db, id=id)
