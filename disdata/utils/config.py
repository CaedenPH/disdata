from typing import List, Dict


class Config:
    """
    Represents the database config.

    Parameters
    ----------
    lock_database: `bool`
        Determines whether or not the database server should be locked
        and no members can join the server
    force_lock: `bool`
        Determines whether to force kick everyone in the database server
    whitelisted_members: `List[int]`
        List of user ids that are allowed inside the database server
    """

    lock_database: bool
    force_lock: bool
    whitelisted_members: List[int]

    @classmethod
    def from_dict(cls, dict: Dict[str, str]):
        cls = Config
        if "lock_database" in dict:
            cls.lock_database = dict["lock_database"]
        if "force_lock" in dict:
            cls.force_lock = dict["force_lock"]
        if "whitelisted_members" in dict:
            cls.whitelisted_members = dict["whitelisted_members"]
        return cls
