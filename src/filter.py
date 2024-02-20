from typing import Dict, List, Tuple
from rapidfuzz.distance.DamerauLevenshtein import normalized_similarity


def get_hashtag_accounts(posts: List[Dict], hashtag: str) -> List[str]:
    """
    From a set of posts, returns the IDs of all accounts that posted a
    particular hashtag (excluding reposts)

    Parameters
    ----------
    posts:
        A list of dictionary records, where each record corresponds to one post.
        Keys are metadata fields for a post, and values are the metadata itself
    hashtag:
        The hashtag by which to filter

    Returns
    -------
    accounts:
        The IDs of all accounts that posted the `hashtag` (excluding reposts)
    """
    hashtag_accts = []

    for post in posts:

        repost = post["is_repost"]

        if repost:
            continue

        hashtags = post["hashtags"]
        if hashtags:
            for ht in hashtags:
                if ht == hashtag:
                    hashtag_accts.append(post["author_id"])

    return hashtag_accts


def get_similar_screen_names(
    accounts: List[Dict], min_similarity: float
) -> List[Tuple[str, str]]:
    """
    From a set of accounts, returns pairs of accounts that have similar screen
    names according to the normalized Damerau-Levenshtein similarity

    Parameters
    ----------
    accounts:
        A list of account records, where each record corresponds to one account.
        Keys are metadata fields for an account, and values are the metadata
        itself
    min_similarity:
        A value between 0 and 1, indicating the minimum similarity needed to
        determine two accounts have similar screen names

    Returns
    -------
    similar_account_pairs:
        A list of tuples of the format (account_id1, account_id2) indicating
        which accounts have similar screen names
    """

    similar_accts = []
    n = len(accounts)

    for i in range(n):

        account = accounts[i]
        screen_name = account["screen_name"]
        account_id = account["id"]

        for j in range(i + 1, n):

            comparison_account = accounts[j]

            if (
                normalized_similarity(screen_name, comparison_account["screen_name"])
                >= min_similarity
            ):
                similar_accts.append((account_id, comparison_account["id"]))

    return similar_accts
