from fastapi import FastAPI
from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

from filter import get_hashtag_accounts, get_similar_screen_names


class Post(BaseModel):
    id: str
    created_at: datetime
    author_id: str
    is_repost: bool
    text: str
    hashtags: Optional[List[str]]


class Account(BaseModel):
    id: str
    created_at: datetime
    screen_name: str


class InputData(BaseModel):
    posts: List[Post]
    accounts: List[Account]
    hashtag: str
    min_similarity: float


app = FastAPI()


@app.get("/pairs")
def similar_posts(data: InputData):
    data_json = data.model_dump()
    filt_accts = get_hashtag_accounts(posts=data_json['posts'], hashtag=data_json['hashtag'])
    hashtag_accts = [acct for acct in data_json['accounts'] if acct['id'] in filt_accts]
    sim_accts = get_similar_screen_names(
        accounts=hashtag_accts, min_similarity=data.min_similarity
    )
    return {"similar_account_pairs": sim_accts}
