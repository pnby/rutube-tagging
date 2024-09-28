from typing import List, Optional

from pydantic import BaseModel


#
# A scheme for storing tags and the percentage of occurrence of tags in the array of current tags
#
class TagSchema(BaseModel):
    tags: List[str]
    occurrences: Optional[float] = None

#
# Defines the scheme of the tags in which they will be in their raw form
#
class TagRawSchema(BaseModel):
    tags: str