# py_search_box
## Feature:
- Input:
  - List of sentence (Which will be final answer).
  - Query string.
  - List of selected filter to be applied
- Output:
  - List of matching sentence to given query.
- Process:
  - Applying filters like convert to lower case, upper case, space divider, stop word filter, synonyms filter.

## Upgrade options:
  - [ ] Adding feature of index. Index means user can predefine some important matching in given sentence list for matching with query. for example: you could have an index rating of product in you sentence. Search can answer questions like "list T-shirt having rating more than 4?"
  - [ ] Direct communicate with SQL database with defined filed names.
  - [ ] Spelling correction according to words in sentence.
  - [x] Add RESTfull flask API
