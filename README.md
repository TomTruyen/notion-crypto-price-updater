# NotionCryptoPriceUpdater

## Created by [Gareth Evens](https://www.youtube.com/channel/UCowfhbZ-yU3Db16nS-HNVEA)

## Setup guides

[Written guide](https://heygarethevans.notion.site/Setup-Instructions-e907297617104d5d850ca403922413cd)

[Video Guide](https://www.youtube.com/watch?v=7Yc06t7oY7s)

- Also copy `my_variables.example.yml` to `my_variables.yml`. Value for the token can be found under the integration on Notion

## Notion

NOTE: when filling in the table, the following fields are REQUIRED:

- Name (ticker of crypto)
- Amount invested
- Number of coins in wallet
- Price/coin should be not empty (so either manually input a value like "0" OR EASIER just set a filter rule like `price/coin NOT EMPTY` this will automatically fill in 0 on new rows)
